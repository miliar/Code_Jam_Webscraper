#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

int n, k;
double p[100];
double u;

int main(void) {
	int T;
	cin >> T;
	for (int tt = 1; tt<= T; tt++) {
		cin >> n >> k;
		cin >> u;

		priority_queue<pair<double, int> > pq;

		for (int i = 0; i<n ;i++) {
			cin >> p[i];
			pq.push(mk(-p[i], 1));
		}
		while (fabs(u) > 1e-9 && !pq.empty()) {
			double y = -pq.top().fi; int qx = pq.top().se; pq.pop();
			double ynx;
			if (pq.empty()) {
				ynx = 1;
			}
			else ynx = -pq.top().fi;
			//cout << u << ":  "<< y << " " << ynx << " " << qx << "@\n";

			double am = min(u, (ynx - y) * qx);
			u-=am;
			
			y += am / qx;

			if (fabs(y-ynx) < 1e-9){
				if (!pq.empty()) {
					int xx = pq.top().se + qx;
					pq.pop();
					pq.push(mk(-y, xx));
				}
				else pq.push(mk(-y, qx));
			}
			else {
				pq.push(mk(-y, qx));
			}
			//cout << u << " "<< pq.size() << endl;
		}

		double ans = 1;

		while(!pq.empty()){
			ans *= pow(-pq.top().fi, pq.top().se);pq.pop();
		}
		cout << "Case #" << tt << ": ";
		printf("%.9lf\n", ans);


	}
	
	
	return 0;
}
