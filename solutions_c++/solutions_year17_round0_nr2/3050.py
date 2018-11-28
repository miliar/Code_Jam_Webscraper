#include<iostream>
#include<cstdio>
#include<algorithm>
#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
const int maxn = 1<<4;
const int INF = 1<<29;
typedef long long ll;

int T, N;
char S[32];

void flip(int p){
    S[p-1]--;
    for(int i = p; S[i]; ++i)
        S[i] = '9';
}

int main(){
    freopen("entrada.txt", "r", stdin);
    freopen("salida.txt", "w", stdout);

    scanf("%i", &T);
    forn(t, T){
        scanf("%s", S);

        bool updated;
        do{
            updated = false;
            for(int i = 1; S[i]; ++i)
                if( S[i] < S[i-1] ){
                    updated = true;
                    flip(i);
                }
        }while( updated );

        int pos;
        for(pos = 0; S[pos] == '0'; ++pos);

        printf("Case #%d: %s\n", t+1, S+pos);

    }

    return 0;
}
