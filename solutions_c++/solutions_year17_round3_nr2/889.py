#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.txt", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
typedef long long LL;
typedef pair<int,int> pii;
const int MOD = 1e9 + 7;
const int MAX = 1e5 + 5;
vector<pii> v1, v2;

int main() {
    fr;fw;
    int T, cases = 1;
    cin >> T;
    while(T--){
        v1.clear(); v2.clear();
        int n, m;
        cin >> n >> m ;
        REP(i, n){
            int c, d;
            cin >> c >> d;
            v1.pb(mp(c, d));
        }

        sort(v1.begin(), v1.end());

        REP(i, m) {
            int j, k;
            cin >> j >> k;
            v2.pb(mp(j, k));
        }

        sort(v2.begin(), v2.end());

        cout <<"Case #" << cases++<<": ";
        if(n <= 1 && m <= 1){
            cout << 2 <<"\n";
        }
        else{
            if(n == 2){
                int d1, d2;
                d1 = v1[1].S - v1[0].F;
                d2 = 1440 - v1[1].F + v1[0].S;
                if(d1 <= 720 || d2 <= 720) cout << 2 <<"\n";
                else cout << 4 <<"\n";
            }
            else{
                int d1, d2;
                d1 = v2[1].S - v2[0].F;
                d2 = 1440 - v2[1].F + v2[0].S;
                if(d1 <= 720 || d2 <= 720) cout << 2 <<"\n";
                else cout << 4 <<"\n";
            }
        }
    }
    return 0;
}