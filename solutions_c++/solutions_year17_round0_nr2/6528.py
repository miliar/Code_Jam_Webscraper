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
 
bool firstInvalid(string str, int& pos)
{
	for(int i = 0; i < str.length() - 1; ++i)
	{
		if(str[i] > str[i+1])
		{
			pos = i; 
			return false;
		}
	}
	return true;
}
 
int main(int argc, char const *argv[])
{
	int t; 
	cin >> t;
	for(int testCases = 1; testCases <=t; testCases++)
	{
		string str;
		cin >> str;
		int pos = -1;
		while(!firstInvalid(str, pos))
		{
			str[pos]--;
			for(int i = pos + 1; i < str.length(); ++i) 
				str[i] = '9';
		}
		while(str[0] == '0') 
			str.erase(str.begin());
		cout << "Case #" << testCases << ": " + str + "\n";
	}
	return 0;
}