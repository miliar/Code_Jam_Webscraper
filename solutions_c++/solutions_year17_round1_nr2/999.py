#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <unordered_set>
#include <unordered_map>
#include <random>       // std::default_random_engine


using namespace std;
typedef long long ll;
#define MODD(a,b) (((a)%(b)+(b))%(b))
#define EPS 1E-8
#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x))

using namespace std;


int main()
{
	int T; cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		int n, p;
		cin >> n >> p;
		vector<int> r(n);
		for (int i = 0; i < n; i++) cin >> r[i];
		vector<deque<double> > Q(n);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < p; j++) {
				int q;
				cin >> q;
				double k = double(q) / r[i];
				Q[i].push_back(k);
			}
		for (int i = 0; i < n; i++) sort(Q[i].begin(), Q[i].end());
		int ans = 0; 

		bool hasempty = 0;
		while (!hasempty) {
			double minf = 9E9, maxf = 0;
			int minid=0;
			for (int i = 0; i < n; i++) {
				if (Q[i].front() < minf) {
					minf = Q[i].front();
					minid = i;
				}
				maxf = max(maxf, Q[i].front());
			}
			bool good = 0;
			int midf = int((minf + maxf) / 2);
			for (int k = max(midf - 3, 1); k <= midf + 3; k++) {
				if (minf / k >= 0.9 - EPS && minf / k <= 1.1 + EPS
					&& maxf / k >= 0.9 - EPS && maxf / k <= 1.1 + EPS) {
					good = 1;
					cerr << k << endl;
					break;
				}
			}
			if (good) {
				ans++;
				for (int i = 0; i < n; i++) {
					Q[i].pop_front();
					hasempty |= Q[i].empty();
				}
			}
			else {
				Q[minid].pop_front();
				hasempty |= Q[minid].empty();
			}
		}
		
		printf("Case #%d: %d\n", cs, ans);
	}
	
	return 0;
}