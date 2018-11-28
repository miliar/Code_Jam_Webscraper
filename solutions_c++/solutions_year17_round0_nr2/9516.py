#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	ifstream f("B-small-attempt0.in");
	ofstream f2("out.txt");
	int t;
	f >> t;
	int T = t;
	while(t--)
	{
		int n;
		f >> n;
		for(int i = n; i >= 0; --i)
		{
			int d = i%10;
			int temp = i;
			while(temp > 0)
			{
				temp /= 10;
				int d2 = temp%10;
				if(d2 > d)
					break;
				d = d2;
			}
			if(temp == 0)
			{
				f2 << "Case #" << T-t << ": " << i << endl;
				break;
			}
		}
	}
	f.close();
	f2.close();
}