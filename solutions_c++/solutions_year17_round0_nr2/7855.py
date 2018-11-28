#include <iostream>
#include <string>

using namespace std;
bool check(int num) {
	string s = to_string(num);
	int size = s.size();
	for (int i = 0; i < size-1; i++) {
		if (s[i] > s[i+1]) {
			return false;
		}
	}
	return true;
}
int getNum (int n) {
	for (int i = n; i > 0; i--) {
		if (check(i))
			return i;
	}
	return 1;
}
int main(int argc, char *argv[]) {
	int t, n;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n;
		cout << "Case #" << i << ": " << getNum(n) << endl;
	}
}