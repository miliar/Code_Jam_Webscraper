#include <fstream>
#include <math.h>
#include <string>

std::ifstream cin("input.in");
std::ofstream cout("output.txt");


std::string lastTidy(std::string x) {

	int i = x.size() - 1;
	while (i > 0) {
		if (x[i] < x[i - 1]) {

			for(int k = i; k < x.size();k++) 
				x[k] = '9';

			int j = i - 1;
			while (j >= 0 && --x[j] == '/') {
				x[j] = '9';
				j--;
			}
		}
		i--;
	}
	
	return x;
}
int main() {

	long long int numCases; cin >> numCases;

	for (long long int i = 0; i < numCases; i++) {

		std::string x;

		cin >> x;

		x = lastTidy(x);
		if (x[0] == '0') x.erase(0,1);

		cout << "Case #" << i +1<< ": " << x << "\n";

	}

	return 0;
}