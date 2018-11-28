#include <iostream>
#include <string>

using namespace std;

static inline int obstacle(const string &num) {
	int n = num.size();
	for (int i = 1; i < n; ++i)
		if (num[i-1] > num[i])
			return i;
	return n;
}

string last(string &num) {
	int n = num.size();
	int o = obstacle(num);
	if (o == n)
		return move(num);

	for (int i = o; i < n; ++i)
		num[i] = '9';

	--num[o-1];
	for (int i = o - 2; i >= 0; --i) {
		if (num[i] <= num[i+1])
			break;
		--num[i];
		num[i+1] = '9';
	}

	if (num.front() == '0')
		num.erase(num.begin());
	return move(num);
}

int main(void) {
	cout.sync_with_stdio(false);
	int nTests;
	cin >> nTests;
	for (int t = 1; t <= nTests; ++t) {
		string num;
		cin >> num;
		cout << "Case #" << t << ": " << last(num) << endl;
	}
	return 0;
}
