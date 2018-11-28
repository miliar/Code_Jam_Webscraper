#include <fstream>
#include <string>
#include <math.h>
#include <stdint.h>
using namespace std;

void getDist(long long n, long long k, long long& minL, long long& maxL){
	long long n_l = 1;
	long long n_s = 0;

	long long cnt = 0;
	long long x = n;

	while (true){
		if (cnt + n_l >= k){
			maxL = x/2;
			minL = (x % 2 == 0) ? (x/2-1) : (x/2);
			return;
		}
		cnt += n_l;
		if (cnt + n_s >= k){
			maxL = (x % 2 == 0)? (x / 2 - 1):( x/ 2);
			minL = x / 2 - 1;
			return;
		}
		cnt += n_s;
		if (x % 2 == 0){
			n_s = 2 * n_s + n_l;
		}
		else{
			n_l = 2 * n_l + n_s;
		}
		x /= 2;
	}
}

int main(int argc, char** args){
	ifstream in_file("input.txt");
	ofstream out_file("output.txt");

	int T;
	in_file >> T;
	long long number;
	long long K;
	for (int t = 0; t < T; ++t){
		in_file >> number >> K;
		long long maxl, minl;
		getDist(number, K, minl, maxl);

		out_file << "Case #" << t + 1 << ": " << maxl <<" "<< minl << std::endl;
	}
	getchar();
	return 0;
}