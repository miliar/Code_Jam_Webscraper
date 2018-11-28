#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;

long long int lastStall(long long int n, long long int k) {
	long long int people = pow(2,floor(log(k)/log(2)));
	long long int stalls = n - people + 1;
	long long int minMax = ceil(stalls * 1.0 / people);
	long long int maxMax = floor(stalls * 1.0 / people);
	long long int onlyStall = stalls - maxMax * people;
	long long int allOnly = k - people + 1;

	if (allOnly > onlyStall){
		return maxMax;
	}
	
	return minMax;
}

int main() {
    ifstream infile("C-small-2-attempt0.in");
    ofstream outfile("C-small-2-attempt0.out");
    long long int t, n, k, min, max;
    infile >> t;
    for (int i = 0; i < t; i++) {
        infile >> n;
        infile >> k;
        
        outfile << "Case #" <<  i+1 <<": ";

		long long int stall = lastStall(n, k);
		
		if (stall < 1) {
			min = 0;
			max = 0;
		}
		else {
			min = ceil((stall - 1) / 2.0);
			max = floor((stall - 1) / 2.0);
		}

		outfile << min << " " << max << endl;
    }

    return 0;
}
