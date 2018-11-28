#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int main() {
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
		int D, N;
		cin >> D >> N;
		double K[N], S[N];
		FOR (i, N)
			cin >> K[i] >> S[i];
		double s = 1.0, e = 10000000000000.0, mid;
		while (e - s > 1e-6) {
			mid = (s + e) / 2.0;
			bool possible = true;
			double t = 1.0 * D / mid;
			FOR (i, N)
				if ((D - K[i]) / S[i] > t) {
					possible = false;
					break;
				}
			if (possible)
				s = mid;
			else
				e = mid;
		}
		printf("%.7lf", s);
    cout << "\n";
  }
  return 0;
}
