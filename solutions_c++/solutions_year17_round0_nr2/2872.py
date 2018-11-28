#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()
#define li long long
#define ld long double
#define x first
#define y second
#define pt pair<int, int>
#define pll pair<li, li>
#define forn(i, t) for(int i = 0; i < (t); i++)
#define fore(i, f, t) for(int i = (f); i < (t); i++)
#define forr(i, f, t) for(int i = (f) - 1; i >= (t); i--)
#define all(x) (x).begin(), (x).end()
#define ins insert

using namespace std;


const int INF = 1e9;
const int MOD = 1e9 + 7;
const li INF64 = 1e18;
const ld EPS = 1e-7;

mt19937 myrand(time(NULL));

string s;
int n;


bool read(){
	char buf[20];
	if(scanf("%s\n", buf) != 1)
		return 0;
	s = buf;
	n = sz(s);
	return 1;
}


void solve(){
	++n;
	s = '0' + s;
	forn(i, n - 1)
		if (s[i] > s[i + 1]){
			forr(j, i + 1, 1)
				if (s[j - 1] < s[j]){
					s[j]--;
					fore(k, j + 1, n)
						s[k] = '9';
					break;
				}
			break;
		}
	if (s[1] == '0')
		printf("%s\n", s.substr(2, n).c_str());
	else
		printf("%s\n", s.substr(1, n).c_str());
}


int main(){
	#ifdef _DEBUG
		freopen("input.txt", "r", stdin);
	#endif
	int n;
	scanf("%d\n", &n);
	forn(i, n){
		read();
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}