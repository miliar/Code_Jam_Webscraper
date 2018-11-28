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

char a[7] = "ROYGBV";
	

int maxind(int *b, char f)
{
	int u = 0;
	if (a[u] == f)
		u++;
	for (int m=1; m<6; m++)
		if (a[m] != f && b[m] > b[u])
			u = m;
	return u;
}

int idx(char f)
{
	for (int m=0; m<6;m++)
		if (a[m]==f)
			return m;
}

void runtestcase()
{	
	int N, b[6];
	cin >> N >> b[0] >> b[1] >> b[2] >> b[3] >> b[4] >> b[5];
	char r[1001];
	
	int w = maxind(b, 'X');
	r[0] = a[w];
	b[w]--;

	int i = 1;
	int j = N-1;
	while (i<=j)
	{
		if (r[i-1] == r[(j+1) % N ])
		{
			int wi = maxind(b, r[i-1]);
			if (b[wi]==0)
			{
				cout << "IMPOSSIBLE";
				return;
			}
			b[wi]--;
			r[i]=a[wi];
			i++;
		}
		else
		{
			int w = maxind(b, 'X');
			int wi = idx(r[(j+1) % N]);
			if (b[wi] == b[w])			
			{
				b[wi]--;
				r[i]=a[wi];
				i++;
			}
			else
			{
				int wj = idx(r[i]);
				if (b[wj] == b[w])
				{
					b[wj]--;
					r[j] = a[wj];
					j--;
				}
				else
				{
					b[w]--;
					r[i] = a[w];
					i++;
				}
			}
			if (r[i] == r[i-1] || r[j] == r[(j+1) % N])
			{
				cout << "IMPOSSIBLE";
				return;
			}
		}		
	}
	r[N] = '\0';
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