# Sistema de Gestão de Produtos Eletrônicos

Uma aplicação web desenvolvida em Python com Django para gerenciar um catálogo completo de produtos eletrônicos como iPhone, PlayStation, Xbox e muito mais.

## 📋 Sobre o Projeto

Este sistema foi criado para facilitar o gerenciamento de um catálogo de produtos eletrônicos, oferecendo uma interface intuitiva tanto para administradores quanto para usuários finais. Utilizando o poder do Django, conseguimos criar uma solução robusta, segura e escalável.

## 🚀 Tecnologias Utilizadas

- *Python 3.x* - Linguagem de programação principal
- *Django* - Framework web completo e robusto
- *SQLite* - Banco de dados leve e eficiente
- *HTML/CSS* - Interface do usuário
- *Django Admin* - Painel administrativo automático

## ✨ Funcionalidades

### Para Administradores
- ✅ Adicionar novos produtos ao catálogo
- ✅ Editar informações de produtos existentes
- ✅ Remover produtos do sistema
- ✅ Gerenciar categorias (iPhone, PlayStation, Xbox, etc.)
- ✅ Controle de estoque
- ✅ Upload de imagens dos produtos
- ✅ Interface administrativa amigável

### Para Usuários
- 🔍 Visualizar catálogo completo de produtos
- 📱 Navegar por categorias específicas
- 📄 Ver detalhes completos dos produtos
- 🏷️ Consultar preços e disponibilidade

## 🏗️ Arquitetura

O projeto segue o padrão *MTV (Model-Template-View)* do Django:

- *Models*: Definem a estrutura dos dados dos produtos
- *Templates*: Interface visual para os usuários
- *Views*: Lógica de negócio e processamento de requisições

### Estrutura do Banco de Dados


Produto
├── nome (CharField)
├── categoria (CharField)
├── preço (DecimalField)
├── estoque (IntegerField)
├── descrição (TextField)
├── imagem (ImageField)
└── data_criação (DateTimeField)


## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. *Clone o repositório*
bash
git clone https://github.com/seu-usuario/sistema-produtos-eletronicos.git
cd sistema-produtos-eletronicos


2. *Crie um ambiente virtual*
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows


3. *Instale as dependências*
bash
pip install -r requirements.txt


4. *Configure o banco de dados*
bash
python manage.py makemigrations
python manage.py migrate


5. *Crie um superusuário*
bash
python manage.py createsuperuser


6. *Execute o servidor*
bash
python manage.py runserver


7. *Acesse a aplicação*
- Aplicação principal: http://127.0.0.1:8000/
- Painel administrativo: http://127.0.0.1:8000/admin/

## 📁 Estrutura do Projeto


projeto/
├── manage.py
├── requirements.txt
├── produtos/
│   ├── models.py      # Modelos de dados
│   ├── views.py       # Lógica das views
│   ├── urls.py        # Roteamento
│   ├── admin.py       # Configuração do admin
│   └── templates/     # Templates HTML
├── static/            # Arquivos estáticos (CSS, JS, imagens)
├── media/             # Upload de arquivos
└── config/
    ├── settings.py    # Configurações do Django
    └── urls.py        # URLs principais


## 🎯 Por que Django?

### Vantagens do Framework

- *Desenvolvimento Rápido*: Com poucas linhas de código, temos um sistema funcional
- *Admin Automático*: Painel administrativo gerado automaticamente
- *Segurança*: Proteção contra ataques comuns (CSRF, XSS, SQL Injection)
- *ORM Poderoso*: Trabalhe com banco de dados usando apenas Python
- *Escalabilidade*: Fácil migração para bancos mais robustos (PostgreSQL, MySQL)
- *Comunidade Ativa*: Grande quantidade de documentação e suporte

### Benefícios do SQLite

- *Simplicidade*: Configuração zero, perfeito para desenvolvimento
- *Portabilidade*: Banco em arquivo único, fácil de backup
- *Performance*: Excelente para projetos pequenos e médios
- *Facilidade*: Ideal para prototipagem e testes

## 🚀 Expansões Futuras

- [ ] Sistema de autenticação de usuários
- [ ] Carrinho de compras
- [ ] Sistema de avaliações
- [ ] API REST para integração mobile
- [ ] Sistema de busca avançada
- [ ] Relatórios de vendas
- [ ] Integração com sistemas de pagamento

## 📝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (git checkout -b feature/nova-funcionalidade)
3. Commit suas mudanças (git commit -am 'Adiciona nova funcionalidade')
4. Push para a branch (git push origin feature/nova-funcionalidade)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

- *Desenvolvedor*: Seu Nome
- *Email*: seu.email@exemplo.com
- *LinkedIn*: [Seu LinkedIn](https://linkedin.com/in/seu-perfil)
- *GitHub*: [@seu-usuario](https://github.com/seu-usuario)

---
