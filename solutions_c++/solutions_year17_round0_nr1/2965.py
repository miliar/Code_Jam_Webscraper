/*input
*/
#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define sp " "
#define fi first
#define se second
#define MOD 1000000007
#define N 1
#define Mask(x) (1ll<<(x))
#define int long long
#define lnode (node<<1)
#define rnode ((node<<1)+1)
#define mid ((l+r)>>1)
using namespace std;
typedef pair<int, int> ii;
typedef long long ll;

string s;
int t, k, cnt , ok;

signed main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> t;
	for(int test = 1; test <= t; ++test){
		cin >> s >> k; cnt = 0, ok = 0;
		for(int i=0; i <= s.size()-k; ++i)
			if(s[i] == '-')
			{
				for(int j=i; j<i+k; ++j)
					if(s[j] == '-') s[j] = '+';
						else s[j] = '-';
				++cnt;
			}
		for(int i=0; i<s.size(); ++i)
			if(s[i] == '-'){
				cout << "Case #" << test << ": IMPOSSIBLE\n"; ok = 1;
				break;
			}
		if(!ok) cout << "Case #" << test << ": " << cnt << endl;
	}
	return 0;
}