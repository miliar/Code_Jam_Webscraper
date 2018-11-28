#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

int main(void) {
	ios::sync_with_stdio(false);
	int T;cin >> T;
	for (int tt = 1; tt<=T; tt++) {
		cout << "Case #" << tt << ": " ;

		string s;cin >> s;
		int k; cin >> k;
		int l = 0, r = s.size()-1;

		int ans = 0;
		for (int i = 0; i<s.size() - k + 1; i++) {
			if(s[i] == '+') continue;
			if (s[i] == '-') {
				for (int j = 0; j<k; j++) {
					if (s[i+j] == '-')
						s[i+j] = '+';
					else s[i+j] = '-';
				}
				++ans;
			}
		}
		bool ok = true;
		for (int i = 0; i<s.size(); i++)
			ok &= s[i]=='+';
		if (!ok)
			cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";



	}
	
	
	return 0;
}
