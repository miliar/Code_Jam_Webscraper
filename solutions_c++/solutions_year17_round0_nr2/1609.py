#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#define ll unsigned long long
using namespace std;

int main() {

	std::ifstream in("C:/Users/Yoav/Jam/Qual/B-large.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("c:/Users/Yoav/Jam/Qual/outB-large.in");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		ll n;
		cin >> n;
		int i = 1;
		string s = '0' + to_string(n);
		int len = (int)s.length();
		for (; i < len - 1 && s[i-1] <= s[i]; i++);
		if (i == len - 1 && s[len - 2] <= s[len - 1])
			cout << n << endl;
		else {
			for (; s[i - 1] == s[i - 2]; i--);
			ll mod = (ll)pow(10, len - i);
			ll ans = n - (n % mod + 1);
			cout << ans << endl;
		}
	}
	return 0;
}
