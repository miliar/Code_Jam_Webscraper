#include <algorithm>
#include <numeric>
#include <iostream>
#include <vector>
#include <cmath>

#define FOR(it, seq) for(auto it : seq)
#define FORI(it, beg, end) for(auto it = beg; it != end; ++it)

#define DBG(x) cout << x
#define DBGV(v) {cout << "["; FOR(i_, v) {DBG(i_); cout << ", ";} cout << "]" << endl; }

using namespace std;

typedef long long lint;
typedef vector<int> VI;
typedef vector<lint> VL;

struct Pancake {
	Pancake(double r, double h, double circ, double base):
		r(r), h(h), circ(circ), base(base) {}

	double r, h;
	double circ, base;
};

typedef vector<Pancake> VP;
typedef vector<Pancake *> VPP;

int T;

double solve() {
	int N, K;
	cin >> N;
	cin >> K;

	VP pancakes;

	FORI(i, 0, N) {
		double r, h;
		cin >> r;
		cin >> h;
		pancakes.emplace_back(r, h, 2*M_PI*h*r, M_PI*r*r);
	}

	// sort by radius
	struct {
		bool operator()(Pancake &a, Pancake &b) {
			return a.r > b.r;
		}
	} cmp_radius;

	sort(pancakes.begin(), pancakes.end(), cmp_radius);
	
	VPP pancakes_ordered;
	FORI(i, 0, N) {
		pancakes_ordered.push_back(pancakes.data() + i);
	}

//	cout << "Ordered: ";
//	FOR(p, pancakes_ordered) {
//		cout << p->r << ",";
//	}
//	cout << endl;

	// sort by circ
	struct {
		bool operator()(Pancake *a, Pancake *b) {
			return a->circ > b->circ;
		}
	} cmp_circ;

	struct {
		double operator()(double presum, Pancake *p) {
			return presum + p->circ;
		}
	} sum_circ;

	double max = 0;
	FORI(i, 0, N) {
		if (i + K > N)
			break;

		VPP pk_work(pancakes_ordered);
		double sum = pk_work[i]->base + pk_work[i]->circ;
		//cout << "Trying base: " << i << ", " << pk_work[i]->r << endl;

		sort(pk_work.begin() + i + 1, pk_work.end(), cmp_circ);
		sum += accumulate(pk_work.begin() + i + 1, pk_work.begin() + i + K, 0.0, sum_circ);
		//cout << "sum: " << sum << endl;

		if (sum > max)
			max = sum;
	}


	return max;
}

int main(int argc, char *argv[])
{
	cin >> T;

	cout.precision(17);
	FORI(t, 0, T) {
		cout << "Case #" << (t+1) << ": ";

		// print answer
		cout << solve();

		cout << endl;
	}


	return 0;
}
