#include<iostream>
#include<cstdio>
#include<algorithm>
#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
const int maxn = 1<<4;
const int INF = 1<<29;
typedef long long ll;

int T;
ll N, K;

int main(){
    freopen("entrada.txt", "r", stdin);
    freopen("salida.txt", "w", stdout);

    scanf("%i", &T);
    forn(t, T){
        scanf("%lld %lld", &N, &K); --K;

        ll n_par = 0, n_impar = 0, tam_par, tam_impar;

        if( N % 2 ) n_impar++;
        else        n_par++;

        /// ver caso cuando no entra al for

        for(ll tam_row = 1; tam_row <= K; tam_row *= 2){

            tam_par = tam_impar = N;
            if( N % 2 ) tam_par--;
            else        tam_impar--;

            ll impar = n_impar;
            n_impar = n_par;

            if( (tam_impar/2) % 2 ) n_impar += 2 * impar;
            else                    n_par   += 2 * impar;

            N /= 2;
            K -= tam_row;
        }

        if( N % 2 ){
            if( n_impar <= K ) --N;
        }else if( n_par <= K ) --N;

        printf("Case #%d: %lld %lld\n", t+1, N/2, (N%2) ? (N/2) : (N/2-1));
    }

    return 0;
}
