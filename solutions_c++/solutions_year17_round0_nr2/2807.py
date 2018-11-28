#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
using namespace std;

int T;
long long n;

int main() {	
	cin >> T;
	for (int cse = 1; cse <= T; cse++) {
		cin >> n;
		vector<int> digit;
		while (n) {
			digit.push_back(n % 10);
			n /= 10;
		}
		digit.push_back(0);
		for (int i = digit.size() - 2; i >= 0; i--) {
			if (digit[i] < digit[i + 1]) {
				int x = i + 1;
				while (x < digit.size() && digit[x] == digit[i + 1])
					x++;
				digit[x - 1]--;
				for (int j = x - 2; j >= 0; j--)
					digit[j] = 9;
				break;
			}
		}
		cout << "Case #" << cse << ": ";
		while (digit.back() == 0) digit.pop_back();
		for (int i = digit.size() - 1; i >= 0; i--)
			cout << digit[i];
		cout << endl;
	}
	return 0;
}

