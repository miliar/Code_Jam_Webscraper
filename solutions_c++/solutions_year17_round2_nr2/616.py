#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define f(i,x,y) for(int i = x; i < y; ++ i)
typedef long long ll;

int a,b,c,ab,ac,bc;

int main()
{
	int number_of_testcases;
	cin >> number_of_testcases;
	for (int testcase = 1; testcase <= number_of_testcases; ++ testcase)
	{
		cout << "Case #" << testcase << ": ";
		int n;
		cin >> n >> a >> ab >> b >> bc >> c >> ac; // ROYGBV
		string s(n, 'z');

		if (ab + ac + bc == 0)
		{
			if (a*2 == n)
			{
				f(i, 0, a) s[i*2] = 'R';
				f(i, 0, b) s[i*2+1] = 'Y';
				f(i, 0, c) s[i*2+b*2+1] = 'B';
				cout << s << endl;
			}
			else if (b*2 == n)
			{
				f(i, 0, b) s[i*2] = 'Y';
				f(i, 0, a) s[i*2 + 1] = 'R';
				f(i, 0, c) s[i*2 + a*2 + 1] = 'B';
				cout << s << endl;
			}
			else if (c*2 == n)
			{
				f(i, 0, c) s[i*2] = 'B';
				f(i, 0, a) s[i*2 + 1] = 'R';
				f(i, 0, b) s[i*2 + a*2 + 1] = 'Y';
				cout << s << endl;
			}
			else if (a*2 > n || b*2 > n || c*2 > n)
			{
				cout << "IMPOSSIBLE" << endl;
			}
			else
			{
				f(i, 0, a) s[i*2] = 'R';
				int pos = n - 1;
				f(i, 0, b)
				{
					if (s[pos] == 'R') s[--pos] = 'Y';
					else s[pos] = 'Y';
					pos -= 2;
				}
				f(i, 0, n) if (s[i] == 'z') s[i] = 'B';
				cout << s << endl;
			}
		}
		if (s[0] != 'z')
		f(i, 0, s.size()-1) if (s[i] == s[i+1]) cerr << endl << testcase << endl;
	}
}

