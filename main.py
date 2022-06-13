def parse(query: str) -> dict:
    return {}

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

def parse_cookie(query: str) -> dict:
    dic={}
    find=query.rfind(';')
    query_new=query[:find] +query[find+1:]
    print(query_new)
    a = query_new.split(';')
    if len(a) > 1:
        for i in a:
            c = i.split('=',1)
            dic[c[0]]=c[1]
    return dic

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('film=mentalist;year=2008;season=1')=={'film': 'mentalist', 'year': '2008', 'season': '1'}
    assert parse_cookie('car=BMW;color=blue;country=Germany;')=={'car':'BMW','color':'blue','country':'Germany','year':'1999'}
    assert parse_cookie('coffe=latte;price=150')=={'coffee':'latte','price':'150'}
    assert parse_cookie('video=python;time=13:30;author=Mike')=={'video':'python','time':'13:30','author':'Mike'}
    assert parse_cookie('language=Ukrainian;symbols=5000;')=={'language':'Ukrainian','symbols':'5000'}
    assert parse_cookie('hotel=Hilton;guests=3;city=Kiev')=={'hotel':'Hilton','guests':'3','city':'Kiev'}
    assert parse_cookie('author=Orwell;book=1984;price=200')=={'author':'Orwell','book':"1984",'price':'200'}
    assert parse_cookie('group=412b;lessons=15;')=={'group':'412b', 'lessons':'15'}
    assert parse_cookie('cinema=Scream;year=2020')=={'cinema':'Scream','year':'2020'}
    assert parse_cookie('pizza=Hawaii;price=300;place=DreamTown')=={'pizza':'Hawaii','price':'300','place':'DreamTown'}
