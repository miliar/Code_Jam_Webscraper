#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <list>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <map>
#include <set>
#include <sstream>
using namespace std;
typedef signed long long int lli;
typedef vector<int> vi;
#define FOR(i, p, n) for(int i(p); i < n; i++)
#define FORR(i,p) for( i(p); i>=0; i--)
#define ALL(a) (a.begin()),(a.end())
#define sqr(x) ((x)*(x))
#define sqrt(x) sqrt(1.0*(x))
#define pow(x,n) pow(1.0*(x),n)
#define FORI(n) for(int i=0;i<n;i++)
#define sz(V) (int)V.size()
#define pb push_back
#define UN(x) (x).resize(unique(ALL((x))) - (x).begin());
#define mp make_pair
const int INF = 1000000000;
bool solve()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int cs(0); cs < t; cs++)
	{
		string t;
		cin >> t;
		
		for (int i(t.size() - 1); i >= 0; i--)
		{
			if (i)
			{
				if (t[i] < t[i - 1])
				{
					int l(i - 1);
					while(t[l] == '0' && l>0) l--;
					t[l]--;
					for (int j(l + 1); j <t.size(); j++) t[j] = '9';
				}
			}
		}
		if (t[0] == '0') t.erase(t.begin());
		cout << "Case #" << cs+1 << ": " << t << endl;
	}
	return 1;
}
int main()
{
	solve();
	//while (solve());
	return 0;
}