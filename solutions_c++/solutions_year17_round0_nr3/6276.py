#include <iostream>
#include <fstream>
#include <queue>
#define MAX_N 1000000

using namespace std;

int arr[MAX_N];
int t, n, k;
int main() {
	ofstream fout;
	fout.open("output.txt");
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n >> k;
		int cnt = 0;
		queue<int> q;
		q.push(n);
		arr[n] = 1;
		int tmp = 0;
		while (k > cnt) {
			tmp = q.front();
			q.pop();
			if (tmp % 2 == 0) {
				q.push(tmp / 2);
				arr[tmp / 2] += arr[tmp];
				q.push(tmp / 2 - 1);
				arr[tmp / 2] += arr[tmp];
			}
			else {
				q.push(tmp / 2);
				arr[tmp / 2] += arr[tmp];
				q.push(tmp / 2);
				arr[tmp / 2] += arr[tmp];
			}
			cnt += arr[tmp];
		}
		if (tmp % 2 == 0) {
			cout << "Case #" << i << ": " << arr[tmp / 2 - 1] << " " << arr[tmp / 2] << endl;
			fout << "Case #" << i << ": " << arr[tmp / 2 - 1] << " " << arr[tmp / 2] << endl;
		}
		else {
			cout << "Case #" << i << ": " << arr[tmp / 2] << " " << arr[tmp / 2] << endl;
			fout << "Case #" << i << ": " << arr[tmp / 2] << " " << arr[tmp / 2] << endl;
		}
	}


	fout.close();

	return 0;
}