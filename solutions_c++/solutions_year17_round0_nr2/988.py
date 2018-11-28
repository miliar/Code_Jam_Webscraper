#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int idx; //for faster computation 

bool checktidy(long long int x) {
	int maxd = 9;
	int counter = 0;
	long long int digits = x;
	while (digits >= 10) { //last digit first
		int d = digits % 10;
		if (d > maxd) {
			idx = counter;
			return false;
		}
		digits = digits / 10;
		maxd = d;
		counter++;
	}
	if (digits > maxd){
		idx = counter;
		return false;
	}
	else return true;
}

long long int pow_ten(int x) { //compute power of 10 for int
	if (x < 1) return 1;
	long long int total = 1;
	for (int i = 0; i < x; i++) {
		total = total * 10;
	}
	return total;
}
int main() {
	int T;
	long long int N;
	ifstream infile("B-large.in");
	ofstream outfile("outlargeB.txt");

	infile >> T;
	for (int t = 0; t < T; t++) { //for every test case
		outfile << "Case #" << t + 1 << ": ";
		infile >> N;
		while(true) { //check each number backwards
			if (checktidy(N)) {
				outfile << N << "\n";
				break;
			}
//			cout << N << " " << idx << endl;
			N = N / pow_ten(idx) * pow_ten(idx) - 1;
		}
	}
	return 0;
}