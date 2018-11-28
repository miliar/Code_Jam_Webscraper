#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;
const long long int md = 1e15;
const double mt = 1e30;
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int i=1;i<=t;i++) {
		int q,n;
		in >> n >> q;
		vector <int> e(n),s(n);
		for (int j=0;j<n;j++) {
			in >> e[j] >> s[j];
		}
		vector <vector <long long int> > d(n,vector<long long int>(n,0));
		for (int j=0;j<n;j++) for (int k=0;k<n;k++) {
			in >> d[j][k];
			if (d[j][k] == -1) d[j][k] = md;
		}
		vector <int> u(q),v(q);
		for (int j=0;j<q;j++) in >> u[j] >> v[j];
		
		for (int j=0;j<n;j++) for (int k=0;k<n;k++) for (int l=0;l<n;l++) {
			if (d[k][l] > d[k][j] + d[j][l]) d[k][l] = d[k][j] + d[j][l];
		}
		
		vector <double> a(q,0.);
		for (int j=0;j<q;j++) {
			vector <bool> b(n,true);
			int cur = u[j]-1;
			vector <vector <double> > c(n,vector<double>(n,mt));
			vector <double> x(n,mt);
			
			b[cur] = false;
			for (int k=0;k<n;k++) for (int l=0;l<n;l++) c[cur][l] = 0.;
			x[cur] = 0.;
			while (cur != v[j]-1) {
				for (int k=0;k<n;k++) {
					if (d[cur][k] <= e[cur]) {
						if (c[k][cur] > x[cur] + (double)d[cur][k] / s[cur]) c[k][cur] = x[cur] + (double)d[cur][k] / s[cur];
						if (x[k] > c[k][cur]) x[k] = c[k][cur];
					}
				}
				
				for (int k=0;k<n;k++) if (b[k]) cur = k;
				for (int k=0;k<n;k++) if (b[k] && x[k] < x[cur]) cur = k;
				b[cur] = false;
			}
			
			a[j] = x[cur];
			cout << i << "\t" << j << "\t" << a[j] << "\n";
		}
		
		out.setf(ios::fixed);
		out.precision(6);
		out << "Case #" << i << ":";
		for (int j=0;j<q;j++) out << " " << a[j];
		out << "\n";
	}
	return 0;
}

