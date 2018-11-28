#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
int x[20];
int main() {
	int T;
	string N;
	int i, j, k, len, maxv;
	int kase = 0;
	bool isFirst;
	ofstream out("answer.txt");
	cin >> T;
	while (T--) {
		cin >> N;
		for (i = 0; i < N.size(); i++)
			x[i] = N[i] - '0';
		len = N.size() - 1;
		for (i = len; i >= 0; i--) {
			maxv = 0;
			for (j = 0; j < i; j++) {
				if (x[j] > maxv)
					maxv = x[j];
			}
			if (maxv > x[i]) {
				for (k = i; k <= len; k++)
					x[k] = 9;
				k = i - 1;
				while (k >= 0) {
					if (x[k] == 0) {
						x[k] = 9;
						k--;
					} else {
						x[k] -= 1;
						break;
					}
				}
			}
		}
		out << "Case #" << (++kase) << ": ";
		isFirst = true;
		for (i = 0; i <= len; i++) {
			if (x[i] != 0)
				isFirst = false;
			if (x[i] == 0 && isFirst)
				continue;
			out << x[i];
		}
		out << endl;
	}
	out.close();
	return 0;
}
