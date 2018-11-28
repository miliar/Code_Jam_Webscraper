#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(){
	int t;
	cin >> t;
	
	for (int times = 1; times <= t; times++){
		int n,k;
		cin >> n >> k;
		long long curp = 1;
		int depth = 0;
		while (curp < k){
			curp += 1;
			curp *= 2;
			curp -= 1;
			depth++;
		}
		long long left = k - (pow(2.0,depth)-1);
		long long sum = n - (pow(2.0,depth)-1);
		long long inThisDepth = pow(2.0,depth);
		long long numlarger = sum%inThisDepth;
		long long smaller = sum/inThisDepth;
		long long larger = smaller +1;
		long long best;
		if (left <= numlarger)
			best = larger;
		else
			best = smaller;
		cout << "Case #" << times << ": " << best/2 << " " << (best-1)/2 << endl;
	}
	return 0;
}