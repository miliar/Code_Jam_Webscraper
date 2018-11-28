#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

void oneRun(){
	long long N;
	cin >> N;
	int digits = (int)log10(N)+1;
	int A[digits+1];
	for(int i=0; i<digits; i++) {
		A[i] = N % 10;
		N /= 10;
	}
	int previous = 9;
	for(int i=0; i < digits; i++) {
		if(A[i] > previous) {
			A[i]--;
			for(int j=(i-1); j >= 0; j--) {
				A[j] = 9;
			}
		}
		previous = A[i];
	}
	for(int i=(digits-1); i >= 0; i--) {
		if(i==(digits-1) && A[i]==0) continue;
		cout << A[i];
	}
}

int main(){
	int nums;
	cin >> nums;
	for(int i=1; i <= nums; i++) {
		cout << "Case #" << i << ": ";
		oneRun();
		cout << endl;
	}
	return 0;
}