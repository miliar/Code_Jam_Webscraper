#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n, k;
set<ll> st;
map<ll, ll> cnt;

int main(){
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		st.clear(), cnt.clear();
		cin >> n >> k; st.insert(n); cnt[n]++;

		ll lst = -1;
		while (k > 0ll){
			ll mx = *st.rbegin(); st.erase(mx); lst = mx;
			k -= cnt[mx];

			if (mx & 1)
				cnt[mx>>1] += cnt[mx]*2ll, st.insert(mx>>1);
			else{
				cnt[mx>>1] += cnt[mx], st.insert(mx>>1);
				cnt[(mx>>1)-1] += cnt[mx], st.insert((mx>>1)-1);
			}
		}
		
		if (lst & 1)
			printf("Case #%d: %lld %lld\n", w, lst>>1, lst>>1);
		else
			printf("Case #%d: %lld %lld\n", w, lst>>1, (lst>>1)-1);
	}
	return 0;
}
