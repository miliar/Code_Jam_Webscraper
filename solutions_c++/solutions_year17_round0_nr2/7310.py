#include<iostream>
#include<string>
#include<limits>
#include<math.h>
#include<vector>

using namespace std;

int main() {
	int t;
	cin >> t;
	//int imax = numeric_limits<int>::max();
	//long long llmax = numeric_limits<long long>::max();
	//cout << "imax : " << imax << " " << " llmax : " << llmax << endl;
	//cout << (llmax - pow(10,10) ) << " " << (llmax - pow(10,18)) << " " << (llmax - pow(10,19)) << endl;

	long long n;
	for (int i = 0; i < t; i++) {
		cin >> n;
		vector<int> vi;
		while (n) {
			vi.push_back(n % 10);
			n /= 10;
		}
		int len = vi.size();
		for (int j = 1; j < len; j++) {
			if (vi[j - 1] < vi[j]) {
				vi[j]--;
				for (int y = 0; y < j; y++) {
					vi[y] = 9;
				}
			}
		}
		long long mult = 1;
		long long out_num = 0;
		for (int x = 0; x < len; x++) {
			//cout << " x : " << x << " " << vi[x] << endl;
			out_num += (vi[x] * mult);
			mult *= 10;
		}
		cout << "Case #" << (i + 1) << ": " << out_num << endl;
	}
	cin.get();
	return 0;
}