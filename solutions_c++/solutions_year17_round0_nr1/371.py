
// In the name of God
#include <bits/stdc++.h>

using namespace std;
#define Size(x) ((int)(x).size())
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int>pii;
const int INF = 1e9 + 10;
const int MN = 2e3 + 5;

bool mk[MN];

int main()
{
	ios_base :: sync_with_stdio(false) ,cin.tie(0) , cout.tie(0);
	int T;cin>>T;
	int cnt = 0;
	while(T--){
		++cnt;
		string s;cin >> s;
		int k;cin>>k;
		int n = Size(s);
		int cur = 0 , ans = 0;
		bool Fail = false;
		memset(mk , 0 , sizeof mk);
		for(int i=0;i<n;++i){
			if(cur&1){
				if(s[i] == '-') s[i] = '+';
				else s[i] = '-';
			}
			if(s[i] == '-'){
				if(i > n-k) Fail = true;
				++cur , ++ans , mk[i+k-1] = true;
			}if(mk[i]) --cur;
		}
		if(Fail) cout << "Case #" << cnt << ": IMPOSSIBLE\n";
		else cout << "Case #" << cnt << ": " << ans << '\n';
	}
	return 0;
}

