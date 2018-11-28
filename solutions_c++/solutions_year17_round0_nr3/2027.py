#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

bool pairCompare(const pair<int, int>& firstElem, const pair<int, int>& secondElem) {
	return (firstElem.first < secondElem.first) || ((firstElem.first == secondElem.first) && (firstElem.second > secondElem.second));
}

int main() {
	ofstream fout("stall.out");
	ifstream fin("stall.in");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++) {
		long long int N, K;
		fin >> N >> K;
		long long int c1 = N;
		long long int c2 = 1;
		long long int n1 = 0;
		long long int n2 = 0;
		long long int a1 = 0;
		long long int a2 = 0;
		long long int b1 = 0;
		long long int b2 = 0;
		long long int ans = N;
		c1 = N;
		c2 = 1;
		bool carry = false;
		while (K > 0) {
			ans = c1;
			K -= c2;
			if (c1 % 2 == 0) {
				if (a1 != (c1 / 2) && a2 != 0) cout << "aerror" << endl;
				a1 = (c1 / 2);
				a2 += (c2);
				if (b1 != (c1 / 2)-1 && b2 != 0) cout << "berror" << endl;
				b1 = (c1 / 2) - 1;
				b2 += c2;
			}
			else if (c1 % 2 == 1) {
				if (carry == false) {
					if (b1 != ((c1-1)/ 2) && b2 != 0) cout << "aoerror" << endl;
					b1 = ((c1-1)/ 2);
					b2 += 2*(c2);
				}
				if (carry == true) {
					if (a1 != ((c1 - 1) / 2) && a2 != 0) cout << "aoerror" << endl;
					a1 = ((c1 - 1) / 2);
					a2 += 2*(c2);
				}
			}
			if (carry) {
				c1 = n1;
				c2 = n2;
				carry = false;
			}
			else {
				c1 = a1;
				c2 = a2;
				n1 = b1;
				n2 = b2;
				a1 = 0;
				a2 = 0;
				b1 = 0;
				b2 = 0;
				carry = true;
			}

		}
		unsigned long long int y, z;
		if (ans % 2 == 0) {
			y = (ans / 2);
			z = (ans / 2) - 1;
		} else {
			y = ((ans - 1) / 2);
			z = y;
		}
		fout << "Case #" << t + 1 << ": " << y << " " << z << endl;
	}
	system("pause");
}

