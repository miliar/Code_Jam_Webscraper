#define _CRT_SECURE_NO_DEPRECATE
#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
/*--------------------------------*/
#define pb push_back
#define INT_MIN (1 << 31)
#define INT_MAX ~(1 << 31)
#define LL_MIN -9223372036854775808
#define LL_MAX  9223372036854775807
#define lower(c) char(32 | c)
#define upper(c) char(~32 & c)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define RFOR(i, a, b) for (int i = a; i >= b; i--)
#define FORIT(i, a, b) for (auto i = a; i != b; i++)
#define READ freopen("input.txt", "r", stdin);
#define WRITE freopen("output.txt", "w", stdout);
#define MOD ll(1000000007)
#define PI acos(-1)
/*-------------------------------------------------------------*/


bool tidy(ll n){

	int last = n % 10;
	n /= 10;

	while (n){
		if (n % 10 > last) return 0;
		last = n % 10;
		n /= 10;
	}

	return 1;
}

int main() {


	int T;
	scanf("%d\n", &T);
	FOR(t, 1, T){
		ll n;
		scanf("%lld", &n);

		ll m = n;
		int digits = 0;
		while (m){
			digits++;
			m /= 10;
		}


		while (!tidy(n)){
			int i = digits;

			while (i > 1){

				ull a = pow(10, i), b = pow(10, i - 1);
				int x = (n%a) / (a / 10), y = (n%b) / (b / 10);

				if (y < x){
					n -= b;
					n += (b - 1) - (n % b);
					break;
				}

				i--;
			}
		}

		printf("Case #%d: %lld\n", t, n);

	}

	return 0;
}