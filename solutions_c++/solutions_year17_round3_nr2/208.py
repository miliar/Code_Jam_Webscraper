#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __int("$3");

int t;
int tt;
int n;
int aj;
int ac;
int tc;
int tj;
int tx;
int e;
priority_queue<pair<int, int>> qc;
priority_queue<pair<int, int>> qj;

pair<pair<int, int>, bool> act[202];
#define c first.first
#define d first.second
#define p second

int main()
{
	cin >> t;
	for (tt = 1; tt <= t; ++tt)
	{
		cin >> ac >> aj;
		tc = 0;
		tj = 0;
		tx = 0;
		while (!qc.empty()) qc.pop();
		while (!qj.empty()) qj.pop();
		for (int i = 0; i < ac; ++i)
		{
			cin >> act[i].c >> act[i].d;
			act[i].p = true;
			tc += act[i].d - act[i].c;
		}
		for (int i = 0; i < aj; ++i)
		{
			cin >> act[i+ac].c >> act[i+ac].d;
			act[i+ac].p = false;
			tj += act[i+ac].d - act[i+ac].c;
		}
		sort(act, act + ac + aj);
		act[ac + aj] = act[0];
		act[ac + aj].c += 1440;
		act[ac + aj].d += 1440;
		e = 0;
		for (int i = 0; i < ac + aj; ++i)
		{
			if (act[i].p && act[i+1].p)
			{
				qc.push(make_pair(act[i].d - act[i+1].c, i));
				e += 2;
			}
			else if ((!act[i].p) && (!act[i+1].p))
			{
				qj.push(make_pair(act[i].d - act[i+1].c, i));
				e += 2;
			}
			else
			{
				tx += act[i+1].c - act[i].d;
				++e;
			}
		}
		while ((!qc.empty()) && (tc - qc.top().first <= 720))
		{
			tc -= qc.top().first;
			qc.pop();
			e -= 2;
		}
		while ((!qj.empty()) && (tj - qj.top().first <= 720))
		{
			tj -= qj.top().first;
			qj.pop();
			e -= 2;
		}
		cout << "Case #" << tt << ": " << e << endl;
	}



	return 0;
}
