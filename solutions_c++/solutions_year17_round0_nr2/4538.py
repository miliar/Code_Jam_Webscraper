#include <iostream>
#include <vector>
#include <string>
#define ll long long int
using namespace std;


int main()
{
	iostream::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		string a;
		cin >> a;
		a.reserve();
		vector<int> liczba;
		for (int i = 0; i < a.size(); i++)
		{
			liczba.push_back((int)a[i] - (int)'0');
		}
		for (int p = 0; p < 20; p++)
		{


			int last = 0;
			for (int i = 0; i < liczba.size(); i++)
			{
				if (liczba[i] < last) {
					liczba[i - 1]--;
					for (int j = i; j < liczba.size(); j++)
					{
						liczba[j] = 9;
					}
					break;
				}
				last = liczba[i];
			}
		}
		cout << "Case #" << q + 1 << ": ";
		for (int i = 0; i < liczba.size(); i++)
		{
			if (i == 0 && liczba[0] == 0) {
				continue;
			}
			cout << liczba[i];
		}
		cout << "\n";
	}
	return 0;
}

