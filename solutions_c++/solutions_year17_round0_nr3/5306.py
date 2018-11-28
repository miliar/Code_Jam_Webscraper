#include<bits/stdc++.h>
using namespace std;
#define all(a) a.begin(),a.end()
#define allR(v) v.rbegin(),v.rend()
#define IO cin.tie(0);std::ios::sync_with_stdio(false)
#define PB push_back
#define PF push_front
#define set(a,b) memset(a,b,sizeof(a))
#define rep(i,b,n) for(int i=b;i<n;i++)
#define PQ priority_queue
#define scani(x) scanf("%d", &x)
#define scanc(x) scanf("%c", &x)
#define scand(x) scanf("%lf", &x)
#define scanll(x) scanf("%lld", &x)
#define print printf
#define FI freopen("C-small-2-attempt0.in", "r", stdin)
#define FO freopen("o.out", "w", stdout)
typedef long long ll;typedef pair<int, int>ii;typedef vector<ii>vii;typedef vector<int>vi;
#define INF 1000000000
#define EPS 1e-9
int dx[] = {0, 1, 0, 0, -1};
int dy[] = {0, 0, 1, -1, 0};
const ll mod = 1000000000+7;

int main(){
    FI; FO;
    int T; scani(T);
    int c = 0;
    while(T--){
        ll n, k; scanll(n); scanll(k);
        ll a, b;
        PQ<ll>q; q.push(n);
        while(k --){
            int tt = q.top();
            if(tt % 2)a = tt / 2, b = tt / 2;
            else a = tt / 2, b = tt / 2 - 1;
            q.pop();
            q.push(a); q.push(b);
        }
        printf("Case #%d: %lld %lld\n", ++c, a, b);
    }
}
