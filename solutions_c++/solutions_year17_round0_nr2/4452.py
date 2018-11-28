#include <iostream>
#include <vector>
#include <algorithm>
typedef long long int ll;
using namespace std;

ll n,t;
vector<int> d,r;

int main()
{
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		ll m;
		cin >> n;
		cout << "Case #" << i << ": ";
		m = n;

		d.clear();
		r.clear();
		while (n>0)
		{
			d.push_back(n%10);
			n /= 10;
		}

		reverse(d.begin(), d.end());

		int j = 0;
		while (j < d.size()-1)
		{
			if (d[j]>d[j+1])
			{
				break;
			}
			else
			{
				j++;
			}
		}

		if (j<d.size()-1)
		{
			int l = j-1;

			while (l >= 0)
			{
				if (d[l]<d[l+1])
				{
					break;
				}
				else
				{
					l--;
				}
			}

			if (l<0)
			{
				if (d[0]>1) r.push_back(d[0]-1);
				for (int k = 1; k < d.size(); ++k)
				{
					r.push_back(9);
				}
			}
			else
			{
				for (int k = 0; k <= l; ++k)
				{
					r.push_back(d[k]);
				}
				r.push_back(d[l+1]-1);
				for (int k = l+2; k < d.size(); ++k)
				{
					r.push_back(9);
				}
			}

			for (int k = 0; k < r.size(); ++k)
			{
				cout << r[k];
			}

			cout << endl;
		}
		else
		{
			cout << m << endl;
		}
	}
}