#pragma warning(disable: 4996)
#include <stdio.h>
#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
#include <math.h>
#include <unordered_set>
using namespace std;



/*2017 04 08*/

#define CURRENT A
#define  A 0 // Oversized Pancake Flipper
#define  B 1 // Tidy Numbers
#define  C 2 //
#define  D 3 //
#define  E 4 //
#define  F 5 //
#define  G 6 //



//Oversized Pancake Flipper
#if (CURRENT == A)

char buf[1010];
int flip;
int ans;
int len;

bool dg(int idx)
{
	if ( idx>=len)
	{
		return true;
	}

	if (buf[idx]=='+')
	{
		while (buf[idx] == '+')
			idx++;
		return dg(idx);
	}
	else
	{
		if (idx>(len-flip))
		{
			return false;
		}

		for (size_t i = 0; i < flip; i++)
		{
			buf[i + idx] ^= 6;
		}
		ans++;
		return dg(idx+1);

	}

}

int solve()
{

	int idx = 0;
	len = strlen(buf);
	ans = 0;
	if (dg(0))
	{
		return ans;
	}
	else
	return -1;

}

int main(void)
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("As.out", "w", stdout);
		freopen("A-large.in", "r", stdin);
		freopen("AL.out", "w", stdout);
	int nTest;

	//scanf("%d", &nTest);
	cin >> nTest;
	for (int i = 1; i <= nTest; i++)
	{
		cin >> buf >> flip;

		int res = solve();
		cout << "Case #" << i << ": ";
		if (res == -1)	cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}

	return 1;
}
#endif




#if ( CURRENT == B )

char n[30];

bool isTidy()
{
	int idx = 1;
	int len = strlen(n);
	if (len == 1) true;
	while (idx<len)
	{
		if (n[idx]<n[idx - 1])
		{
			return false;
		}
		idx++;
	}
	return true;
}

void solve()
{
	int idx = 1;
	int len = strlen(n);

//	if (len == 1) return;


	bool found = false;
	while (idx<len)
	{
		if (n[idx]<n[idx-1])
		{
			found = true;
			break;
		}
		idx++;
	}

	if (found)
	{
		int i = len - 1;
		while (i>=idx)
		{
			n[i] = '9'; i--;
		}
		idx--;
		while (idx>=0)
		{
			if (n[idx]>'0')
			{
				n[idx]--;
				break;
			}
			else
			{
				n[idx] = '9';
				idx--;
			}
		}

		if (n[0]=='0')
		{
			for (size_t j = 1; j <= len; j++)
			{
				n[j - 1] = n[j];
			}
		}
	}
}


int main(void)
{
//	freopen("B-small-attempt0.in", "r", stdin);
	//freopen("Bs.out", "w", stdout);
		freopen("B-large.in", "r", stdin);
		freopen("BL.out", "w", stdout);
	int nTest;

	//scanf("%d", &nTest);
	cin >> nTest;
	for (int i = 1; i <= nTest; i++)
	{
		cin >> n;
		while (!isTidy())
			solve();
		cout << "Case #" << i << ": ";
		cout << n << endl;
	}

	return 1;
}
#endif

#if ( CURRENT ==C )



#endif

#if ( CURRENT ==D )



#endif
