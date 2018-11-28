#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <unordered_set>

using namespace std;

#define DEBUG 1
typedef long long ll;

fstream fin("smallA.in");
fstream fout("smallA.out");

ll toll(const string& s){
	istringstream ss(s);
	ll ret;
	ss >> ret;
	return ret;
}


double alg(ll D, ll N) {

    vector<pair<ll, ll> > vec;

    for (ll i = 0; i < N; ++i) {
        ll t1, t2;
        fin >> t1 >> t2;
        vec.push_back(make_pair(t1, t2));
    }

    sort(vec.begin(), vec.end(), [](const pair<ll, ll> & a, const pair<ll, ll> & b) -> bool
    {
        return a.first < b.first;
    });


    double maxTime = 0.0;
    for (int i=0; i<vec.size(); ++i) {
        maxTime = max(maxTime, (D - vec[i].first) / (double)vec[i].second);
        //cout << ceil((D - vec[i].first) / (double)vec[i].second) << endl;

    }

    return D / maxTime;
}


void f_main(const int& testCase) {
	ll D, N;
	fin >> D >> N;
	double res = alg(D, N);

	if (DEBUG) {
		cout << "Case #" << testCase << ": " << setprecision(6) << res << endl;
	}
	fout << "Case #" << testCase << ": " << setprecision(6) << res << endl;

}


int main() {
	int T;
	fin >> T;
    cout << fixed;
    fout << fixed;
	for (int t=0; t < T; ++t) {
		f_main(t+1);
	}
	return 0;
}
