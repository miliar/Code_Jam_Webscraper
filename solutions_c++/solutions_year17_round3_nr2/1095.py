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
int Ac, Aj;
int dp[60 * 24 + 10][720 + 10][3][2];
int arr[60 * 24 + 10];

vector<pair<int, pair<int,int> > > vecC, vecJ , vecAll;


int f(int time , int  rTimeC , int nubat , int first) //// numbat == 0 c , numbat == 1 j
{
	if (time == 24 * 60 + 1)
	{
		if (rTimeC == 0)
		{
			if (first == nubat)
				return 0;
			return 1;
		}
		if (rTimeC == -1)
		{
			if (first == nubat)
				return 0;
			return 1;
		}
		return INF;
	}
	if (rTimeC < 0)
		return INF;
	if (dp[time][rTimeC][nubat][first] >= 0)
		return dp[time][rTimeC][nubat][first];
	
	/*if (time - 720 + rTimeC > 720)
		return INF;*/
	int ans = INF;
	if(arr[time] == -1)
	{
		if(nubat == 0)
		{
			ans = min(f(time + 1, rTimeC - 1, 0 , first), f(time + 1, rTimeC, 1 , first) + 1);
		}
		else
		{
			ans = min(f(time + 1, rTimeC, 1 , first), f(time + 1, rTimeC - 1, 0 , first) + 1);
		}
	}
	else if(arr[time] == 0 && nubat == 0)
	{
		ans = f(time + 1, rTimeC, 1 , first) + 1;
	}
	else if(arr[time] == 0 && nubat == 1)
	{
		ans = f(time + 1, rTimeC, nubat , first);
	}
	else if(arr[time] == 1 && nubat == 0)
	{
		ans = f(time + 1, rTimeC - 1, nubat , first);
	}
	else if(arr[time] == 1 && nubat == 1)
	{
		ans = f(time + 1, rTimeC - 1, 0 , first) + 1;
	}
	return dp[time][rTimeC][nubat][first] = ans;
}

int main()
{
	//ofstream cout ("test.out");
	//ifstream cin ("test.in");
	freopen("B.txt" ,"r" , stdin);
	freopen( "Boutput.txt" , "w" , stdout );

	int t = 0;
	cin >> t;
	int test = 1;
	while (t --)
	{
		cin >> Ac >> Aj;
		vecC.clear();
		vecJ.clear();
		vecAll.clear();
		memset(dp, -1, sizeof dp);
		memset(arr, -1, sizeof arr);
		int TimeC = 0, TimeJ = 0;
		for(int i = 0 ; i < Ac ; i ++)
		{
			int c, d;
			pair<int, pair<int,int> > temp;
			cin >> c >> d;
			temp.first = c;
			temp.second.first = d;
			temp.second.second = 0;
			vecC.push_back(temp);
			TimeC += (d - c);
			vecAll.push_back(temp);
			/*for(int k = c ; k <= d ; k++)
			{
				arr[k] = 0;
			}*/
		}
		for(int i = 0 ; i < Aj; i ++)
		{
			int j, k;
			pair<int, pair<int,int> > temp; 
			cin >> j >> k; 
			temp.first = j; 
			temp.second.first = k;
			temp.second.second = 1;
			vecJ.push_back(temp);
			TimeJ += (k - j);
			/*for(int  o = j ; o <= k ; o ++)
			{
				arr[o] = 1;
			}*/
			vecAll.push_back(temp);
		}
		sort(all(vecC));
		sort(all(vecJ));
		sort(all(vecAll));
		for(int o = 0 ; o < vecAll.size() ; o ++)
		{
			for(int p = vecAll[o].first ; p < vecAll[o].second.first ; p++)
			{
				arr[p] = vecAll[o].second.second;
			}
		}

		int ans = min(f(0, 720, 0 , 0), f(0, 720, 1 , 1));
		printf("Case #%d: %d\n" , test++ , ans);
	}
}


