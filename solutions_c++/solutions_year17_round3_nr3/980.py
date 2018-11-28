#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

# define pb push_back
# define mp make_pair

typedef long long ll;
typedef pair<int,int> PII;

const int maxn =  (100)+10;
const double eps = (1e-8);

int n,k;
double u,p[maxn];

int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	// freopen("A-large.in", "r", stdin);
	freopen("output.txt","w", stdout);
	int ncase, T;
	double ans;
	ncase = 0;
	cin >> T;
	while(T --) {
		ncase++;
		cin >> n >> k;
		cin >> u;
		for(int i = 1; i <= n; i++) 
			cin >> p[i];
		double minp,minp2;
		int cnt = 0;
		// cout << "u = " << u << endl;
		while((u-0) > eps) {
			minp = minp2 = 100;
			for(int i = 1; i <= n; i++) 
				minp = min(minp, p[i]);
			int k = 0;
			for(int i = 1; i <= n; i++) {
				if(abs(minp - p[i]) < eps)
					k++;
				if(p[i] > minp) {
					minp2 = min(minp2, p[i]);
				}
			}	
			if(abs(minp2-100) < eps) {
				for(int i = 1; i <= n; i++) {
					p[i] = min(1.0, p[i]+u/n);
				}
				u = 0;
			}
			else{
				if(u > k*(minp2-minp)) {
					for(int i = 1; i <= n; i++) {
						if(abs(minp - p[i]) < eps) {
							p[i] = (minp2);
							u -= (minp2 - minp);
						}
					}
				}
				else {
					for(int i = 1; i <= n; i++) {
						if(abs(minp - p[i]) < eps) {
							p[i] += (u/k);
						}
					}
					u = 0;
				}
			}
			++cnt;
			// cout << "cnt = " << cnt << " u = " << u << endl;
			// for(int i = 1; i <= n; i++) {
			// 	cout << "p[" << i << "]=" << p[i] << endl; 
			// 	ans *= p[i];
			// }
		}
		double ans = 1;
		for(int i = 1; i <= n; i++) {
			// cout << "p[" << i << "]=" << p[i] << endl; 
			ans *= p[i];
		}
		printf("Case #%d: %.7lf\n",ncase,ans);
	}
	return 0;
}