#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

bool kiemTraTangDan(unsigned long long n) {
	while (n >= 10)
	{
		int donvi = n % 10;
		n = n / 10;
		if (donvi<n % 10)
		{
			return false;
		}
	}
	return true;
}
int main() {
	int N;

	freopen("out-put.out", "w", stdout);
	freopen("B-small-attempt2.in", "rt", stdin);
	unsigned long long temp;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> temp;
		while (kiemTraTangDan(temp) == false) {
			temp--;
		}
		cout << "Case #" << i << ": " << temp << endl;
	}
	//fclose(stdin);
	fclose(stdout);
	return 0;
}