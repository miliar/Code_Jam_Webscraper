#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream file("C-large.in");
	ofstream out("output3.txt");
	long long int N, n, k;
	file >> N;
	for(int i=0; i<N; i++) {
		file >> n >> k;
		long long int cut = 0;
		long long int b = 1;
		while(cut < k)  {
			cut += b;
			b *= 2;
		}
		if(cut >= n) {
			out << "Case #" << i+1 << ": 0 0" << endl;
		}
		else {
			long long int d = (n-cut) / b;
			//cout << n << " " << cut << " " << b << endl;
			k -= b/2;
			if(k+b/2 < (n-cut)%b) {
				out << "Case #" << i+1 << ": " << d+1 << " " << d+1 << endl;				
			}
			else if(k < (n-cut)%b) {
				out << "Case #" << i+1 << ": " << d+1 << " " << d << endl;
			}
			else {
				out << "Case #" << i+1 << ": " << d << " " << d << endl;
			}

		}
	}
}