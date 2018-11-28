#include <iostream>
#include <fstream>

using namespace std;

long long n;
int t;
bool is_acd(long long n);

int main()
{
	int t;   cin >> t;

	ofstream fout;
	fout.open("output.txt");
	for(int i = 1; i <= t; i++) {
		cin >> n;
		while (!is_acd(n)) {
			n--;
		}
		cout << "Case #" << i << ": " << n << endl;
		fout << "Case #" << i << ": " << n << endl;

	}	
	fout.close();

	return 0;
}


bool is_acd(long long n) {
	long long pre = n % 10;
	while (n != 0) {
		n /= 10;
		int tmp = n % 10;
		if (tmp > pre) return false;
		pre = tmp;
	}

	return true;
}