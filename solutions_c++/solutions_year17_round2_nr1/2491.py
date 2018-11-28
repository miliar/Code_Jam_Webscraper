#include <iostream>
#include <iomanip>
#include <vector>
#include <utility>
#include <string>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<long> vl;
typedef vector<ll> vll;
typedef vector<ii> vpi;

int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; ++c) {
		string out = "";
		double N, D;
		cin >> D >> N;
		double mt = 0;
		for (int i = 0; i < N; ++i) {
			double Di, Si;
			cin >> Di >> Si;
			double t = (D-Di)/Si;
			if (t > mt)
				mt = t;
		}
		
		
		printf("Case #%d: %.6f\n", c, D/mt);
		//cout << setprecision(6) << "Case #" << c << ": " << (double)D/mt << "\n";
	}
	return 0;
}
