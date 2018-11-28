#include <iostream>
#include <string>
#include <sstream>
using namespace std;

typedef long long lint;

lint go(lint num) {
	lint base = 10;
	int idx = 1;
	do {
		stringstream ss; ss << num;
		string str = ss.str();
		int len = str.length();
		for (int i = len-idx-1; i >= 0; --i) {
			if (str[len-idx] < str[i]) {
				num = num - num % base -1;
				break;
			}
		}
		base *= 10;
		++idx;
	} while (num >= base);
	return num;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output2L.txt","w", stdout);
    
	int T; cin >> T;
	lint num;
	for (int c = 1; c <= T; ++c) {
		cin >> num;
		cout << "Case #" << c << ": " << go(num) << endl;
	}
}