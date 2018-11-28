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
#define fi(n) for(int i = 0; i < (n); i++)
#define FOR(i, k, n) for(int i = (k); i < (n); i++)
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
	in.open("C-small-2-attempt0.in");
	out.open("C-small.out");

	int T;
	cin >> T;
	FOR(tc, 1, T + 1)
	{
		ll n, k;
		cin >> n >> k;
		priority_queue<ll> q;
		q.push(n);
		fi(k - 1)
		{
			q.push(q.top() - 1 - (q.top() - 1) / 2);
			q.push((q.top() - 1) / 2);
			q.pop();
		}
		ll a = (q.top() - 1) / 2;
		ll b = q.top() - 1 - (q.top() - 1) / 2;
		cout << "Case #" << tc << ": " << max(a, b) << " " << min(a, b) << endl;
	}
	return 0;
}





