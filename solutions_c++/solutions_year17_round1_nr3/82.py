#include "bits/stdc++.h"
using namespace std;
#define mt make_tuple
#define mp make_pair
typedef tuple<int, int, int, int> state;
set<state> visited;
int main(){
	int cases; cin >> cases;
	for(int cs = 1; cs <= cases; cs++){
		cout << "Case #" << cs << ": ";
		int hd, ad, hk, ak, b, f;
		cin >> hd >> ad >> hk >> ak >> b >> f;
		bool ok = false;
		visited.clear();
		queue<pair<state, int> > q;
		q.push(mp(mt(hd, ad, hk, ak), 0));
		visited.insert(mt(hd, ad, hk, ak));
		while(!q.empty()){
			state now;
			int crap;
			//cout << "hfal";
			tie(now, crap) = q.front();
			q.pop();
			state nxt;
			int life, attack, elife, eattack;
			tie(life, attack, elife, eattack) = now;
			if(life <= 0) continue;
			if(elife - attack <= 0){
				cout << crap+1 << endl;
				ok = true;
				break;
			}
			auto fnt = [&](state &l){
				if(visited.count(l)) return;
				visited.insert(l);
				q.push(mt(l, crap+1));
				//cerr << "add\n";
			};
			nxt = mt(life - eattack, attack, elife-attack, eattack); fnt(nxt);
			nxt = mt(life - eattack, attack + b, elife, eattack); fnt(nxt);
			nxt = mt(hd - eattack, attack, elife, eattack); fnt(nxt);
			nxt = mt(life - max(0, eattack - f), attack, elife, max(0, eattack - f)); fnt(nxt);
		}
		if(!ok) cout << "IMPOSSIBLE\n";
		cerr << cs << endl;
	}
	return 0;
}


