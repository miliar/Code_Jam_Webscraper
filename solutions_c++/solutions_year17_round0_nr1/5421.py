#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(ll i=0; i<(ll)(n); i++)
#define FOR(i,n,m) for (ll i=n; i<(ll)(m); i++)
#define pb push_back
#define INF 1000000007LL
#define all(a) (a).begin(),(a).end()
#define chmin(a,b) a=min(a,b)
#define chmax(a,b) a=max(a,b)

typedef long long ll;
typedef pair<int,int> p;

int dy[4]={-1,1,0,0};
int dx[4]={0,0,1,-1};

int T;
int main(){
    ios::sync_with_stdio(false);
    cin >> T;
    REP(i,T) {
        string S;
        int K;
        cin >> S >> K;
        vector<int> sint(S.length(),0);
        REP(j, S.length()) {
            if(S[j]=='+') {
                sint[j] = 1;
            }
        }
        int cnt = 0;
        REP(j, S.length()-K+1) {
            if (sint[j]==0) {
                cnt++;
                REP(k, K) {
                    sint[j+k]=1-sint[j+k];
                }
            }
        }
        int flag = 0;
        REP(j, S.length()) {
            if(sint[j]==0){
                flag = 1;
            }
        }
        if (flag) {
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << i+1 << ": " << cnt << endl;
        }
    }
    
    return 0;
}
