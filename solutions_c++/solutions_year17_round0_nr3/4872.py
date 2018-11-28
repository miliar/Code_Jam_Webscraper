#include <iostream>  
#include <string>
#include <fstream>
#include <cmath>

struct Solution {
	int min;
	int max;
};



Solution solve(int n1, int k1) {
	double k = k1, n = n1;
	Solution x;
	float s = (n-k)/pow(2.0, ceil(log2(k+1) ));
	x.min = (int)floor(s);
	x.max = (int)round(s);
	return x;
}

void main() {
	int t;
	std::ofstream out;
	std::ifstream in;
	in.open("C-small-2-attempt0.in");
	out.open("out.txt");
	in >> t;
	for (int i = 0; i < t; ++i) {
		int n, k;
		in >> n >> k;
		Solution x = solve(n,k);
		out << "Case #" << i + 1 << ": " << x.max << " " << x.min << std::endl;
	}
	out.close();
	in.close();
}
