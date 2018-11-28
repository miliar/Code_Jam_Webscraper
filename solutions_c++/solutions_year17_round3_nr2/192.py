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

const int MaxN = 720 * 2;
int minutes[MaxN + 10];

int getChange(vi dif, int time_)
{
	{
		int i = 0;
		int m = dif.size();
		while (i < m)
		{
			if (time_ >= dif[i]) time_ -= dif[i];
			else return m - i;
			i++;
		}
	}

	return 0;
}

void solve()
{
	memset(minutes, 0, sizeof(minutes));
	int c, j;
	cin >> c >> j;
	int cTime = 720;
	int jTime = 720;

	for (int i = 0; i < c; i++)
	{
		int start, finish;
		cin >> start >> finish;
		jTime -= (finish - start);
		for (int j = start; j < finish; j++)
			minutes[j] = 2;
	}

	for (int i = 0; i < j; i++)
	{
		int start, finish;
		cin >> start >> finish;
		cTime -= (finish - start);
		for (int j = start; j < finish; j++)
			minutes[j] = 1;
	}

	vi cDif;
	vi jDif;
	int change = 0;
	int first = 0;
	while (minutes[first] == 0)
		first++;

	int prevT = first;
	int prev = minutes[first];
	for (int j = 1; j <= MaxN; j++)
	{
		int i = (first + j) % MaxN;
		if (minutes[i] != 0)
		{
			int delta = i - prevT;
			if (delta < 0) delta += MaxN;
			delta--;
			if (minutes[i] == prev &&  delta > 0)
			{
				if (minutes[i] == 1) cDif.push_back(delta);
				else jDif.push_back(delta);
			}
			if (minutes[i] != prev)
				change++;
			prev = minutes[i];
			prevT = i;
		}
	}

	sort(cDif.begin(), cDif.end());
	sort(jDif.begin(), jDif.end());
	
	change += 2 * getChange(cDif, cTime);
	change += 2 * getChange(jDif, jTime);

	cout << change << endl;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// LL a[110];
	// memset(a,0,sizeof(a));

	freopen("B-large.in","r",stdin);
	freopen("output_B_large.txt","w",stdout);
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