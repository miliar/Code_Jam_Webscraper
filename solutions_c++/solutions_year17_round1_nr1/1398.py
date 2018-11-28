#include<bits/stdc++.h>

using namespace std;

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1) {
  cerr << name << " : " << arg1 << endl;
}

template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) {
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << " : " << arg1<<" | ";
  __f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define all(a) a.begin(), a.end()
#define endl '\n'
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define boost  ios_base::sync_with_stdio(false);
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

typedef long long llint;
typedef long long ll ;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

const int mod = 1e9 + 7 ;
ll powmod(ll a,ll b) {ll res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}
ll gcd(ll a , ll b){return a==0?b:gcd(b%a,a);}
/*---------------------------------------------------------------------------------------------------------------------*/
const int maxn = 100010;
const int inf = INT_MAX;
char a[50][50];
int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tt = 0;
	cin >> tt;
	int t = 0;
	while(tt--) {
		t++;
		cout << "Case #" << t << ": \n";
		int r, c;
		cin >> r >> c;
		for(int i = 0; i < r; i++)
			cin >> a[i];
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				if(a[i][j] != '?') {
					int k = j - 1;
					while(k >= 0 && a[i][k] == '?') {
						a[i][k] = a[i][j];
						k--;
					}
				}
			}
		}

		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				if(a[i][j] != '?') {
					int k = j + 1;
					while(k < c && a[i][k] == '?') {
						a[i][k] = a[i][j];
						k++;
					}
				}
			}
		}
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				if(a[i][j] != '?') {
					int k = i - 1;
					while(k >= 0 && a[k][j] == '?') {
						a[k][j] = a[i][j];
						k--;
					}
				}	
			}
		}
		for(int i = 0; i < r; i++) {
			for(int j = 0; j < c; j++) {
				if(a[i][j] != '?') {
					int k = i + 1;
					while(k < r && a[k][j] == '?') {
						a[k][j] = a[i][j];
						k++;
					}
				}	
			}
		}
		for(int i = 0; i < r; i++)
			cout << a[i] << endl;
	}
    return 0;
}