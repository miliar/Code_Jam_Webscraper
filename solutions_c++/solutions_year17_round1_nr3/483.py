#include <bits/stdtr1c++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ": ";
		// strategy: (D..CD..even more...CD..even even more...)*(B..CB..C)*(AAAA)+
		ll Hd, Ad, Hk, Ak, B, D;
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		
		typedef tuple<int, int, int, int> state;
		state st{Hd, Ad, Hk, Ak};
		map<state, int> dist;
		dist[st] = 0;
		queue<state> q({st});
		map<state, state> par;
		
		bool found = false;
		state en;
		while (!q.empty()) {
			int hd, ad, hk, ak, d = dist[q.front()];
			tie(hd, ad, hk, ak) = q.front();
			//cerr << "At: " << d << " " << hd << " " << ad << " " << hk << " " << ak << endl;
			q.pop();
			
			if (hd <= 0) continue;
			if (hk <= 0) {
				en = make_tuple(hd, ad, hk, ak);
				cout << d << endl;
				found = true;
				break;
			}
			
			// must cure
			vector<state> go;
			/*
			if (hd-ak+D <= 0) {
				state nxt{Hd-ak, ad, hk, ak};
				go.push_back(nxt);
			} else {
			*/
				state nxt;
				// try debuff
				int ak_ = max(ak-D, 0LL);
				nxt = state{hd-ak_, ad, hk, ak_};
				go.push_back(nxt);
				
				// try buff
				nxt = state{hd-ak, ad+B, hk, ak};
				go.push_back(nxt);
				
				// try attack
				nxt = state{(hk-ad > 0 ? hd-ak : hd), ad, hk-ad, ak};
				go.push_back(nxt);
				
				// try cure
				nxt = state{Hd-ak, ad, hk, ak};
				go.push_back(nxt);
			//}
			
			for (const state& nxt : go) {
				if (!dist.count(nxt)) {
					//cerr << "Exploring: " << d << " " << get<0>(nxt) << " " << get<1>(nxt) << " " << get<2>(nxt) << " " << get<3>(nxt) << endl;
					dist[nxt] = d + 1;
					//par[nxt] = make_tuple(hd, ad, hk, ak);
					q.push(nxt);
				}
			}
		}
		
		if (!found) cout << "IMPOSSIBLE" << endl;
		else {
			/*
			string s = "A";
			state cur = en;
			while (cur != st) {
				state p = par[cur];
				int hd0, ad0, hk0, ak0, hd1, ad1, hk1, ak1;
				tie(hd0, ad0, hk0, ak0) = p;
				tie(hd1, ad1, hk1, ak1) = cur;
				if (ad0 < ad1) s.push_back('B');
				if (ak1 != 0 && hd0 <= hd1) s.push_back('C');
				if (ak0 > ak1) s.push_back('D');
				if (hk0 > hk1) s.push_back('A');
				cur = p;
				cerr << hd1 << " " << ad1 << " " << hk1 << " " << ak1 << endl;
			}
			reverse(s.begin(), s.end());
			cout << s << endl;
			//*/
		}
    }
	return 0;
}