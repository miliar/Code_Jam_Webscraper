/*
B name oooo
ID: amin_un1
PROG: ride
LANG: C++

my ID
uva = "sir sbu"
codforsec = "sir_sbu"
topcoder = "sir_sbu"
usaco = "amin_un1"
*/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <cmath>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <bitset>
#include <complex>
#include <iomanip>
#include <time.h>
using namespace std;

#define ll long long
#define ld long double

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAX = 100001;
const long long mod = 1000 * 1000 * 1000 + 7;

#define mp make_pair
#define pb(a) push_back(a)
#define L(s) (int)((s).size())
#define all(c) (c).begin(), (c).end()

#define INF (1e9)
#define EPS (1e-9)
#define E (2.718281828459045)


////////////////////////////////////////////////////code///////////////////////////////////////





int main()
{
	//ofstream cout ("test.out");
	//ifstream cin ("test.in");
	freopen("BB.txt" ,"r" , stdin);
	freopen( "BBoutput.txt" , "w" , stdout );

	int test;
	cin >> test;
	int t = 0; 
	while(test -- )
	{
		string input, ans;
		cin >> input;
		t++;
		ans = input;
		bool can = false;
		for(int i = ans.length() - 1 ; i > 0 ; i--)
		{
			if(ans[i] < ans[i-1])
			{
				ans[i] = '9';
				if(ans[i-1] == '0')
				{
					int t = i - 1;
					while(ans[t] == '0')
					{
						ans[t] = '9';
						t--;
					}
					ans[t]--;
				}
				else
				{
					ans[i - 1]--;
				}
				for (int k = i; k < ans.length(); k++)
					ans[k] = '9';
			}
		}
		if (ans[0] == '0')
			ans = ans.substr(1, ans.length() - 1);
		cout << "Case #" << t << ": " << ans << endl;
		
	}
	return 0;
}

