#include <iostream>
#include <vector>
#include <string>
#include <bitset>
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
		int k;
		cin >> k;
		bitset<1000> bs;
		bs.flip();
		int ov = 0;
		for (int i = 0; i < a.size(); i++)
		{
			bs[i] = a[i] == '+';
		}
		for (int i = 0; i < a.size()-k+1; i++)
		{
			if (bs[i])
			{
				continue;
			}
			ov++;
			for (int j = 0; j < k; j++)
			{
				bs.flip(i + j);
			}

		}
		//cout << bs.count() << endl;
		if (bs.count()==1000)
		{
			cout << "Case #" << q + 1 << ": " << ov << "\n";
		}
		else {
			cout << "Case #" << q + 1 << ": " << "IMPOSSIBLE" << "\n";

		}
	}
	
	return 0;
}

