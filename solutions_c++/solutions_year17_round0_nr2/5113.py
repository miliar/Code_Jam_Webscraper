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
#define FI freopen("B-large.in", "r", stdin)
#define FO freopen("o.out", "w", stdout)
typedef long long ll;typedef pair<int, int>ii;typedef vector<ii>vii;typedef vector<int>vi;
#define INF 1000000000
#define EPS 1e-9
int dx[] = {0, 1, 0, 0, -1};
int dy[] = {0, 0, 1, -1, 0};
const ll mod = 1000000000+7;

vector<ll> tidy;

void doit(ll n){
    if(n > 1e18)return;
    tidy.PB(n);
    rep(i, (n ? n % 10 : 1), 10)doit(n * 10 + i);
}

int main(){
    FI; FO;
    doit(0);
    sort(all(tidy));
    int T; scani(T);
    int c = 0;
    while(T --){
        ll n; scanll(n);
        int i = lower_bound(all(tidy), n) - tidy.begin();
        printf("Case #%d: %lld\n", ++c, (i == tidy.size() || tidy[i] > n ? tidy[i - 1] : tidy[i]));
    }
}
