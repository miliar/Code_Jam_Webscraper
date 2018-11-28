#include <iostream>
#include <fstream>
using namespace std;
int digits_num(int num) {
	int counter = 0;
	while (num >= 1)
	{
		num /= 10;
		counter++;
	}
	return counter;
}
int get_digit(int num, int position) {
	int n = digits_num(num);
	for (int i = 0; i < (n - (position + 1)); i++) {
		num /= 10;
	}
	return num % 10;
}
bool check(int x) {
	int n = digits_num(x);
	for (int i = 0; i < n - 1; i++) {
		if (get_digit(x, i) > get_digit(x, i + 1)) return false;
	}
	return true;
}
int main() { 
	fstream File;
	File.open("test.txt", ios::out);
	int T, num;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> num;
		while (!check(num)) {
			num--;
		}
		File << "Case #" << i << ": " << num << endl;
	}
	
	File.close();
	system("pause");
	return 0;
}


