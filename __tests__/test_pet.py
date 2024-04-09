# 1 - bibliotecas # engine(motor)
import pytest
import requests
import json

# 2 - classe( opcional no python)
# 2.1 - atributos ou variaveis
pet_id = 487524501   # codigo do animal
pet_name = "Juca"
pet_category_id = 1
pet_category_name = "dog"
pet_tag_id = 1
pet_tag_name = "vacinado"  # tidtudlo
pet_status = "available"   # staus do animal

# informações em comum
url='https://petstore.swagger.io/v2/pet'
headers={'Content-Type': 'application/json'}

# 2.2 - funções
# Consulta e resultado esperado
def test_post_pet():
    # Configura
    # dados de entrada esta no arquivo json
    pet=open('./fixtures/json/pet1.json')  # abre o arquivo json
    data=json.loads(pet.read())  # ler o conteudo e carreaga como json em uma variavel data
    # dados de saida resultado esperado estão nos atributos acima da funções
    
    # Executa
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )
    
    
    # Valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id']== pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['status']== pet_status

def test_get_pet():
    # Confugura
    # dados de entrada e saida / resultado esperado dentro da seção de atributos antes das funções
    response = requests.get(
    url=f'{url}/{pet_id}',     # chama o endereço do get/ consulta passando o codigo do animal
    headers=headers,
    # não tem corpo de mensagem / body
    )
    #Executa
    response_body  = response.json()

    # Valida

    assert response.status_code == 200
    assert response_body['name']== pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tag']['id']== pet_tag_id
    assert response_body['status']== pet_status
