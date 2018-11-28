#include <iostream>
#include <fstream>

#define ULL unsigned long long

struct result {
	ULL max;
	ULL min;
};

result getPair(ULL n, ULL k) {
	if (k==1) {
		result r;
		r.max = n/2;
		r.min = (n-1)/2;
		return r;
	}
	if (k % 2 == 0) {
		return getPair(n/2,k/2);
	}
	return getPair((n-1)/2, k/2);
	
}


int main(int argc, char **argv) {
	int t;
	std::ifstream input;
	std::ofstream output;
	
	input.open("C-large.in");
	output.open("out.txt");
	input >> t;
	for (int i = 1;i<=t;i++) {
		ULL n;
		ULL k;
		input >> n;
		input >> k;
		result res = getPair(n,k);
		output << "Case #" << i << ": " << res.max << " " << res.min << std::endl;
	
	}
    input.close();
	output.close();
	return 0;
}
