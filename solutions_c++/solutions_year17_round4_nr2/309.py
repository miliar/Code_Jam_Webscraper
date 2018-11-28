#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,b,a) for (int i=(b);i>=(a);i--)

typedef pair<int, int> ii;
typedef long long ll;
int n, c, m;
int vet[10010];
int person[10010];
int promos = 0;

bool solvre(int ans){
    int x;
    int colocados = 0;
    int left;
    promos = 0;
    REP(i, 1, n){
        if(ans<vet[i]){
            x = vet[i] - ans;
            left = (ans * (i-1)) - colocados;
            if(x>left){
                return false;
            }
            if(x>0){
                promos += x;
            }
        }
        colocados += vet[i];
    }
    return true;
}

void solvre(){
    cin>>n>>c>>m;
    int x, y;
    rep(i, 0, n+10){
        vet[i] = 0;
    }
    rep(i, 0, c+10){
        person[i] = 0;
    }
    rep(i, 0, m){
        cin>>x>>y;
        vet[x]++;
        person[y]++;
    }


    int ans = 1;
    int colocados = 0;

    int minimo = 1;
    int maximo = 1e6 + 1000;
    while(minimo<maximo){
        ans = (minimo+maximo)/2;
        if(solvre(ans)){
            maximo = ans;
        }else{
            minimo = ans+1;
        }
    }
    ans = maximo;
    
    y = 0;
    rep(i, 0, c+5){
        y = max(y, person[i]);
    }
    if(y>ans)
        ans = y;

    solvre(ans);
    cout<<ans<<" "<<promos<<endl;

}

int main(){
    int t;
    cin>>t;
    REP(i, 1, t){
        printf("Case #%d: ", i);
        solvre();
    }
}