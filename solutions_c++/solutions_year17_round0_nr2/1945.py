#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const int maxn = 100000 + 10;

void solve(string &s){
	int n = (int)s.length();

	for (int i = 0; i + 1 < n; ++i){
		if (s[i] > s[i + 1]){
			if (s[i] == '1' && s[i + 1] == '0'){
				for (int i = 0; i < n - 1; ++i)
					cout << 9;
				cout << endl;
				return;
			}

			int p = i;
			while (p > 0 && s[p - 1] == s[p])
				p--;
			s[p]--;

			for (int j = 0; j < n; ++j){
				if (j <= p) cout << s[j];
				else cout << 9;
			}
			cout << endl;
			return;
		}
	}

	cout << s << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

#ifdef MARX
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif

	int t;

	cin >> t;

	int tc = 1;

	while (t--){
		string s; 
		cin >> s;

		cout << "Case #" << tc++ << ": ";
		solve(s);
	}
	return 0;
}