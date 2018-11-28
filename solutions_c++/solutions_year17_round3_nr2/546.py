#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;
class sgm {
public:
	int c,d;
	int f;
public:
	sgm(int cc=0, int dd=0, int ff=0) {
		c = cc;
		d = dd;
		f = ff;
	}
};
bool cmp(sgm p,sgm q) {
	return (p.c < q.c);
}
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int i=1;i<=t;i++) {
		int ac,aj;
		in >> ac >> aj;
		vector <int> cc(ac),dc(ac),cj(aj),dj(aj);
		for (int j=0;j<ac;j++) in >> cc[j] >> dc[j];
		for (int j=0;j<aj;j++) in >> cj[j] >> dj[j];
		vector <sgm> e;
		for (int j=0;j<ac;j++) e.push_back(sgm(cc[j], dc[j], 0));
		for (int j=0;j<aj;j++) e.push_back(sgm(cj[j], dj[j], 1));
		vector <int> w(2,0);
		for (int j=0;j<ac;j++) w[0] += dc[j] - cc[j];
		for (int j=0;j<aj;j++) w[1] += dj[j] - cj[j];
		
		sort(e.begin(),e.end(),cmp);
		int n = ac+aj;
		int g = n;
		vector <int> len(n,0),lf(n,-1);
		for (int j=0;j<n;j++) {
			if (e[j].f == e[(j+1)%n].f) {
				len[j] = (e[(j+1)%n].c+1440 - e[j].d)%1440;
				lf[j] = e[j].f;
				g++;
			}
		}
		
		vector <vector <int> > h(2,vector <int>(0));
		for (int j=0;j<n;j++) {
			if (lf[j] != -1) {
				h[lf[j]].push_back(len[j]);
			}
		}
		for (int j=0;j<2;j++) sort(h[j].begin(),h[j].end());
		
		for (int j=0;j<2;j++) {
			for (int k=0;k<(int)(h[j].size());k++) {
				//cout << j << "\t" << k << "\t" << h[j][k] << "\t" << w[j] << "\n";
				if (h[j][k] + w[j] <= 720) {
					g -= 2;
					w[j] += h[j][k];
				}
			}
		}
		
		out << "Case #" << i << ": " << g << "\n";
	}
	return 0;
}

