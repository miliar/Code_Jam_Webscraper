#include<iostream>
using namespace std;
int main() {
	int count;
	cin >> count;
	for (int i = 0; i < count; i++) {
		string num;
		cin >> num;
		for (int j = 0; j < num.length() - 1; j++) {
			if (num[j] > num[j+1]) {
				num[j] = (char)((int)num[j] - 1);
				for (int k = j+1; k < num.length(); k++) {
//					cout << "Prev numk = " << num << " ";
					num[k] = '9';
//					cout << "Next = " << num << " ";
				}
				for (int k = j; k > 0; k--) {
					if (num[k] < num[k-1]) {
//						cout << "Prev numk = " << num << " ";
						num[k-1] = (char)((int)num[k-1] - 1);
						num[k] = '9';
//						cout << "Next = " << num << " ";
					}
				}
						
				break;
			}
		}
		cout << "Case #" << i+1 << ": " << stoll(num) << endl;
	}
	return 0;
}
