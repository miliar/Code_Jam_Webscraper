#include <iostream>
#include <cmath>

using namespace std;

bool isTidy(int N[], int size) {
	for(int i = size-1; i >=0; i--) {
		if(N[i] < N[i-1]) {
			return false;
		}
	}
	return true;
}

bool intToArr(int N, int length) {
	int arr[length];
	for (int i = length-1; i >= 0; i--) {
    	arr[i] = N % 10;
    	N /= 10;
	}
	if(isTidy(arr, length) == true) {
		return true;
	}
	else return false;
}

int lastTidy(int N) {
	int length = 1;
	int div = N;
	while(div /= 10) length++;
	for(int i = N; i > 1; i--) {
		if(intToArr(i, length) == true) return i;	
	}	
}

int main() {
	int cases, N[100], results[100];
	cin >> cases;
	for(int i = 1; i <= 100; ++i) {
		cin >> N[i];
	}
	for(int i = 1; i <= cases; i++) {
		results[i] = lastTidy(N[i]);
		cout << "Case #" << i << ": " << results[i] << endl;
	}
}
