# Guia de Uso do Script de Detecção de XSS

Este guia fornece instruções sobre como usar um script em Python para automatizar a busca por vulnerabilidades de Cross-Site Scripting (XSS) em sites.

## Pré-requisitos
- Python 3 instalado em seu sistema.
- As bibliotecas `requests` e `BeautifulSoup4` instaladas. Você pode instalá-las usando o pip:

    ```bash
    pip install requests beautifulsoup4
    ```

## Passos para usar o script
1. **Copie o código:**  
   Copie o código do script fornecido e cole em um arquivo com a extensão `.py`, por exemplo, `xss_tester.py`.

2. **Abra o terminal:**  
   Navegue até o diretório onde você salvou o arquivo usando o terminal.

3. **Execute o script:**  
   Execute o script com o comando:

    ```bash
    python xss_tester.py
    ```

4. **Digite a URL alvo:**  
   Quando solicitado, insira a URL do site que você deseja testar (certifique-se de ter permissão para isso).

5. **Aguarde os resultados:**  
   O script irá testar a URL fornecida e informará se alguma vulnerabilidade XSS foi encontrada.

## Atenção
Use este script apenas em sites para os quais você tem permissão explícita para testar. Testes não autorizados são ilegais e antiéticos.

## Exemplo de Uso
Se você quiser testar um site, digite algo como:

