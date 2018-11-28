#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

double p[51];
double pd[53][53];
double pdr[53][53];
int n, k;
double u;
double eps = 1e-4;

void read() {
	scanf("%d %d", &n, &k);
	scanf("%lf", &u);
	for (int i = 0; i < n; i++) {
		scanf("%lf", &p[i]);
	}
}

vector<double> calc(vector<double>& v, int k) {
	int n = v.size();
	for (int i = 0; i <= n; i++) pd[0][i] = pdr[n][i] = 0;
	pd[0][0] = pdr[n][0] = 1;
	
	for (int i = 1; i <= n; i++) {
		for (int j = n; j >= 0; j--) {
			pd[i][j] = pd[i-1][j-1] * v[i-1] + pd[i-1][j] * (1-v[i-1]);
		}
	}

	for (int i = n-1; i >= 0; i--) {
		for (int j = n; j >= 0; j--) {
			pdr[i][j] = pdr[i+1][j-1] * v[i] + pdr[i+1][j] * (1-v[i]);
		}
	}

	vector<double> ans(n, 0);

	for (int i = 0; i < n; i++) {
		for (int left = 0; left < k; left++) {
			ans[i] += pd[i][left] * pdr[i+1][k-1-left];
		}
	}
	
	return ans;
}

void solve() {
	vector<double> a;
	for (int i = 0; i < n; i++) a.push_back(p[i]);

	calc(a,k);
	double curr = 0;
	for (int i = k; i <= n; i++) curr += pd[n][i];

	int its = u * 10000;
	int it = 0;
	while (u > 0) {
		//if (it % 10000 == 0) printf("its = %d, it = %d, ts = %d\n", its, it, its * 9 / 10);
		if (it <= its * 999.0 / 1000.0) eps = 1e-4;
		else eps = 1e-7;
		eps = min(eps, u);
		//double eps = min(u, 1e-4 + (it / 10000.0) * (1e-9 - 1e-4));
		//printf("u = %f\n", u);
		double b = -1;
		int idx = -1;

		vector<double> calcs = calc(a,k);
		for (int i = 0; i < n; i++) if (a[i]+eps <= 1) {
			a[i] += eps;
			double nw = calcs[i];
			if (nw > b) {
				b = nw;
				idx = i;
			}
			a[i] -= eps;
		}

		if (idx == -1) break;
		curr += b * eps;
		a[idx] += eps;
		u -= eps;
		it ++;
	}

	calc(a,k);
	curr = 0;
	for (int i = k; i <= n; i++) curr += pd[n][i];
	printf("%.15f\n", curr);
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
			fprintf(stderr, "Case %d solved\n", i+1);
		}
	}
}