#include <cstdio>
#include <string>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void) {
	int T, N, j = 1;
	cin >> T;

	while(T--) {
		cin >> N;
		for(int i = N; i >= 0; i--) {
			string num = to_string(i);
			sort(num.begin(), num.end());
			if(to_string(i) == num) {
			    cout << "Case #" << j << ": ";
				cout << num << endl;
				j++;
				break;
			}
		}	
	}

	return 0;
}