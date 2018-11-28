#include <iostream>
#include <math.h>
using namespace std;

int main(){
	int test;
	cin >> test;
	for (int t = 0; t < test; ++t)
	{
		long long num;
		int digit[20] = {0};
		int digitNum = 0;
		cin >> num;

		long long tmp = num;
		while(tmp > 0) {
			digit[digitNum] = tmp % 10;
			tmp /= 10;
			digitNum++;
		}
		for (int i = 0; i < digitNum/2; ++i) {
			int tt = digit[i]; 
			digit[i] = digit[digitNum-1-i];
			digit[digitNum-1-i] = tt;
		}
		cerr << "digit number:" << digitNum << endl;

		long long ans = 0;
		long long ones = 0;
		for (int i = 0; i < digitNum; ++i)
		{
			ones += pow(10, i);
		}
		cerr << ones << endl;

		if (ones > num) {
			for (int i = 0; i < digitNum-1; ++i)
			{
				ans += 9*pow(10, i);
			}
		} else if (ones == num) {
			ans = ones;
		} else if (digitNum == 1) {
			ans = digit[0];
		} 
		else {
			int dig = 0;
			int arr[20] = {0};
			int cur = 0;
			//arr[0] = digit[0];
			// find which digit to desc
			for (int i = 0; i < digitNum-1; i++) {
				if (digit[i] <= digit[i+1]) {
					arr[i] = digit[i];
					cerr << "arr[" << i << "] = " << digit[i]<<endl;
					
					cur++;
				} else {
					arr[i] = digit[i]-1;
					break;
				}
			}
			cerr << "cur = " << cur << endl;
			while (true) {
				if (cur == digitNum-1) {
					arr[cur] = digit[cur];
					break;
				}
				if (cur == 0 || arr[cur] >= arr[cur-1]) {
					//arr[cur] = digit[cur];
					break;
				}
				cerr << cur << ": 9" << endl;
				arr[cur] = 9;
				arr[cur-1] = arr[cur-1] - 1; 
				cur = cur - 1;
			}
			cout << "Case #" << t+1 << ": ";
			for (int i = 0; i < digitNum; ++i) {
				if (i < digitNum-2 && arr[i] == 0) {
					continue;
				}
				if (arr[i] > 0 || i == 0) {
					cout << arr[i];
				}else {
					cout << 9;
				}
			}
			cout << endl;
			ans = -1;
		}
		if (ans >= 0)
		cout << "Case #" << t+1 << ": " << ans << endl;

	}
}