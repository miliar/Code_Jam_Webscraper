#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <tuple>
#include <algorithm>
#include <iterator>
#include <functional>
#include <cmath>
#include <math.h>
#include <time.h>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const double Pi = 3.14159265359;
const string alphabet = "abcdefghijklmnopqrstuvwxyz";

namespace Helpers {
	class Help {
	public:
		static bool is_prime(const ll& n) {
			for (ll i = 2; i*i <= n; i++)
				if (n%i == 0)
					return false;
			return true;
		}

		static ll gcd(const ll& a, const ll& b) {
			return b ? gcd(b, a % b) : a;
		}

		static ll gcdex(ll a, ll b, ll & x, ll & y) {
			if (a == 0) {
				x = 0; y = 1;
				return b;
			}
			ll x1, y1;
			ll d = gcdex(b%a, a, x1, y1);
			x = y1 - (b / a) * x1;
			y = x1;
			return d;
		}

		static ll lcm(ll a, ll b) {
			return a / gcd(a, b) * b;
		}

		static ll fibonacci(ll n) {
			fibnums.resize(n + 1, -1);
			return fibonacci_core(n);
		}

		static ll kmp(const std::string& sMain, const std::string& sFind) {
			std::vector<ll> vPrefix(sMain.size(), 0);
			// prefix
			for (ll i = 1; i < sMain.size(); i++) {
				ll k = vPrefix[i - 1];
				while (k > 0 && sMain[i] != sMain[k])
					k = vPrefix[k];
				if (sMain[i] == sMain[k])
					k++;
				vPrefix[i] = k;
			}
			// kmp
			ll answer = -1;
			ll k = 0;
			for (ll i = 0; i < sMain.length(); i++) {
				while (k > 0 && sMain[i] != sFind[k])
					k = vPrefix[k - 1];
				if (sMain[i] == sFind[k])
					k++;
				if (k == sFind.size()) {
					answer = i - sFind.size() + 1;
					break;
				}
			}
			return answer;
		}

		static ll combinations(ll n, ll k, ll mod) {
			if (n < k) swap(n, k);

			ll top = 1;
			for (ll x = max(n - k, k) + 1; x <= n; x++)
				top = (top*x) % mod;

			ll bottom = 1;
			for (ll x = 1; x <= min(n - k, k); x++)
				bottom = (bottom*x) % mod;

			ll x, y, g = gcdex(bottom, mod, x, y);

			if (g != 1)	throw(L"COMBINATIONS FAILED!");

			x = (x % mod + mod) % mod;

			return (top * x) % mod;
		}

	private:
		static vector<ll> fibnums;
		static ll fibonacci_core(ll n) {
			if (n == 0)
				return 0;
			if (n == 1 || n == 2)
				return 1;

			return fibnums[n] != -1 ? fibnums[n] : (fibnums[n] = fibonacci_core(n - 1) + fibonacci_core(n - 2));
		}
	};

	vector<ll> Help::fibnums;
}
/*************************************************************************/
/*************************************************************************/


int main()
{
	ifstream fin("in.in");
	ofstream fout("out.out");

	int test_n;
	fin >> test_n;
	for (int test = 0; test < test_n; test++) {
		int d, n;
		fin >> d >> n;
		typedef struct DP {
			int pos, speed;
		};
		
		vector<DP> v(n);
		for (auto& e : v) fin >> e.pos >> e.speed;

		sort(v.begin(), v.end(), [d](auto a, auto b) { return (double(d - a.pos) / a.speed) < (double(d - b.pos) / b.speed); });

		double time = double(d - v.back().pos) / v.back().speed;

		double ans = d / time;

		fout << "Case #" << test + 1 << ": " << fixed << setprecision(6) << ans << endl;
	}

	return 0;
}