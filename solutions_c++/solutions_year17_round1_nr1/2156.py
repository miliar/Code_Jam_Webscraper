#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	int r,c;
	in >> t;
	for(int i=1;i<=t;i++) {
		in >> r >> c;
		vector <string> a(r),b;
		for (int j=0;j<r;j++) {
			in >> a[j];
		}
		b = a;
		for (int j=0;j<r;j++) {
			for (int k=0;k<c;k++) {
				if (b[j][k] != '?') {
					for (int l=0;l<k;l++) {
						b[j][l] = b[j][k];
					}
					break;
				}
			}
			for (int k=1;k<c;k++) {
				if (b[j][k] == '?') {
					b[j][k] = b[j][k-1];
				}
			}
		}
		for (int j=0;j<r;j++) {
			if (b[j][0] != '?') {
				for (int m=0;m<j;m++) for (int k=0;k<c;k++) {
					b[m][k] = b[j][k];
				}
				break;
			}
		}
		for (int j=1;j<r;j++) {
			if (b[j][0] == '?') {
				for (int k=0;k<c;k++) {
					b[j][k] = b[j-1][k];
				}
			}
		}
		
		out << "Case #" << i << ":\n";
		for (int j=0;j<r;j++) {
			out << b[j] << "\n";
		}
	}
	return 0;
}

