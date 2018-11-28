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
		int n,p;
		in >> n >> p;
		vector <int> g(n);
		vector <int> a(p,0);
		for (int j=0;j<n;j++) {
			in >> g[j];
			a[g[j]%p]++;
		}
		int ans(0);
		if (p == 2) {
			int z;
			
			z = a[0];
			ans += z;
			a[0] -= z;
			n -= z;
			
			z = a[1]/2;
			ans += z;
			a[1] -= z*2;
			n -= z*2;
			
			if (n>0) ans++;
		} else if (p == 3) {
			int z;
			
			z = a[0];
			ans += z;
			a[0] -= z;
			n -= z;
			
			z = min(a[1],a[2]);
			ans += z;
			a[1] -= z;
			a[2] -= z;
			n -= z*2;
			
			z = a[1]/3;
			ans += z;
			a[1] -= z*3;
			n -= z*3;
			
			z = a[2]/3;
			ans += z;
			a[2] -= z*3;
			n -= z*3;
			
			if (n>0) ans++;
		} else if (p == 4) {
			int z;
			
			z = a[0];
			ans += z;
			a[0] -= z;
			n -= z;
			
			z = min(a[1],a[3]);
			ans += z;
			a[1] -= z;
			a[3] -= z;
			n -= z*2;
			
			z = a[2]/2;
			ans += z;
			a[2] -= z*2;
			n -= z*2;
			
			z = min(a[1]/2,a[2]);
			ans += z;
			a[1] -= z*2;
			a[2] -= z;
			n -= z*3;
			
			z = min(a[3]/2,a[2]);
			ans += z;
			a[3] -= z*2;
			a[2] -= z;
			n -= z*3;
			
			z = a[1]/4;
			ans += z;
			a[1] -= z*4;
			n -= z*4;
			
			z = a[3]/4;
			ans += z;
			a[3] -= z*4;
			n -= z*4;
			
			if (n>0) ans++;
		}
		out << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}

