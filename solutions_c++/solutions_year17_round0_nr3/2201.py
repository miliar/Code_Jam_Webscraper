#include <fstream>
#include <string>
#include <cstring>

using namespace std;
ifstream in;
ofstream out;

int main(){
	in.open("input.txt");
	out.open("output.txt");
	int T;
	in >> T;
	for (int m = 0; m < T; ++m){
		out << "Case #" << m + 1 << ": ";
		long long N, K;
		in >> N >> K;
		long long tempN, tempK, x=1, rK, f, sum;
		tempN = N;
		tempK = K;
		while (tempK > 0){
			tempK -= x;
			x *= 2;
		}
		x /= 2;
		tempK += x;
		rK = K - tempK;
		tempN = (N - rK)/ (rK+1);
		sum = N - rK - tempN*(rK + 1);
		if (sum >= tempK) {
			out << (tempN - (tempN) / 2) << " " << ((tempN) / 2);
		}
		else out << (tempN - 1 - (tempN - 1) / 2) << " " << ((tempN - 1) / 2);
		out << "\n";
	}
	in.close();
	out.close();
	return 0;
}