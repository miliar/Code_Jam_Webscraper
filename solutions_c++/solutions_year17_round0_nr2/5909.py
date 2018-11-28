#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int t;
int arr[20];
int len;
string s;
void init() {
	s = "";
	len = 0;
	for (int i = 0; i < 20; i++) {
		arr[i] = 0;
	}
}
int main() {
	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		init();
		cin >> s;
		len = s.length();
		for (int i = 0; i < len; i++) {
			arr[i] = s[i] - '0';
		}
		int prv = arr[0];
		for (int i = 1; i < len; i++) {
			if (arr[i] < prv) {//이전 값보다 작으면
				arr[i] = 9;
				arr[i - 1] = arr[i - 1] - 1;
				prv = prv - 1;
				for (int g = i - 2; g >= 0; g--) {
					if (arr[g] > prv) {
						arr[g + 1] = 9;
						arr[g] = arr[g] - 1;
						prv = arr[g];
					}
					else {
						break;
					}
				}
				for (int k = i + 1; k < len; k++) {
					arr[k] = 9;
				}
				break;
			}
			else {
				prv = arr[i];
			}
		}
		bool flag = false;
		cout << "Case #" << test << ": ";
		for (int i = 0; i < len; i++) {
			if (arr[i] > 0) {
				flag = true;
			}
			if (flag) {
				cout << arr[i];
			}
		}
		cout << endl;
	}
	return 0;
}