#include <bits/stdc++.h>
using namespace std;
#define all(a)						a.begin(), a.end()
#define minimum(a)					*min_element(a.begin(), a.end())
#define maximum(a)					*max_element(a.begin(), a.end())
#define cerr1(a)					cerr << "[ " << a << " ]\n"
#define cerr2(a,b)					cerr << "[ " << a << " , " << b << " ]\n"
#define cerr3(a,b,c)				cerr << "[ " << a << " , " << b << " , " << c << " ]\n"
#define fi 							first
#define se 							second
/*DAM SEHGAL*/
typedef long long ll;typedef long double ld;typedef vector<int> vi;typedef vector<char> vc;
typedef vector<string> vs;typedef vector<ll> vl;typedef set<int> si;typedef set<string> ss;
typedef map<int, int> mii;typedef map<string, int> msi;typedef pair<int, int> pii;
typedef pair<ll, ll> pll;typedef vector<pii> vii;typedef vector<vi> vvi;typedef vector<vii> vvii;
const int INF = 0x3f3f3f3f, MOD = 1e9 + 7;
ll power(ll a, ll n) {ll p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
ll power(ll a, ll n, ll mod) {ll p = 1;while (n > 0) {if(n%2) {p = p * a; p %= mod;} n >>= 1; a *= a; a %= mod;} return p % mod;}
ll add(ll a , ll b , ll mod = MOD){return (a + b) % mod;}
ll sub(ll a , ll b , ll mod = MOD){return ((a-b)%mod + mod)%mod;}
ll mul(ll a , ll b , ll mod = MOD){return (a * b) % mod;}
ll divide(ll a , ll b , ll mod = MOD){return (a * power(b,mod-2,mod))%mod;}
ll sqrt_floor(ll x){ll y = sqrt(x); while (y * y > x)--y; while ((y + 1) * (y + 1) <= x) ++y; return y;}


int main(int argc, char const *argv[])
{
	int totalTest;
	cin >> totalTest;
	for (int testCase = 1; testCase <= totalTest; ++testCase)
	{
		string str;
		int k, cunt = 0;
		cin >> str >> k;

		int len = str.length();
		for (int i = 0; i <= len - k; ++i)
		{
			if(str[i] == '-')
			{
				++cunt;
				for (int j = 0; j < k; ++j)
				{
					if (str[i + j] == '+')
						str[i + j] = '-';
					else
						str[i + j] = '+';
 				}
			}
		}
		for (int i = 0; i < len; ++i)
		{
			if (str[i] == '-')
			{
				cout << "Case #" << testCase << ": " << "IMPOSSIBLE\n";
				goto end;
			}
		}
		cout << "Case #" << testCase << ": " <<  cunt << "\n";

		end:;
	}	
	return 0;
}