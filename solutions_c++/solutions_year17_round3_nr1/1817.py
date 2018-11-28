#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <stdlib.h>
#include <string.h>
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <ctype.h>
#include <iomanip>      // std::setprecision

#include <math.h>
#define FOR(x,y,z) for(int x = (y); x < (z); x++)
#define FORD(x,y,z) for(int x = (y); x >= z; x--)
#define REP(r,n) for(int r = 0; r < (n); r++)
#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define MAXUS 1000001
#define MAXUS2 9000005
#define PI 3.1415926
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); i++)
#define ALL(u) (u).begin(),(u).end()
#define epsilon 0.000001
using namespace std;
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PR;



LL global_top_number = 0;
int main() {
	LL T, N, K;	
	cin >> T;
	long long int a, b;
	vector<pair<long long int, int> > sizes;
	vector<pair<long long int, long long int> >v;
	for (int t = 1; t <= T; t++) {
		cin >> N >> K;
		sizes.clear();
		v.clear();
		for (int i = 0; i < N; i++) {
			cin >> a >> b;
			v.PB({a,b});
			long long int d = 2*a*b;
			pair<long long int, int> e = {d, i};
			sizes.PB(e);
		}
		sort(sizes.begin(), sizes.end());
//		for (int i = 0; i < N; i++) {			cout << sizes[i].ST << " "<< endl;
		//}
		long double bestResult = 0.;
		int lastRadius = MAXUS;
		int l = 0;
		for (int i = 0; i < N; i++) {
			int radiusPodstawa = v[i].ST;
			vector<pair<long long int, long long int>> indexes = {v[i]};
			for (int j = N-1; j >= 0 && indexes.size() < K; j--) {
				// cout << sizes[j].ND << " " << i << endl;	
				if (sizes[j].ND == i) continue;
				if (radiusPodstawa >= v[sizes[j].ND].ST) {
					pair<int, int> e = v[sizes[j].ND];
					indexes.PB(e);
				}
				if (indexes.size() == K) break;
			}
			if (indexes.size() < K) continue;
			sort(indexes.begin(), indexes.end());
			long double result = 0;
			// cout << indexes.size();
			for (int j = K-1; j >= 0; j--) {
					auto p = indexes[j];
					// cout << p.ST << " " << p.ND << endl;
					if (j == K-1) {
						// cout << p.ND*2*p.ST*PI + p.ST*p.ST*PI;
						result += p.ND*2*p.ST*PI + p.ST*p.ST*PI;
					} else {
						// cout << p.ND * 2 * p.ST * PI;
						result += p.ND * 2 * p.ST * PI;
					}
					// cout << result;
			}
			if (bestResult < result) bestResult = result;
		}
		cout << "Case #"  <<t << ": ";	
		cout << setprecision(1001) << bestResult << endl;
	}
	return 0;
}
