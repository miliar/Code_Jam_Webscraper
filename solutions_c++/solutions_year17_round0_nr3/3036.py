//#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

//#define F first
//#define S second

// TIMER
std::clock_t __start;
double __duration;
void start_timer() { __start = std::clock(); }
void print_timer() {
	__duration = (std::clock() - __start) / (double)CLOCKS_PER_SEC;
	std::cout << "Duration (msec): " << __duration * 1000 << '\n';
}
// END TIMER

//PI
#define M_PI		3.14159265358979323846
// fast input
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)

template <class T>
T min_(T a, T b) { return (a < b ? a : b); }
template <class T>
T max_(T a, T b) { return (a > b ? a : b); }

double EPS = 1e-16;
bool eq_(const double& lhs, const double &rhs) {
	return (fabs(lhs - rhs) < EPS);
}

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef pair<ll, ll> llll;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef vector<llll> vllll;
typedef vector<int> vi;
typedef vector<ull> vull;

const int INF = int(2e9);
const ll INF_LL = LLONG_MAX;
const ll MOD = 1e9 + 7;
const int MAX_N = 1e6 + 5;


int main() {
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	
	ifstream fin("c.in");
	ofstream fout("c.out");
	ll T;
	fin >> T;
	ll K, N;
	for (int t = 0; t < T; ++t) {
		fin >> N >> K;
		ll row = 0;
		ll total = 0;
		ll nsmall = 0, nbig = 1;
		ll even_val = 0, odd_val = 0;
		ll half = N;
		ll row_total = 0;
		if (N % 2 == 1) {
			odd_val = N;
			even_val = N - 1;
		}
		else {
			even_val = N;
			odd_val = N - 1;
		}
		while (total < K) {
			row_total = ll(pow(2, row));
			if (row == 1 && (N % 2 == 1)) {
				nbig = 2;
			}
			else if (even_val < odd_val) {
				nbig += (row_total - nbig - nsmall);
			}
			else {
				nsmall += (row_total - nbig - nsmall);
			}

			if (half % 2 == 1) {
				odd_val = half;
				even_val = half - 1;
			}
			else {
				even_val = half;
				odd_val = half - 1;
			}

			total += row_total;
			row++;
			half /= 2;
		}
		K = K - (total - row_total); 

		ll res;
		if (K <= nbig)
			res = max(even_val, odd_val);
		else
			res = min(even_val, odd_val);
		
		ll y, z;
		if (res % 2 == 1) {
			y = res / 2;
			z = res / 2;
		}
		else {
			y = res / 2;
			z = res / 2 - 1;
		}
		
		fout << "Case #" << t + 1 << ": " << y<<' '<<z<<'\n';
	}
	return 0;
}