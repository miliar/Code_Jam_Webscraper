#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int i=1;i<=t;i++) {
		double d;
		int n;
		in >> d >> n;
		vector <double> k(n),s(n),v(n);
		for (int j=0;j<n;j++) in >> k[j] >> s[j];
		for (int j=0;j<n;j++) {
			v[j] = s[j] * d / (d - k[j]);
		}
		out.setf(ios::fixed);
		out.precision(6);
		out << "Case #" << i << ": " << *min_element(v.begin(),v.end()) << "\n";
	}
	return 0;
}

