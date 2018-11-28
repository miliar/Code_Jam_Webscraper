#include <bits/stdc++.h>

#define st first
#define nd second
#define pb push_back
#define mp make_pair

#define cl(x,y) memset(x, y, sizeof(x))
#define dbs(x) cerr << x << endl;
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f, MOD = 1e9+7;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const double PI=acos(-1), EPS = 1e-9;
const ll N = 1e18;

int main () {
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        ll n;
        scanf("%lld", &n);

        bool repeat = true;
        while(repeat) {
            repeat = false;
            ll k=1, last=0;
            while(10*k<=n and k < N) k*=10;
            //printf("k: %lld\nn: %lld\n", k, n);
            while(k) {
                if((n/k)%10 >= last) {
                    last=(n/k)%10;
                    k/=10;
                    //printf("last: %d\n", last);
                }
                else {
                    n -= n%(10*k); n--;
                    repeat = true;
                    break;
                }
            }
        }
        printf("Case #%d: %lld\n", t, n);
    }

    return 0;
}
