#include <bits/stdc++.h>
using namespace std;
#define forn(i,n) for(int i=0 ;i < (int)(n); i++)
#define forni(i,n) for(int i=1 ;i <= (int)(n); i++)
#define dforn(i, n) for( tint i=(int) (n)-1 ;i >= 0; i--)
typedef long long tint;
const int MAXN=500100, inf=1e9;

tint n, k, l, r, hay, rnd, sz, bigch, smallch;

int main(){
    freopen("C-large.in", "r", stdin);
    freopen("Output_Problem_3.txt", "w", stdout);
    int t;
    scanf(" %d", &t);
    forn(cs, t){
    //while(cin >> n){
        //puts("Ingrese los numeros");
        cin >> n >> k;
        /*if(k==1){
            l = (n - 1) / 2;
            r = n - 1 - l;
            printf("Case %d: %d %d\n", cs+1, l, r);
            continue;
        }*/
        hay=1;
        while(hay*2 <= k){hay*=2;}
        rnd = hay; hay--;
        n -= hay; k -= hay;
        sz = n / rnd;
        bigch = n - sz * rnd;
        smallch = rnd - bigch;
        if(k <= bigch)sz++;
        l = (sz - 1) / 2;
        r = sz - 1 - l;
        //cout << smallch << " " << bigch << " " << sz << endl;
        cout << "Case #" << cs+1 << ": " << max(l, r) << " " << min(l, r) << endl;
    }
    return 0;
}

