#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>


using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<LL, LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))

int isTidy(string s)
{
	for (int i = 1; i < s.length(); i++)
		if (s[i] < s[i - 1])
			return i;
	return -1;
}

string getNines(int n)
{
	string ans = "";
	for (int i = 0; i < n; i++)
		ans += '9';
	return ans;
}

string dec(string s, int i)
{
	while (i >= 0)
	{
		s[i]--;
		if (i > 0)
		{
			if (s[i] < s[i - 1]) i--;
			else break;
		}
		else break;
	}
	if (s[0] == '0') return getNines(s.length() - 1);
	return s.substr(0, i + 1) + getNines(s.length() - i - 1);
}

void solve()
{
	string s;
	cin >> s;
	int i = isTidy(s);
	if (i == -1)
	{
		cout << s << endl;
		return;
	}

	cout << dec(s, i - 1) << endl;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	//cout<<fixed;
	//cout<<setprecision(9);

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}