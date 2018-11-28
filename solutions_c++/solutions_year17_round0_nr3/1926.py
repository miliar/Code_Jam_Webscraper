#include <bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
typedef long long ll;

ll n,k;
map<ll,ll> Map;
map<ll,ll>::iterator it;

ll getMax(){ return (Map.rbegin())->first; }

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,tc(1);
	cin >> T;
	while(T--){
        cin >> n >> k;
        Map.clear();
        Map[n] = 1;
        ll a,b;
        while(k){
            ll m = getMax();
            ll r = min(Map[m], k);
            Map[m] -= r;
            if(Map[m] == 0) Map.erase(m);
            ll nw = m / 2;
            if(m&1){
                Map[nw] += 2 * r;
                a = b = nw;
            }else{
                Map[nw] += r;
                Map[nw-1] += r;
                a = nw;
                b = nw-1;
            }
            k -= r;
        }
        cout << "Case #" << tc++ << ": " << a << " " << b << endl;
	}
    return 0;
}
