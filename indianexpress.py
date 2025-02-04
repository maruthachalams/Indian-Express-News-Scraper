import re
import requests
import time

def single_regex(pattern, target_string):
    data = re.findall(pattern, target_string)
    return data[0] if data else ''
    
def get_response(url):
    content_response = requests.get(url)
    response_code = content_response.status_code
    print(response_code)

    content = content_response.text
    time.sleep(5)

    with open('Result_page.html', 'w', encoding='utf-8') as SP:
        SP.write(content)
    return content 
 
output_data = "News_Title\tDescription\tDate\tArticle_URL\n"

with open("OutPut.txt", 'w') as OP:
    OP.write(output_data)
    
main_url = "https://indianexpress.com/latest-news/"

content = get_response(main_url)

    
PN = single_regex(r'page-numbers\s*dots[\w\W]*?page-numbers[^>]*?>([^>]*?)<',str(content))
if PN == '':
    PN = 1
CPN = 1
for pages in range(1,int(PN)+1):
    updated_main_url = f"https://indianexpress.com/latest-news/page/{pages}"
    
    content = get_response(updated_main_url)
    
    news_blocks = re.findall(r'(<div class="date">[\w\W]*?<\/div>\s*<\/div>)',str(content))
    for news_block in news_blocks:
        news_block = re.sub(r'&#8216;','"',str(news_block))
        news_block = re.sub(r'&#8217;','"',str(news_block))
        News_Title = single_regex(r'<h2><a\s*href\=\"[^>]*?>([^>]*?)<\/a>',str(news_block))
        Description = single_regex(r'<p>([^>]*?)<\/p>',str(news_block))
    
        if Description:
            Description = re.sub(r'\s{2,1000}','',str(Description))
        Date = single_regex(r'\"date\">([^>]*?\d{4})',str(news_block))   
        Article_URL = single_regex(r'<h2><a\s*href\=\"([^>]*?)\"',str(news_block))
       
        output_data = f"{News_Title}\t{Description}\t{Date}\t{Article_URL}\n"

        with open("OutPut.txt", 'a') as OP:
            OP.write(output_data)
    print(f"completed Page Count: {CPN} of {PN}")
    CPN += 1
print("Completed")
