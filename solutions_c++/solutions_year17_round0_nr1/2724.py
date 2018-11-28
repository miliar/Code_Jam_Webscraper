#include<bits/stdc++.h>
using namespace std;
const bool DBG = 1;

#define TRACE(x)    x
#define WATCH(x)    TRACE(cout << #x" = " << x << endl)
#define WATCHR(a,b) TRACE(for(auto it=a; it!=b;) cout<<*(it++)<<" ";cout<<endl)
#define WATCHC(V)   TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<pair<int,int>> vpii;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cout << fixed << setprecision(15);

	string s;
	int T,k; cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> s >> k;
		vector<bool> v;
		for(char c : s) v.push_back(c == '+');
		int result = 0;
		for(int i = 0; i <= v.size() - k; i++) {
			if(!v[i]) {
				for(int j = 0; j < k; j++) v[i+j] = !v[i+j];
				result ++;
			}
			/*cout << "### ";
			for(auto j : v) cout << ((int)j);
			cout << endl;*/
		}
		bool good = true;
		for(int i = v.size()-1; i > v.size()-k; i--) good &= v[i];
		if(good) cout << result << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
