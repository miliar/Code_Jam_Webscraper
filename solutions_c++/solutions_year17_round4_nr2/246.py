#include <bits/stdc++.h>

using namespace std;

#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
  enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge { c b, e; };
sim > rge<c> range(c i, c j) { return rge<c>{i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
#ifdef LOCAL
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair< b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
    *this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};
#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "

int divCeil(int a, int b) {
	assert(b);
	return (a + b - 1) / b;
}

void maxi(int & a, int b) { a = max(a, b); }

void test_case() {
	int seats, people, m;
	scanf("%d%d%d", &seats, &people, &m);
	vector<vector<int>> wanting(seats);
	for(int rep = 0; rep < m; ++rep) {
		int seat, who;
		scanf("%d%d", &seat, &who);
		assert(seat <= seats && who <= people);
		wanting[seat-1].push_back(who-1);
	}
	vector<int> already_this_person(people);
	int already_total = 0;
	int rides = 0;
	for(int i = 0; i < seats; ++i) {
		for(int who : wanting[i]) {
			++already_total;
			maxi(rides, ++already_this_person[who]);
		}
		maxi(rides, divCeil(already_total, i + 1));
	}
	int changed = 0;
	vector<int> tmp(people, 0);
	for(int i = 0; i < seats; ++i) {
		int greedy = 0;
		for(int who : wanting[i])
			maxi(greedy, ++tmp[who]);
		changed += max({0, (int) wanting[i].size() - rides, 0});
		for(int who : wanting[i])
			maxi(greedy, --tmp[who]);
	}
		
		
		/*for(int who : wanting[i]) {
			++already_total;
			maxi(answer, ++already_this_person[who]);
		}
		maxi(answer, divCeil(already_total, i + 1));*/
	printf("%d %d\n", rides, changed);
}

int main(int argc, char * argv[]) {
	int T;
	scanf("%d", &T);
	for(int nr = 1; nr <= T; ++nr) {
		printf("Case #%d: ", nr);
		test_case();
	}
}
