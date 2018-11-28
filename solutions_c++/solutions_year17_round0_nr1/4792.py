#pragma warning(disable : 4996) //_CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <set>
#include <time.h>
#include <iomanip>
#include <iso646.h>
#include <stdio.h>
#include <map>
#include <queue>

typedef long long LL;
typedef long double LD;
typedef unsigned long long ull;

#define sync ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ss second
#define ff first
#define mp make_pair
#define endl "\n"
#define pb push_back
#define FilkinMaksim int main()
#define exit return 0
#define f_in freopen("chemie.in", "r", stdin)
#define f_out freopen("chemie.out", "w", stdout)
#define file_on f_in; f_out

//const LD M_PI = 3.14159265358979323846;
const LD EPS = 0.0000000001;
const LL INF = 1000000007;

using namespace std;

int main()
{
	//file_on;
	int t;
	cin >> t;
	for (int h = 1; h <= t; h++)
	{
		long long ans = 0;
		string s;
		int l;
		cin >> s;
		cin >> l;
		bool ok = true;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				if (l + i <= s.size())
				{
					ans++;
					for (int j = i; j < i+l; j++)
						if (s[j] == '-') s[j] = '+';
						else s[j] = '-';
				}
				else
				{
					ok = false;
					break;
				}
			}
		}
		if (ok) cout << "Case #" << h << ": " << ans << endl;
		else cout << "Case #" << h << ": IMPOSSIBLE"<< endl;
	}
	return 0;
}

// cout <<"Case #"<<h<<": "<<x*j << endl;