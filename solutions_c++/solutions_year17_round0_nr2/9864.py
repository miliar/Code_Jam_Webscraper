#include<iostream>
#include<string>
using namespace std;

int main(){
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		long long num;
		cin >> num;
		num++;
		bool flag = false;
		while (!flag) {
			long long tmp = --num;
			int last = 10;
			flag = true;
			while (tmp) {
				if (last < tmp % 10) {
					flag = false;
					break;
				}
				else {
					last = tmp % 10;
					tmp /= 10;
				}
			}
		}
		cout << "Case #" << i <<": " << num << endl;
	}
	//system("pause");
	return 0;
}