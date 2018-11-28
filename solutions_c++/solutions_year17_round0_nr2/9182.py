#include<iostream>
#include<string>
#include<algorithm>

#define fre freopen("0.in","r",stdin),freopen("0.out","w",stdout)
using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int t, n, i, s,flag=0,test=0;
	string sn;
	cin >> t;
	bool sorted;
	while (t--)
	{
		test++;
		cin >> n;
		for (int i = n; i >= 0; i--)
		{
			sn = to_string(i);
			s= sn.length();
			sorted = is_sorted(sn.begin(), sn.end());
			if (sorted && sn[s - 1] != '0')
			{
				cout << "Case #" << test << ": " << i << "\n";
				break;
			}
			else
			{
				continue;
			}
		}
	}
}
