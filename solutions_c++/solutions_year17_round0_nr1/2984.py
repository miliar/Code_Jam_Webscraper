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
	
	ifstream fin("a.in");
	ofstream fout("a.out");
	int T, K;
	fin >> T;
	for (int t = 0; t < T; ++t) {
		string S;
		fin >> S >> K;
		int idx = 0;
		bool fail = false;
		int count = 0;
		while (idx < S.size()) {
			if (S[idx] == '+')
				++idx;
			else {
				if (idx + K - 1 < S.size()) {
					count++;
					for (int i = 0; i < K; ++i)
						S[idx+i] = (S[idx+i] == '+' ? '-' : '+');
					++idx;
				}
				else {
					fail = true;
					break;
				}
			}
		}
		fout << "Case #" << t + 1<<": ";
		if (fail)
			fout << "IMPOSSIBLE\n";
		else
			fout << count << '\n';
		

	}
	return 0;
}