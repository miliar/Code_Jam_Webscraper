#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e5+4;
typedef long long ll;

int main(){
// #ifndef ONLINE_JUDGE
freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);
// #endif
	string s;
	int t, k, cs = 0; cin >> t;
	while(t--){
		bool flag = true;
		int f = 0;
		cin >> s >> k;
		int i = 0;
		for (i = 0; i < s.length() - k; ++i)
		{
			if(s[i] == '+') ;
			else{
				for (int j = i; j < i + k; ++j)
				{
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				f++;
			}
		}
		int cnt_ = 0, cnt = 0;
		for (; i < s.length(); ++i)
		{
			if(s[i] == '-') cnt_++;
			else cnt++;
		}
		if(cnt_ == k) f++;
		else if(cnt == k) ;
		else flag = false; 
		if(flag) printf("Case #%d: %d\n", ++cs, f);
		else printf("Case #%d: IMPOSSIBLE\n", ++cs);
	}
	return 0;
}