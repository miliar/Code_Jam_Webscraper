/*input
4
132
1000
7
111111111111111110
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
int t;

signed main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> t; cin.ignore();
	for(int test = 1; test <= t; ++test){
		getline(cin, s);
		for(int i=0; i<s.size() - 1; ++i)
			if(s[i] > s[i+1]){
				s[i]--; int ok = i + 1;
				for(int j = i-1; j >= 0; --j)
					if(s[j] > s[j+1]) --s[j], ok = j+1;
				for(int j=ok; j<s.size(); ++j)
					s[j] = '9'; 
				break;
			}
		if(s[0] == '0') for(int i=1; i<s.size(); ++i) s[i] = '9';
		reverse(s.begin(), s.end()); 
		while(*(--s.end()) == '0') s.erase(--s.end());
		reverse(s.begin(), s.end());
		cout << "Case #" << test << ": " << s << "\n";
	}
	return 0;
}