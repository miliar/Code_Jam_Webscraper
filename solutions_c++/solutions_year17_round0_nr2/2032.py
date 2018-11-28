#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <deque>
#include <string>

using namespace std;

int t,T;

#define ULL unsigned long long

void runtestcase()
{	
	string S;
	string r;
	cin >> S;
	r = S[0];
	bool f = false;
	for (ULL k = 1; k < S.size(); k++)
	{
		if (!f)
		{
			if (S[k] < S[k-1])
			{
				f = true;
				ULL l = k-1;
				if (l>0)
				{
					while (r[l] == r[l-1])
					{
						l--;
						if (l == 0)
							break;
					}
				}
				r[l]--;				
				for (l++;l<=k-1;l++)
					r[l]='9';
			}
			else
			{
				r += S[k];
			}
		}
		if (f)
		{
			r += '9';
		}		
	}
	while (r[0] == '0')
		r = r.substr(1);
	cout << r;
}

void main()
{	
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cerr << t;
		cout << "Case #" << t << ": ";
		runtestcase();
		cout << endl;
	}	
}