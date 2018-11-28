#include <iostream>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <algorithm>
#include <string>
#include <vector>
#include <queue> 
#include <stack>
#include <deque> 
#include <set>
#include <map>
#include <unordered_map>
#include <list>
#include <utility>
#include <bitset>
#include <stdio.h>
#include <iomanip>
#include <climits>
#include <cmath>
#include <functional>
#include <sstream>
#include <math.h>
#include <stdio.h>
#include <tuple>
#include <regex>
#define FOR(i,n) for(int i=0; i<n ; i++)
#define pi 3.14159265358979323846
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define F first
#define S second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const double EPS = 1e-9;
const ll MOD = 1000000007;
const int INF = 2000 * 1000 * 1000;
const int MAX = 1005; // 2*2^ceil(log_2(n)) - 1
using namespace std;
int popcount(int n) { bitset<32> b(n); return b.count(); }
long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { ll temp = gcd(a, b); 	return temp ? (a / temp * b) : 0; }
template <typename T>
T modpow(T base, T exp, T modulus){ base %= modulus; T result = 1; while (exp > 0){ if (exp & 1) result = (result * base) % modulus; base = (base * base) % modulus;	exp >>= 1; }return result; }
inline bool isInteger(const std::string & s){ if (s.empty() || ((!isdigit(s[0])) && (s[0] != '-') && (s[0] != '+'))) return false; char * p; strtol(s.c_str(), &p, 10); return (*p == 0); }

int d,n;
vector<int> pos, vel;


int main()
{	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc; cin >> tc;
	cout << fixed << setprecision(10);
	FOR(k, tc)
	{
		scanf("%d %d", &d, &n);
		pos = vector<int>(n), vel = vector<int>(n);
		FOR(i, n) scanf("%d %d", &pos[i], &vel[i]);	
		ld st = 0, ed = 1e18, mid, mx = 0;
		FOR(i, n)		
			mx = max(mx, (ld(d) - pos[i]) / vel[i]);		
		FOR(j, 1000)
		{
			mid = (st + ed) / 2;
			if ((d/mid) >= mx) st = mid;
			else ed = mid;
		}
		cout << "Case #" << k + 1 << ": " << st << endl;
	}
	return 0;
}




