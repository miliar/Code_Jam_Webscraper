#include<iostream>
#include<vector>
using namespace std;

bool isTidy(long long int inp) {
	int remainder = inp % 10;
	inp = inp / 10;
	while (inp != 0) {
		int rem = inp % 10;
		if (rem > remainder) return false;
		remainder = rem;
		inp /= 10;
	}
	return true;
}

long long int getTidy(long long int inp) {
	if (isTidy(inp)) return inp;
	else {
		inp = (inp - inp % 10 - 1) / 10;
		return getTidy(inp) * 10 + 9;
	}
}



int main() {
	int num;
	cin >> num;
	for (int i = 0; i < num; i++) {
		long long int inp;
		cin >> inp;
		inp = getTidy(inp);
		cout << "Case #" << i + 1 << ": " << inp << endl;
	}
}