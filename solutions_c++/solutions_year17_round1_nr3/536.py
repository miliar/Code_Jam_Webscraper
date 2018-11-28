#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

typedef long long lli;

lli INF = 99999999LL;

typedef struct{
    lli attack;
    lli health;
    lli init;
} Aux;

Aux pessoa, dragao;
lli b, d;

bool operator<(const Aux &l, const Aux &r){
    if (l.attack == r.attack){
        return l.health < r.health;
    }
    return l.attack < r.attack;
}

bool operator==(const Aux &l, const Aux &r){
    return l.attack == r.attack && l.health == r.health;
}

typedef struct{
    Aux pessoa;
    Aux dragao;
    bool state;
} Estado;

bool operator<(const Estado &l, const Estado &r){
    if (l.pessoa == r.pessoa){
        if (l.dragao == r.dragao){
            return l.state < r.state;
        }
        return l.dragao < r.dragao;
    }
    return l.pessoa < r.pessoa;
}


map<Estado, int> mapa;
lli get(Aux pessoa, Aux dragao, bool state){
    cout << pessoa.health << " " << dragao.health << " " << state << endl;
    Estado s;
    s.pessoa = pessoa;
    s.dragao = dragao;
    s.state = state;
    if (dragao.health <= 0)
        return INF;
    if (pessoa.health <= 0)
        return 0;
    if (mapa.find(s) == mapa.end()){
        if (state){
            dragao.health -= pessoa.attack;
            mapa[s] = INF;
            mapa[s] = get(pessoa, dragao, !state);
        }
        else{
            mapa[s] = INF;
            lli ans = INF;
            {
                Aux pessoa_ = pessoa;
                Aux dragao_ = dragao;
                pessoa_.health -= dragao_.attack;
                ans = min(ans, get(pessoa_, dragao_, !state));
            }
            {
                Aux pessoa_ = pessoa;
                Aux dragao_ = dragao;
                dragao_.attack += b;
                if (dragao.attack >= pessoa.health)
                    ans = 0;
                else
                    ans = min(ans, get(pessoa_, dragao_, !state));
            }
            {
                Aux pessoa_ = pessoa;
                Aux dragao_ = dragao;
                dragao_.health = dragao_.init;
                ans = min(ans, get(pessoa_, dragao_, !state));
            }
            {
                Aux pessoa_ = pessoa;
                Aux dragao_ = dragao;
                pessoa_.attack = max(0LL, pessoa_.attack-d);
                ans = min(ans, get(pessoa_, dragao_, !state));
            }
            mapa[s] = min(INF, 1 + ans);
        }
    }
    return mapa[s];
}

int main(){ _
    int t;
    cin >> t;
    for (int q = 1; q <= t; q++){
        cin >> dragao.health >> dragao.attack
            >> pessoa.health >> pessoa.attack
            >> b >> d;
        dragao.init = dragao.health;
        mapa.clear();
        lli ans = get(pessoa, dragao, false);
        cout << "Case #" << q << ": ";
        if (ans >= INF)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
	return 0;
}
