#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int i=1;i<=t;i++) {
		int n,m,c;
		in >> n >> c >> m;
		vector <int> p(m),b(m);
		vector <vector <int> > a(c,vector <int>(n,0));
		vector <int> bs(c,0),ps(n,0);
		for (int j=0;j<m;j++) {
			in >> p[j] >> b[j];
			a[b[j]-1][p[j]-1]++;
			bs[b[j]-1]++;
			ps[p[j]-1]++;
		}
		int ans = max(ps[0],max(bs[0],bs[1]));
		int ans2 = 0;
		//cout << "Hello!\n";
		for (int j=0;j<n;j++) {
			if (ps[j]>ans) {
				ans2 = ps[j]-ans;
			}
		}
		out << "Case #" << i << ": " << ans << " " << ans2 << "\n";
	}
	return 0;
}

