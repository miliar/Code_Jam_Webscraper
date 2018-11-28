#include <bits/stdc++.h>
using namespace std;
#define forn(i,n) for(int i=0 ;i < (int)(n); i++)
#define forni(i,n) for(int i=1 ;i <= (int)(n); i++)
#define dforn(i, n) for( tint i=(int) (n)-1 ;i >= 0; i--)
typedef long long tint;
const int MAXN=500100, inf=1e9;

int sz, pos;
char n[30], act;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("Output_Problem_2.txt", "w", stdout);
    int t;
    cin >> t;
    forn(cs, t){
    //while(cin >> n){
        cin >> n;
        sz = strlen(n);
        act = n[0];
        bool caca = false;
        forn(i, sz-1){if(n[i+1] < act){pos = i; caca=true; break;} act=n[i+1];}
        if(caca){
            while(pos > 0 and n[pos-1] == n[pos])pos--;
            n[pos]--; pos++;
            while(pos < sz){n[pos]='9'; pos++;}
        }
        cout << "Case #" << cs+1 << ": ";
        pos = 0;
        while(n[pos]=='0')pos++;
        for(int i = pos; i < sz; i++)cout << n[i]; cout << endl;
    }
    return 0;
}

