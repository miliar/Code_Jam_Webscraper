#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
int main() {
	int arr[20];
	unsigned int N;
	int T;
	scanf("%d\n", &T);
	for(int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": ";
		char ch;
		int i = 0, size, asc = 1, idx = 0, set = 0;
		while(scanf("%c", &ch) == 1) {
			if(ch == '\n') break;

			arr[i] = ch - '0';
			// cout << arr[i] ;
			if(i > 0 && arr[i] < arr[i-1] && !set) {
				asc = 0;
				idx = i - 1; //前一個!!!!!
				set = 1;
			}
			i++;
		}
		size = i;
		// cout << ":";
		// cout << ": " << idx <<  " :";
		// cout << size << endl;
		if(asc || size == 1) {
			for(int j = 0; j < size; j++)
				cout << arr[j];
			
		} else {
			int j;
			for(j = idx; j > 0 && arr[j] == arr[j-1]; j--) {
				arr[j] = 9;
			}
			// cout << "J:" << j << endl;
			arr[j] = arr[j] - 1;

			if(arr[j] != 0) j = 0;
			else j++;
			// cout << "j: " << j  << "size: " << size <<endl;
			for(; j < size; j++) {
				if(j > idx) {

					cout << "9";
				// } else if(j == idx) {

				} else
					cout << arr[j];
			}
		}
		cout << endl;
		for(int i = 0; i < 20; i++) arr[i] = 0;
	}
}