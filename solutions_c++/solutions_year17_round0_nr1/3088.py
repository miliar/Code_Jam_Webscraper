#include<iostream>
#include<cstdio>
#include<cstring>
#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
typedef long long ll;
const int maxn = 1024;

int T, N, K;
char S[maxn];

int main(){
    freopen("entrada.txt", "r", stdin);
    freopen("salida.txt", "w", stdout);

    scanf("%i", &T);
    forn(t, T){
        scanf("%s %d", S, &K);
        N = strlen(S);
        int Ans = 0;
        for(int i = 0; i <= N - K; ++i)
            if( S[i] == '-' ){
                ++Ans;
                forn(j, K)
                    S[i+j] = '-' + '+' - S[i+j];
            }
        bool possible = true;
        forn(i, N)
            if( S[i] == '-' )
                possible = false;
        if( possible )
            printf("Case #%d: %d\n", t+1, Ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", t+1);
    }

    return 0;
}
