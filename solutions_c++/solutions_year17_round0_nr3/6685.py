#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#define pb push_back
#define bg begin
#define ed end
#define sz size
using namespace std;

int main()
{
	freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
	int tc;
	cin >> tc;
	for (int i = 1; i <= tc; i++)
	{
		string t = "1";
		int n;
		cin >> n;
		int k;
		cin >> k;
		vector<int> v;
		for (int j = 0; j < n; j++) t += '0';
		t += "1";
		v.pb(0);
		v.pb(n+1);
		//cout << t << endl;
		int st = 0, ed = n+1, max = 0, pos = 0, mid = 0;
		while (1)
		{
			mid = (st+ed)/2;
			max = 0;
			v.pb(mid);
			sort(v.bg(), v.ed());
			k--;
			if (k == 0) break;
			for (int j = 1; j < v.sz(); j++)
			{
				if (v[j]-v[j-1] > max)
				{
					max = v[j]-v[j-1];
					st = v[j-1];
					ed = v[j];
				}
			}
		}
		cout << "Case #" << i << ": ";
		for (int j = 0; j < v.sz(); j++) if (v[j] == mid) pos = j;
		cout << v[pos+1]-v[pos]-1 << " " << v[pos]-v[pos-1]-1 << endl;
	}
	return 0;
}