#include<string>
#include<iostream>
#include<vector>
using namespace std;

int main() {
	int num;
	cin >> num;
	for (int i = 1; i <= num; i++) {
		string cake;
		int size;
		cin >> cake >> size;
		int flip = 0;
		vector<int> count(cake.size(), 0);
		for (int j = 0; j <= cake.size() - size; j++) {
			if (cake[j] == '+' && count[j] % 2 == 0) continue;
			if (cake[j] == '-' && count[j] % 2 == 1) continue;
			else {
				flip++;
				for (int k = 0; k < size; k++) {
					count[k + j] += 1;
				}
			}
		}
		int flag = true;
		for (int j = 0; j < cake.size(); j++) {
			if (cake[j] == '-' && count[j] % 2 == 0) {
				flag = false;
				break;
			}
			if (cake[j] == '+' && count[j] % 2 == 1) {
				flag = false;
				break;
			}
		}
		if (flag) {
			cout << "Case #" << i << ": " << flip << endl;
		}
		else {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" <<endl;
		}
	}
	return 0;
}
