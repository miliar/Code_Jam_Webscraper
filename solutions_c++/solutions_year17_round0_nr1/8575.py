#include <iostream>
#include <fstream>
#define sz size
using namespace std;

int main()
{
	freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		string str;
		cin >> str;
		int k, cnt = 0;
		cin >> k;
		for (int j = 0; j <= str.sz()-k; j++)
			if (str[j] == '-')
			{
				int tmp = 0;
				while (tmp != k)
				{
					if (str[j+tmp] == '+') str[j+tmp] = '-';
					else str[j+tmp] = '+';
					tmp++;
				}
				cnt++;
			}
		bool flag = true;
		for (int j = 0; j < str.sz(); j++)
			if (str[j] == '-') flag = false;
		cout << "Case #" << i << ": ";
		if (flag) cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}