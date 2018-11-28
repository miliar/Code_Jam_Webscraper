#include<bits/stdc++.h>
using namespace std;
# define ll long long
# define mod 1000000007
# define MAX 200011
char flipBit(char ch)
{
	return ch == '+' ? '-' : '+';
}
int main()
{
	ifstream cin("file/a.txt");
	ofstream cout("file/b.txt");
	cin.sync_with_stdio(false);
	int t, k, n, i, var = 0, j;
	cin >> t;
	while (t--)
	{
		var++;
		cout << "Case #" << var << ": ";
		string str;
		cin >> str;
		n = str.size();
		if (n == 1) {
			cout << str << '\n';
			continue;
		}
		int ar[20];
		for (i = 0; i < n; i++)
			ar[i + 1] = str[i] - '0';
		bool con1 = false,con2=false;
		for (i = 1; i < n; i++)
			if (ar[i] > ar[i + 1]) {
				con1 = true;
				j = i;
				if (j == 1) {
					con2 = true;
					break;
				}
				while (true) {
					if (j == 0)
					{
						j--;
						break;
					}
					if (ar[j] < ar[i])
						break;
					j--;
				}
				break;
			}
		if (con2) {
			if (ar[1] > 1)
				cout << ar[1] - 1;
			n--;
			while (n--)
				cout << 9;
			cout << '\n';
		}
		else if (!con1)
			cout << str << '\n';
		else {
			if (j == 0) {
				n--;
				while (n--)
					cout << 9;
				cout << '\n';
			}
			else {
				j++;
				for (i = 1; i <= n; i++) {
					if (i == j)
						cout << ar[i] - 1;
					else if (i < j)
						cout << ar[i];
					else
						cout << 9;
				}
				cout << '\n';
			}
		}
	}
	return 0;
}