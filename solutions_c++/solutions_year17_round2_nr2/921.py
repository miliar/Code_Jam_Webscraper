#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstdint>

using namespace std;

char colors[6] = {'R', 'G', 'Y', 'V', 'B', 'O'};

void solve(int n, int arr[6]){
	int stall[n];

	if(arr[0] + arr[2] + arr[4] == 0) {
		cout << "IMPOSSIBLE";
		return;
	}

	if(arr[0] != 0) {
		stall[0] = 0;
		arr[0]--;
	}
	else if(arr[2] != 0) {
		stall[0] = 2;
		arr[2]--;
	}
	else {
		stall[0] = 4;
		arr[4]--;
	}


	for(int i = 1; i < n; i++) {
		if(stall[i - 1] & 1) {
			stall[i] = stall[i - 1] - 1;
			arr[stall[i - 1] - 1]--;
		}
		else {
			if(arr[stall[i - 1] + 1] > 0) {
				stall[i] = stall[i - 1] + 1;
				arr[stall[i - 1] + 1]--;
			}
			else {
				int col1 = (stall[i - 1] + 2) % 6;
				int col2 = (stall[i - 1] + 4) % 6;
				int bonus = stall[0] == col1 ? 1 : 0;

				int x = arr[col1] + bonus - arr[col1 + 1] > arr[col2] - arr[col2 + 1] ? col1 : col2;

				stall[i] = x;
				arr[x]--;
			}
		}
		
	}

	if(stall[n - 1] == stall[0] || stall[n - 1] == (stall[0] + 3) % 6 || stall[n - 1] == (stall[0] + 5) % 6) {
		cout << "IMPOSSIBLE";
		return;
	}

	for(int i = 0; i < 6; i++) {
		if(arr[i] != 0) {
			cout << "IMPOSSIBLE";
			return;
		}
	}

	for(int i = 0; i < n; i++) {
		cout << colors[stall[i]];
	}
}

int main() {
	int t, n, arr[6];

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> n;
		// {'R', 'G', 'Y', 'V', 'B', 'O'}
		cin >> arr[0];
		cin >> arr[5];
		cin >> arr[2];
		cin >> arr[1];
		cin >> arr[4];
		cin >> arr[3];
		
		cout << "Case #" << (i + 1) << ": ";
		solve(n, arr);
		cout << endl;
	}

	return EXIT_SUCCESS;
}
