#include <iostream>

using namespace std;

bool is_tidy (int n) {
	int cur = 10;
	while (n>0) {
		int c = n%10;
		if (c>cur)
			return false;
		n/=10;
		cur = c;
	}
	return true;
}

void solve (int num) {
	int n;

	cin >> n;

	while (!is_tidy(n))
		n--;

	cout << "Case #" << num << ": " << n << endl;
}

int main () {
	int N;
	cin >> N;

	for (int i=0; i<N; i++)
		solve(i+1);

	return 0;
}