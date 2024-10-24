from config import app, templates
from sqlalchemy.orm import Session

from db import get_db, User, Post

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, Form, Depends, File

products = {'apple': 100, 'orange': 200}


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):

    return templates.TemplateResponse('index.html', {'title': 'Home', 'request': request})


@app.get('/test', response_class=HTMLResponse)
async def test(request: Request):
    names = ['Vlad', 'Kyryl', 'Ivan', 'Illia']
    return templates.TemplateResponse('test.html', {'names': names, 'request': request})


@app.get('/page2', response_class=HTMLResponse)
async def test(request: Request):
    names_age = {'Vlad': '14', 'Kyryl': '10', 'Ivan': '15', 'Illia': '12'}
    return templates.TemplateResponse('page_2.html', {'names_age': names_age, 'request': request})


@app.get('/addition-numbers/{num}/{num1}', response_class=HTMLResponse)
async def results(request: Request, num: int, num1: int):
    names_age = {'Vlad': '14', 'Kyryl': '10', 'Ivan': '15', 'Illia': '12'}
    result = num + num1
    return templates.TemplateResponse('page_2.html', {'result': result, 'names_age': names_age, 'request': request})


@app.get('/calculate', response_class=HTMLResponse)
async def results1(request: Request, num1: int = None, num2: int = None, opp: str = None):
    result = 'No answer'
    if opp == '+':
        result = num1 + num2
    elif opp == '-':
        result = num1 - num2
    elif opp == '*':
        result = num1 * num2
    elif opp == '/':
        result = num1 / num2
    return templates.TemplateResponse('calculate.html', {'result': result, 'request': request})


@app.get('/item/{name}', response_class=HTMLResponse)
async def results(request: Request, name: str):
    pr = products[name]
    return templates.TemplateResponse('item.html', {'product': pr, 'request': request})


@app.get('/product')
async def product(request: Request, price: int = 0):
    for name, p in products.items():
        if p == price:
            return templates.TemplateResponse('item.html', {'product': name, 'request': request})


@app.get('/registration', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse('register.html', {'request': request})


@app.post('/registration')
async def register(request: Request,
                   username: str = Form(),
                   password: str = Form(),
                   password_repeat: str = Form(),
                   email: str = Form(),
                   db: Session = Depends(get_db)
                   ):
    user = User(username=username, password=password, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return RedirectResponse('/', status_code=303)


@app.get('/login', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@app.post('/post-create')
async def post_create(text: str = Form(), image=File(), db: Session = Depends(get_db)):
    image.save(f'static/img/{image.filename}')
    post = Post(text=text, image='image.png', user_id=1)
    db.add(post)
    db.commit()
    db.refresh(post)
    return {}
