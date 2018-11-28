#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

vi v;

int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		string s;	
		int n;
		cin >> s >> n;

		v.clear();
		for(int i = 0; i < s.size(); i++) {
			v.pb(s[i] == '+');
		}
		
		int cnt = 0;	

		for(int i = 0; i < v.size() - n + 1; i++) {
			if(!v[i]) {
				for(int j = i; j < i + n; j++) {
					v[j] = !v[j];
				}
				cnt ++;
			}
		}
		bool ok = true;
		for(int i = 0; i < v.size(); i++) {
			if(!v[i]) {
				ok = false;
				break;
			}
		}
		if(!ok) {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}else {
			cout << "Case #" << t << ": " << cnt << endl;
		}
	}
	
	
	return 0;
}
