#include<fstream>
using namespace std;

int main(){
	ifstream fin("C-small-2-attempt0.in");
	ofstream fout("C-small-2-attempt0.out");
	int t = 0;
	fin >> t;

	long long n, k;
	for (int kk = 1; kk <= t; kk++) {
		fin >> n >> k;
		long long i = 1;
		while (i * 2 <= k) {
			i *= 2;
		}
		i--;
		long long p = (n - i) / (i + 1);
		long long r = (n - i) % (i + 1);
		if (k - i <= r) {
			p++;
		}
		fout << "Case #" << kk << ": " << int(p / 2) << ' ' << int((p - 1) / 2) << endl;
	}
	return 0;
}