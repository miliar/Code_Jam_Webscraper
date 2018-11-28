#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define mp make_pair 

int main() {
	int tests, t;
	cin >> tests;
	int n, r, o, y, g, b, v;
	map<int, int> mapa;
	mapa[0] = 3;
	mapa[2] = 5;
	mapa[4] = 1;
	for(t = 1; t <= tests; t++) {
		cin >> n >> r >> o >> y >> g >> b >> v;
		vi colors;
		colors.pb(r);
		colors.pb(o);
		colors.pb(y);
		colors.pb(g);
		colors.pb(b);
		colors.pb(v);
	
		vi pri;
		if(colors[0] >= colors[2]) {
			if(colors[0] >= colors[4]) {
				pri.pb(0);
				if(colors[2] >= colors[4]) {
					pri.pb(2);
					pri.pb(4);
				}
				else {
					pri.pb(4);
					pri.pb(2);
				}
			}
			else {
				pri.pb(4);
				pri.pb(0);
				pri.pb(2);
			}
		}
		else{
			if(colors[2] >= colors[4]) {
				pri.pb(2);
				if(colors[0] >= colors[4]) {
					pri.pb(0);
					pri.pb(4);
				}
				else {
					pri.pb(4);
					pri.pb(0);
				}
			}
			else {
				pri.pb(4);
				pri.pb(2);
				pri.pb(0);
			}
		}
		vi ans;
		bool imp = false;
		int i = 0;
		while(colors[pri[0]] > 0 || colors[pri[1]] > 0 || colors[pri[2]]) {
			if(colors[pri[0]] > 0) {
				if(colors[pri[0]] >= colors[pri[1]] && colors[pri[0]] >= colors[pri[2]]) {
					ans.pb(pri[0]);
					colors[pri[0]]--;
					while(colors[mapa[pri[0]]] > 0) {
						ans.pb(mapa[pri[0]]);
						i++;
						colors[mapa[pri[0]]]--;
						if(colors[pri[0]] > 0) {
							ans.pb(pri[0]);
							colors[pri[0]]--;
						}
						else{
							if(sz(ans) != n) {
								imp = true;
								break;
							}
							else if(ans[0] != pri[0]){
								imp = true;
								break;
							}
						}
					}
				}
			}
			if(colors[pri[1]] > 0) {
				if(colors[pri[1]] >= colors[pri[2]]) {
					ans.pb(pri[1]);
					colors[pri[1]]--;
					while(colors[mapa[pri[1]]] > 0) {
						ans.pb(mapa[pri[1]]);
						i++;
						colors[mapa[pri[1]]]--;
						if(colors[pri[1]] > 0) {
							ans.pb(pri[1]);
							colors[pri[1]]--;
						}
						else{
							if(sz(ans) != n) {
								imp = true;
								break;
							}
							else if(ans[0] != pri[1]){
								imp = true;
								break;
							}
						}
					}
				}
			}
			if(colors[pri[2]] > 0) {
				if(colors[pri[2]] > colors[pri[0]] || ans[sz(ans)-1] == pri[0]) {
					ans.pb(pri[2]);
					colors[pri[2]]--;
					while(colors[mapa[pri[2]]] > 0) {
						ans.pb(mapa[pri[2]]);
						i++;
						colors[mapa[pri[2]]]--;
						if(colors[pri[2]] > 0) {
							ans.pb(pri[2]);
							colors[pri[2]]--;
						}
						else{
							if(sz(ans) != n) {
								imp = true;
								break;
							}
							else if(ans[0] != pri[2]){
								imp = true;
								break;
							}
						}
					}
				}
			}
		}
		if(imp) {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
		else if(colors[1] > 0 || colors[3] > 0 || colors[5] > 0){
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
		else if(ans[0] == ans[n-1]) {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
		else{
			string s = "";
			for(int j = 0; j < n; j++) {
				if(ans[j] == 0) {
					s+='R';
				}
				else if(ans[j] == 1) {
					s+='O';
				}
				else if(ans[j] == 2) {
					s+='Y';
				}
				else if(ans[j] == 3) {
					s+='G';
				}
				else if(ans[j] == 4) {
					s+='B';
				}
				else{
					s+='V';
				}
			}
			cout << "Case #" << t << ": " << s << endl;
		}
	}
	return 0;
}