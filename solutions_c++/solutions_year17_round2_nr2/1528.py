# include <bits/stdc++.h>
using namespace std;

struct HS {
	int k;
	char c;
};

int main()
{		
	int T; cin >> T;
	for(int tt=1; tt<=T; ++tt) {
		int n; cin >> n;
		vector<int> vec(6, 0);
		for(int i=0; i<vec.size(); ++i) {
			cin >> vec[i];
		}
		
		if (vec[0] * 2 > n or vec[2] * 2 > n or vec[4] * 2 > n) {
			printf("Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}
		
		vector<HS> as = {
			{vec[0], 'R'},
			{vec[2], 'Y'},
			{vec[4], 'B'}
		};
		
		sort(as.begin(), as.end(), [](HS a, HS b){
			return (a.k > b.k);
		});
		
		vector<char> cc(n, '?');
		for(int i=0; i<as[0].k; ++i) {
			cc[i*2] = as[0].c;
		}
		
		for(int i=0; i<n; ++i) {
			if (cc[i] == '?') {
				if (as[1].k > as[2].k) {
					cc[i] = as[1].c;
					as[1].k -= 1;
				}
				else {
					cc[i] = as[2].c;
					as[2].k -= 1;
				}
			}
		}
		
		string ans;
		for(int i=0; i<n; ++i) ans += cc[i];
		
		printf("Case #%d: %s\n", tt, ans.c_str());
	}

	return 0;
}