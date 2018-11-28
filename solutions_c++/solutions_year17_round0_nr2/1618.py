#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forab(i,a,b) for( int i = (a); i < (b); i++ )
#define forn(i,n) forab(i,0,n)
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>

const int MXN = 20;


int mn [MXN];

void solve() {
    string s;
    cin >> s;
    int n = s.size();
    forn(i,n-1){
        if (s[i] > s[i+1]) {
            int q = s[i];
            forn(j,i+1) {
                if (s[i-j] == q) {
                    s[i-j]--;
                    s[i-j+1] = '9';

                }
                else {
                    break;
                }
            }
            forab(j,i+1,n) {
                s[j] = '9';
            }
            break;
        }
    }
    int j = 0;
    while (s[j] == '0') {
        j++;
    }
    cout << s.substr(j,n);
}


int main(){
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    forn(i,T){
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
}