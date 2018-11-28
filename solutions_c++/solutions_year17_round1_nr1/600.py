#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;
typedef vector<ii> vii;

int r, c;
string b[25];
string origb[25];
vii pos;

bool test(int r1, int c1, int r2, int c2, char let) {
	if(r1 < 0 or r2 > r - 1 or c1 < 0 or c2 > c - 1) return 1;
	for(int i = r1; i <= r2; i++) {
		for(int j = c1; j <= c2; j++) {
			if(b[i][j] != let and b[i][j] != '?')	
				return 1;
		}
	}
	return 0;
}

int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ":" << endl;
		cin >> r >> c;
		pos.clear();
		for(int i = 0; i < r; i++) {
			cin >> origb[i];
		}
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				if(origb[i][j] != '?') {
					pos.pb(mp(i, j));
				}
			}
		}

		bool ok = false;
		while(!ok) {
			for(int i = 0; i < r; i++) {
				b[i] = origb[i];
			}
			random_shuffle(pos.begin(), pos.end());
			for(int i = 0; i < pos.size(); i++) {
				int curr = pos[i].fi;
				int curc = pos[i].se;
				char curl = b[curr][curc];
				int lt_r = curr;
				int lt_c = curc;
				int rb_r = curr;
				int rb_c = curc;
				while(!test(lt_r, lt_c, rb_r, rb_c, curl)) {
					lt_r--;
				}
				lt_r++;
				while(!test(lt_r, lt_c, rb_r, rb_c, curl)) {
					lt_c--;
				}
				lt_c++;

				while(!test(lt_r, lt_c, rb_r, rb_c, curl)) {
					rb_r++;
				}
				rb_r--;
				while(!test(lt_r, lt_c, rb_r, rb_c, curl)) {
					rb_c++;
				}
				rb_c--;
				for(int j = lt_r; j <= rb_r; j++) {
					for(int k = lt_c; k <= rb_c; k++) {
						b[j][k] = curl;
					}
				}
			}
			ok = true;
			for(int i = 0; i < r; i++) {
				for(int j = 0; j < c; j++) {
					if(b[i][j] == '?')	{
						ok = false;
						break;
					}
				}
				if(!ok) break;
			}

		}
		for(int i = 0; i < r; i++) {
			cout << b[i] << endl;
		}
	}
	
	return 0;
}
