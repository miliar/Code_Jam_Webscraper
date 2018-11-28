#include <bits/stdc++.h>

using namespace std;

#define debug(x) cerr << "  - " << #x << ": " << x << endl;
#define debugs(x, y) cerr << "  - " << #x << ": " << x << "         " << #y << ": " << y << endl;

typedef long long ll;
typedef pair <ll, ll> pii;
#define fi first
#define se second
#define mp make_pair

int main(){
	int t;
	
	cin >> t;

	int tst = 1;

	while(t--){
		ll n, k;
		cin >> n >> k;
		priority_queue <pair <ll, pii>, vector <pair <ll, pii> >, less <pair <ll, pii> > > pq;
		ll l, r;
		if(n % 2 == 0){
			l = (n - 1) / 2;
			r = n / 2;
			pq.push(mp(l, mp(r, 1)));
		}
		else{
			l = n / 2;
			r = n / 2;
			pq.push(mp(l, mp(r, 1)));
		}
		while(!pq.empty() && k > 0){
			pair <ll, pii> res = pq.top();
			pq.pop();

			ll newL = res.fi;
			ll newR = res.se.fi;
			ll cnt = res.se.se;
			//debugs(newL, newR);
			//debug(cnt);
			//getchar();
			if(newL == 0 && newR == 0){
				k -= cnt;
			}
			else if(newL == 0 && newR == 1){
				k -= cnt;
				pq.push(mp(0ll, mp(0ll, cnt)));
			}
			else{
				k -= cnt;

				if(newL == newR){
					pq.push(mp( (newL - 1) / 2ll, mp(newR / 2ll, 2ll * cnt)));
				}
				else{
					pq.push(mp((newR - 1) / 2ll, mp(newR / 2ll, cnt)));
					pq.push(mp((newL - 1) / 2ll, mp(newL / 2ll, cnt)));
				}
			}
			l = newL;
			r = newR;
		}
		cout << "Case #" << tst++ << ": " << r << " " << l << "\n";
	}
	return 0;
}