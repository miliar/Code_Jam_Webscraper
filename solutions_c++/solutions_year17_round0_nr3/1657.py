#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#define ll unsigned long long
using namespace std;

int main() {

	std::ifstream in("C:/Users/Yoav/Jam/Qual/C-large.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("c:/Users/Yoav/Jam/Qual/outC-large.in");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		ll n, k;
		cin >> n >> k;
		while (k > 1) {
			if (k % 2 == 0 || n % 2 == 1) 
				n /= 2;
			else 
				n = n / 2 - 1;
			k /= 2;
		}
		if (n % 2) cout << n / 2 << " " << n / 2;
		else cout << n / 2 << " " << n / 2 - 1;
		cout << endl;
	}
	return 0;
}