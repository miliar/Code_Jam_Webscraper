#include <iostream>
#include<stdio.h>
#include <string>
using namespace std;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	//int n; scanf("%d", &n);
	int n; cin >> n;
	string output;
	long long min, max;

	for (int i = 1; i < n + 1;i++) {
		long long s, k;
		cin >> s >> k;
		
		while ((s != k)&&(k != 1)) {
			if ((s % 2) == 1) {
				s = s / 2;
				k = k / 2;
			}
			else if ((s % 2) == 0) {
				if ((k % 2) == 0) {
					s = s / 2;
					k = k / 2;
				}
				else if ((k % 2) == 1) {
					s = (s - 1) / 2;
					k = (k - 1) / 2;
				}
			}
			cerr << 1;
		}

		if (k == 1) {
			min = (s - 1) / 2;
			max = s / 2;
		}
		else if (s == k){
			min = 0;
			max = 0;
		}


		output = "Case #" + to_string(i) + ": " + to_string(max) + " " + to_string(min);
		cout << output << endl;
	}
}