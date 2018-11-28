#include <stack>
#include <vector>
#include <list>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main() {
	ofstream fout("cordon.out");
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string inp;
		int k;
		cin >> inp >> k;
		int n_min = 0;
		for (int j = 0; j < int(inp.size()); j++) {
			if (inp[j] == '-')
				n_min++;
		}
		if (n_min == 0) {
			fout << "Case #" << i + 1 << ": 0" << "\n";
		}
		else {
			int res = 0;
			for (int j = 0; j < int(inp.size()) - k + 1; j++) {
				if (inp[j] == '-') {
					for (int l = j; l < j + k; l++) {
						if (inp[l] == '-')
							inp[l] = '+';
						else
							inp[l] = '-';
					}
					res++;
				}
			}
			bool flag = 0;
			for (int j = 0; j < int(inp.size()); j++) {
				if (inp[j] == '-') {
					fout << "Case #" << i + 1 << ": IMPOSSIBLE" << "\n";
					flag = 1;
					break;
				}
			}
			if (!flag)
				fout << "Case #" << i + 1 << ": " << res << "\n";
		}
	}
	return 0;
}