#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define fst first
#define snd second
#define debug(x) cout << #x << " = " << x << endl;
typedef long long ll;
typedef pair<int, int> ii;

int main(){
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; tt++){
		string s;
		int k;
		cin >> s >> k;
		
		int ans = 0;
		for(int i = 0; i + k <= s.size(); i++){
			if(s[i] == '-'){
				for(int j = i; j < i + k; j++)
					s[j] = s[j] == '-' ? '+' : '-';
				ans++;
			}
		}

		bool ok = 1;
		for(auto c : s)
			ok &= c == '+';

		printf("Case #%d: ", tt);
		if(!ok)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << endl;
	}
	return 0;
}