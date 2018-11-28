#define _USE_MATH_DEFINES


#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

#define ll long long

typedef tuple<double, double, int> Tuple;

bool cmp_h(const Tuple& p1, const Tuple& p2) {
	return get<0>(p1) > get<0>(p2) || (get<0>(p1) == get<0>(p2) && get<1>(p1) > get<1>(p2));
}

bool cmp_s(const Tuple& p1, const Tuple& p2) {
	return get<1>(p1) > get<1>(p2) || (get<1>(p1) == get<1>(p2) && get<0>(p1) > get<0>(p2));
}



int main() {

	std::ifstream in("C:/Users/Yoav/Documents/Visual Studio 2015/Projects/20171b/20171b/A-large (1).in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("C:/Users/Yoav/Documents/Visual Studio 2015/Projects/20171b/20171b/A-large (1).out");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int n, k;
		cin >> n >> k;

		vector<double> r(n), h(n), hs(n), s(n);
		for (int i = 0; i < n; i++) {
			cin >> r[i] >> h[i];
			hs[i] = 2 * M_PI * r[i] * h[i];
			s[i] = M_PI * r[i] * r[i];
		}

		vector<Tuple> tuples(n), tuples_s(n);
		for (int i = 0; i < n; i++)
			tuples[i] = make_tuple(hs[i], s[i], i);
		tuples_s = vector<Tuple>(tuples);

		sort(tuples.begin(), tuples.end(), cmp_h);
		sort(tuples_s.begin(), tuples_s.end(), cmp_s);

		double best_s = 0;
		vector<Tuple> best_pankakes;

		for (int i = 0; i < n; i++) {
			vector<Tuple> pankakes;
			pankakes.push_back(tuples_s[i]);
			int j = get<2>(tuples_s[i]);
			double s0 = get<1>(tuples_s[i]);
			int num_pankakes = 1;
			for (int l = 0; l < n && num_pankakes < k; l++) {
				if (get<2>(tuples[l]) != j && get<1>(tuples[l]) <= s0) {
					num_pankakes++;
					pankakes.push_back(tuples[l]);
				}
			}
			double outcome = get<1>(pankakes[0]);
			if (num_pankakes == k) {
				for (int l = 0; l < k; l++)
					outcome += get<0>(pankakes[l]);
			}

			if (num_pankakes == k && outcome >= best_s) {
				best_s = outcome;
				best_pankakes = pankakes;
			}
		}

		cout << fixed << setprecision(7) << best_s << endl;

	}
	return 0;
}