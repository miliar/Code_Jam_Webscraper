#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <memory>
#include <unordered_set>
#include <unordered_map>
#include <iterator>
#include <deque>
#include <queue>
#include <cmath>
#include <functional>
#include <numeric>
#include "stdio.h"
#include "time.h"
#include <climits>
#include <stdio.h> 
#include <tuple>
#include <fstream>

#ifdef SAMMAX
#include <ctime>
clock_t beg;
#endif

//#include <boost/lexical_cast.hpp>
//#include <boost/filesystem.hpp>
//#include <boost/utility.hpp>
//#include <boost/aligned_storage.hpp>

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORD(i,a,b) for (int i = (a); i > (b); --i)
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()
#define ABS(a) (((a) >= 0) ? (a) : -(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<vector<pair<int, int> > > VVPI;

const double EPS = 1e-8;

void init() {
#ifdef SAMMAX
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	beg = clock();
#else
	//std::ios_base::sync_with_stdio(false);
	//std::cin.tie(nullptr);
#endif  
}

void finish() {
#ifdef SAMMAX
	fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0*(clock() - beg) / CLOCKS_PER_SEC);
#endif
}

int gcd(int a, int b) { return !a ? b : gcd(b % a, a); }
int lcm(int a, int b) { return a / gcd(a, b) * b; }

void flip(string& s, int a, int b) {
	FOR(i, a, b + 1) {
		if (s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
	}
}

bool isOk(string& s) {
	FOR(i, 0, s.size())
		if (s[i] == '-')
			return false;
	return true;
}

int solve(string& s, int k) {
	int moves = 0;
	int len = s.size();

	FOR(i, 0, len - k + 1) {
		if (s[i] == '-') {
			flip(s, i, i + k - 1);
			moves++;
		}
	}

	return isOk(s) ? moves : -1;
}

int main() {
	init();

	int t;
	cin >> t;
	FOR(caseNum, 1, t + 1) {
		string s;
		int k;

		cin >> s >> k;
		
		printf("Case #%d: ", caseNum);
		
		int res = solve(s, k);

		if (res != -1)
			printf("%d\n", res);
		else
			printf("IMPOSSIBLE\n");
	}

	finish();
	return 0;
}