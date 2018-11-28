#include <iostream>

using namespace std;

int main()
{
    int c;
	cin >> c;

	int tidy[1001] = {0};
	for (int i = 1; i < 10; i++) {
		tidy[i] = i;
		for (int j = 0; j < 10; j++) {
			int tmp = i * 10 + j;
			if (i <= j) tidy[tmp] = tmp;
			else tidy[tmp] = 0;
		}
	}

	for (int i = 1; i < 10; i++) {
		for (int j = 0; j < 100; j++) {
			int tmp = i * 100 + j;
			if (i * 10 <= j && tidy[j] != 0) tidy[tmp] = tmp;
			else tidy[tmp] = 0;
		}
	}

	//for (int i = 0; i < 1000; i++) cout << tidy[i] << " ; ";

	for (int cases = 1; cases <= c; cases++) {
		int n;
		cin >> n;

		if (tidy[n] != 0) cout << "Case #" << cases << ": " << n << endl;
		else {
			while (tidy[n] == 0) n -= 1;
			cout << "Case #" << cases << ": " << n << endl;
		}
	}
    return 0;
}
