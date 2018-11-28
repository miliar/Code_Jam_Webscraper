#include <bits/stdc++.h>
using namespace std;

long long int t, n, k, a, q, r;

int main()
{
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		a = 1;
		cin >> n >> k;
		while (a*2 <= k) a*=2;
		q = (n-a+1)/a;
		r = (n+1)%a;
		//cout << "a:" << a << " q:" << q << " r:" << r << endl;
		if (q%2==1)
		{
			if (k < a+r) cout << "Case #" << i+1 << ": " << (q+1)/2 << " " << (q-1)/2 << endl;
			else cout << "Case #" << i+1 << ": " << (q-1)/2 << " " << (q-1)/2 << endl;
		}
		if (q%2==0)
		{
			if (k < a+r) cout << "Case #" << i+1 << ": " << q/2 << " " << q/2 << endl;
			else cout << "Case #" << i+1 << ": " << q/2 << " " << (q/2)-1 << endl;
		}
	}
}