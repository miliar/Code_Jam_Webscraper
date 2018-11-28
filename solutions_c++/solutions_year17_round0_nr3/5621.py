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
        int N, K;
        cin >> N >> K;
        priority_queue<int> q;
        q.push(N);
        REP(i,K-1) {
            int a = q.top();q.pop();
            a--;
            q.push(a/2);
            q.push(a-a/2);
        }
        int ans = q.top();
        ans--;
        cout << "Case #" << i+1 << ": "<< ans-ans/2 << " " << ans/2 << endl;
    }
    return 0;
}
