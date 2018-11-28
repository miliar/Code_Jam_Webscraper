#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int t, cas, r, c, i, j, e;
	char cake[30][30];

	cin >> t;
	cas = 1;

	while (cas <= t) {
		cin >> r >> c;

		for (i = 0; i < r; i++)
			for (j = 0; j < c; j++)
				cin >> cake[i][j];

		for (i = 0; i < r; i++) {
			bool flag = false;
			j = 0;
			while (j < c) {
				if (cake[i][j] != '?') {
					flag = true;
					e = j-1;
					while (e >= 0 && cake[i][e] == '?') {cake[i][e] = cake[i][j]; e--;}
					e = j+1;
					while (e < c && cake[i][e] == '?') {cake[i][e] = cake[i][j]; e++;}
				}
				j++;
			}
			if (!flag) {
				if (i > 0 && cake[i-1][j] != '?')
					for (j = 0; j < c; j++)
						cake[i][j] = cake[i-1][j];
			}
		}

		for (j = 0; j < c; j++)
			if (cake[0][j] == '?') {
				i = 0;
				while (cake[i][j]=='?') i++;
				while (i>0) {cake[i-1][j] = cake[i][j]; i--;}
			}

		cout << "Case #" << cas << ":" << endl;
		for (i = 0; i < r; i++)
		{
			for (j = 0; j < c; j++)
				cout << cake[i][j];
			cout << endl;
		}
		cas++;

	}

	return 0;
}