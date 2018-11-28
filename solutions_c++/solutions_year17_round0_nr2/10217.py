#include <iostream>

using namespace std;

#include <string>

bool isTidy(unsigned long long numero) {
	int digito = 0, digitoAnterior = 0;
	digito = numero % 10;
	numero /= 10;
	while (numero != 0) {
		digitoAnterior = digito;
		digito = numero % 10;
		numero /= 10;
		if (digito > digitoAnterior) {
			return false;
		}
	}
	return true;
}

void handleCase(unsigned long long numero, const int counter = 0) {
	for (int unsigned long long i = numero; true; i--) {
		if (isTidy(i)) {
			cout << i << endl;
			return;
		}
	}
}

int main() {
	int testCases;
	unsigned long long num;
	cin >> testCases;
	for (int i = 1; i <= testCases; ++i) {
		cin >> num;
		cout << "Case #" << i << ": ";
		handleCase(num);
	}
	return 0;
}