#include <iostream>
#define ll long long
using namespace std;

int main()
{
	freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		ll n;
		cin >> n;
		while (1)
		{
			int a[20], j = 0;
			ll tmp = n;
			while (tmp)
			{
				a[j] = tmp%10;
				tmp /= 10;
				j++;
			}
			bool flag = true;
			for (int k = 0; k < j-1; k++)
				if (a[k] < a[k+1]) flag = false;
			if (flag) break;
			else n--;
		}
		cout << "Case #" << i << ": " << n << endl;
	}
	return 0;
}