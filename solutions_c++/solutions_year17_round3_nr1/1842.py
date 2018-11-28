#pragma region includes
#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
using namespace std;
#pragma endregion

int cmp(const void *va, const void *vb) {
#define cmp_type pair<int,int>
	cmp_type a = *(cmp_type *)va;
	cmp_type b = *(cmp_type *)vb;
#undef cmp_type
	if (a.first == b.first) return b.second - a.second;
	return b.first - a.first;
}

int cmp2(const void *va, const void *vb) {
#define cmp_type int
	cmp_type a = *(cmp_type *)va;
	cmp_type b = *(cmp_type *)vb;
#undef cmp_type
	return a - b;
}


#if 0 read_every_x_line_base
char line[10000];
char buffer[10000];
vector<string> readLineW() {
	vector<string> items;
	fgets(line, 10000, in);
	int buffer_off = 0;
	FILL(buffer, 0);
	while (sscanf(line + buffer_off, "%s", &buffer)) {
		int len = strlen(buffer);
		if (!len) break;
		buffer_off += len + 1;
		printf("%s", buffer);
		items.push_back(buffer);
		FILL(buffer, 0);
	}
	return items;
}
#endif 

#define SORT(arr, len) qsort(arr,len,sizeof((arr)[0]),cmp);
#define SORT2(arr, len) qsort(arr,len,sizeof((arr)[0]),cmp2);
#include <chrono>
#include<random>
std::default_random_engine generator(std::chrono::system_clock::now().time_since_epoch().count());
std::uniform_int_distribution<int> distribution(0, 1);
std::uniform_real_distribution<float> distr(0, 1);


FILE *in, *out;

enum CompStage {
	small,
	large,
	test,
};

void open_files(char problem, CompStage stage, int attempt) {
	char buffer[500];
	char *b = buffer;
	b += sprintf(b, "C:\\users\\daniel\\downloads\\%c-", problem);
	switch (stage) {
	case small: b += sprintf(b, "small-attempt%d", attempt); break;
	case large: b += sprintf(b, "large");					break;
	case test:  b += sprintf(b, "test");					break;
	}
	sprintf(b, ".in");
	in = fopen(buffer, "r");
	sprintf(b, ".out");
	out = fopen(buffer, "w");
	assert(in && out);
}



#pragma region defines

#define MAX(a,b) a = a>b?a:b;
#define MIN(a,b) a = a<b?a:b;
#define MIN2(a,b) a = (a==-1||b<a)?b:a;
#define MAX2(a,b) a = (a==-1||b>a)?b:a;

#define MIN2D(a,b,f) if(a==-1||b<a){a=b;f}
#define FILL(s,v) memset(s, v, sizeof(s))
#define FOR(i,n) for(int i = 0; i < n;i++)
#define FOR1(i,n) for(int i = 1; i <= n;i++)
#define FORI(i,v,n) for(int i = v; i < n;i++)

#define FORR(i,n) for(int i = (n)-1; i >= 0;i--)
#define FORR1(i,n) for(int i = n; i > 0;i--)
#define FORRI(i,v,n) for(int i = (n)-1-(v); i >= 0;i--)
#define FORIT(i,collection)for (auto i = collection.begin(); i != collection.end(); ++i)
#define FORRIT(i,collection)for (auto i = collection.rbegin(); i != collection.rend(); ++i)
#define ALL(n) n.begin(),n.end()
const double PI = acos(-1.0);

#define dpr(i) printf(#i ": %d\n", i)
#define pr(s, ...)fprintf(out,s,__VA_ARGS__)
#define re(s, ...)fscanf(in,s,__VA_ARGS__)
#define mkp(first,second)make_pair(first,second)
#pragma endregion

#pragma region types

typedef long long ll;
typedef unsigned long long ull;
#pragma endregion

#pragma region helpers

ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
ll lcm(ll x, ll y) { return x* (y / gcd(x, y)); };
ll llpow(ll base, ll exponent) { ll ack = 1; FOR(i, exponent) { ack *= base; }return ack; }
int choose(int l, int s) { int t = 1; FORI(i, l - s, l) t *= i + 1; int b = 1; FORI(i, 1, s) b *= i + 1; return t / b; }

template<typename T>
int index(vector<T> vec, T value) { auto it = find(ALL(vec), value); return it == vec.end() ? -1 : it - vec.begin(); }
void bit_print(int p) { FORR(i, 32) printf("%d", (p >> i) & 1); printf("\n"); }
int count_1(int p) { int ack = 0; FOR(i, 32)  ack += (p >> i) & 1; return ack; }
int count_0(int p) { int ack = 0; FOR(i, 32)  ack += (p >> i) & 0; return ack; }
int highest_1(ll num) { FORR(i, 64) { if ((num >> i) & 1) return i; }return -1; }
int highest_0(ll num) { FORR(i, 64) { if (!((num >> i) & 1)) return i; }return -1; }
int lowest_1(ll num) { FOR(i, 64) { if ((num >> i) & 1) return i; }return -1; }
int lowest_0(ll num) { FOR(i, 64) { if (!((num >> i) & 1)) return i; } return -1; }
bool bit(ll num, int i) { return (num >> i) & 1; }
ll set_bit(ll num, int bit, int x) { return num ^= (-x ^ num) & ((1ull) << bit); }
#define contains(container, value) (find(ALL(vector),value) != vector.end()) //simpler than playing with templates..
#pragma endregion



namespace std {
	template<> struct hash<pair<int, int>> {
		typedef pair<int,int> argument_type;
		typedef std::size_t result_type;
		result_type operator()(argument_type const& s) const {
			result_type const h1(std::hash<int>{}(s.first));
			result_type const h2(std::hash<int>{}(s.second));
			return h1 ^ (h2 << 1); // or use boost::hash_combine (see Discussion)
		}
	};
};

unordered_map<pair<int, int>, ll> s;

int N;
ll solve(vector<pair<ll,ll>> arr, int index, int left) {
	if (left == 0 || index >= N)return 0;
	pair<int, int> p = mkp(index, left);
	auto it = s.find(p);
	if (it != s.end()) return it->second;

	ll alt_1 = arr[index].first * 2ull * arr[index].second+ solve(arr, index +1, left-1);
	ll alt_2 = solve(arr, index + 1, left);
	ll res = max(alt_1, alt_2);
	s.insert(mkp(p,max(alt_1, alt_2)));
	return res;
}


int main() {
	open_files('A', small, 3);
	int T; re("%d", &T);
	FOR1(test_case, T) {
		s.clear();
		int K;
		re("%d%d", &N, &K);
		vector<pair<ll, ll>> pairs;
		FOR(i, N) {
			int r, h; re("%d%d", &r, &h);
			pairs.push_back(mkp(r, h));
		}
		SORT(&pairs[0], pairs.size());
		ll area_final = 0;
		FOR(j, N - K + 1) {
			ll ret = pairs[j].first * pairs[j].first + pairs[j].first * 2ull * pairs[j].second+solve(pairs, j+1, K-1);;
			area_final = MAX(ret, area_final);
		}

		pr("Case #%d: %.9lf\n", test_case, area_final * PI);
	}
	return 0;
}