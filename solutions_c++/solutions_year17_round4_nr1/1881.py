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
	in.open("A-small-attempt4.in");
	//in.open("input.in");
	out.open("output.out");

	int T;
	cin >> T;
	FOR(tc, 1, T + 1)
	{
		ll p, n;
		cin >> n >> p;
		ll cnt[4];
		fill(cnt, cnt + 4, 0);
		fi(n)
		{
			ll x;
			cin >> x;
			cnt[x % p]++;
		}
		ll answ = 0;
		answ += cnt[0];
		if (p == 2)
		{
			answ += cnt[1] / 2;
			if (cnt[1] % 2 != 0)
				answ++;
		}
		else if (p == 3)
		{
			if (cnt[1] > cnt[2])
			{
				answ += cnt[2];
				answ += (cnt[1] - cnt[2]) / 3;
				if ((cnt[1] - cnt[2]) % 3 != 0)
					answ++;
			}
			else
			{
				answ += cnt[1];
				answ += (cnt[2] - cnt[1]) / 3;
				if ((cnt[2] - cnt[1]) % 3 != 0)
					answ++;
			}
		}
		cout << "Case #" << tc << ": " << answ << endl;
	}
	return 0;
}





