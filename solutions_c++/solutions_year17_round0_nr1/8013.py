#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;
int main() {
	ifstream file("A-large.in");
	ofstream out("output.txt");
	int n;
	file >> n;
	for (int i = 1; i <= n; i++) {
		string tmp;
		int k;
		file >> tmp;
		file >> k;
		vector<int> res;
		int count = 0;
		for (int j = 0; j < tmp.length(); j++) {
			if (tmp[j] == '+') {
				res.push_back(1);
			}
			else {
				res.push_back(-1);
			}
		}
		for (int j = 0; j < res.size() - k; j++) {
			if (res[j] == -1) {
				count++;
				for (int m = j; m < j + k; m++) {
					res[m] *= -1;
				}
			}
		}
		bool flag = true;
		int cur = res[res.size() - k];
		for (int j = res.size() - k; j < res.size(); j++) {
			if (cur != res[j]) {
				flag = false;
			}
		}
		if (flag)
			out << "Case #" << i << ": " << (cur == -1 ? count + 1 : count) << endl;
		else 
			out << "Case #" << i << ": IMPOSSIBLE"<< endl;
	}
	return 0;
}