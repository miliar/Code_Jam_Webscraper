#define  _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:256000000")

#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <deque>
#include <queue>
#include <iomanip>
#include <fstream>
#include <string>
#include <functional> 

#define ll long long 
#define ld long double 
#define fi(n) for(ll i = 0; i < (n); i++)
#define FOR(i, k, n) for(ll i = (k); i < (n); i++)
#define all(a) (a.begin(), a.end())

const int INF = 2147483647;
const int mod = 1e9 + 7;
const long long lINF = 9223372036854775807;

using namespace std;

#define cin in
#define cout out

ifstream in;
ofstream out;


int main()
{
	in.open("B-large.in");
	//in.open("input.in");
	out.open("output.out");

	int T;
	cin >> T;
	FOR(tc, 1, T + 1)
	{
		int n, p;
		cin >> n >> p;
		vector<ll> need(n);
		fi(n)
			cin >> need[i];

		vector<vector<pair<ll, ll>>> otr(n, vector<pair<ll, ll>>(p));
		fi(n)
		{
			FOR(j, 0, p)
			{
				ll x;
				cin >> x;
				otr[i][j] = { ((x * 10 - 1) / 11) / need[i] + 1, (x * 10 / 9) / need[i]};
			}
			sort(otr[i].rbegin(), otr[i].rend());
		}

		ll count = 0;
		bool doit = true;
		while (doit)
		{
			ll l = -1, r = INF;
			fi(n)
			{
				l = max(otr[i].back().first, l);
				r = min(otr[i].back().second, r);
			}
			if (l > r)
			{
				ll numb = 0;
				fi(n)
				{
					if (otr[i].back().second < otr[numb].back().second)
						numb = i;
				}
				otr[numb].pop_back();
				if (otr[numb].size() == 0)
					doit = false;
			}
			else
			{
				count++;
				fi(n)
				{
					otr[i].pop_back();
					if (otr[i].size() == 0)
						doit = false;
				}
			}
		}

		cout << "Case #" << tc << ": " << count << endl;
	}
	return 0;
}





