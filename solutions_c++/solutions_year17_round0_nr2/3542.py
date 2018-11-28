#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cfloat>
#include <iostream>
#include <algorithm>
#include <climits>
#include <set>
#include <map>
#include <iomanip>
#include <sstream>

int T;
long long N;

int isTidy(long long number) {
	int answer = 0;
	while (number > 0) {
		int onesDigit = number % 10;
		int hundredDigit = (number % 100 - onesDigit) / 10;
		if (onesDigit < hundredDigit) {
			return answer;
		}
		else {
			number -= onesDigit;
			number /= 10;
			answer++;
		}
	}
	return -1;
}

int main() {
	std::ifstream in("B-large.in");
	std::ofstream out("tidy.out");

	in >> T;
	for (int i = 0; i < T; i++) {
		in >> N;
		for (long long j = N; j >= 1; j--) {
			int tidyValue = isTidy(j);
			if (tidyValue == -1) {
				out << "Case #" << std::to_string(i+1) << ": " << std::to_string(j) << "\n";
				j = 0;
				break;
			}
			else {
				long long sizze = pow(10, tidyValue);
				j -= (j % sizze);
				
			}
		}
		
	}

}