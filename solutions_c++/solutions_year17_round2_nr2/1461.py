/*
 * 1.cpp
 *
 *  Created on: 08-Apr-2017
 *      Author: atulb
 */

#include <bits/stdc++.h>

using namespace std;

using LL = long long;
using ULL = unsigned long long;
#define vi vector<LL>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"

void solve(LL casenum)
{
	cout << "Case #" << casenum << ": ";
	LL N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	assert(R + O + Y + G + B + V == N);
	assert(O == 0);
	assert(G == 0);
	assert(V == 0);

	struct color
	{
		char c;
		LL cnt;
		color(char x, LL cn) { c = x; cnt = cn; }
		bool operator<(color& rhs)
		{
			return cnt < rhs.cnt;
		}
	};

	vector<color> v;
	v.pb(color('R', R));
	v.pb(color('Y', Y));
	v.pb(color('B', B));
	//cout << "here" << endl;
	sort(v.rbegin(), v.rend());

	LL sum = R + Y + B;
	LL maxval = (*v.begin()).cnt;

	if (maxval > (sum-maxval))
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	string s;

	while (sum)
	{
		auto it = v.begin();

		if (s.empty()) { s.append(1, (*it).c); (*it).cnt--; sum --; continue; }

		if (((*it).cnt > 0) && s.back() != ((*it).c)) { s.append(1,((*it).c)); (*it).cnt--; sum--; continue; }

		if (v[1].cnt < v[2].cnt) { swap(v[1], v[2]); }
		++it;
		while ((*it).c == s.back() && it != v.end()) ++it;

		assert(it != v.end());
		s.append(1, (*it).c); (*it).cnt--; sum--; continue;
	}

	LL sz = s.size();
	assert(N == sz);

//	cout << casenum << endl;
//	cout << s << endl;
	for (LL i=0;i<N;i++)
	{
		if (i==0) assert(s[0] != s.back() && casenum);
		else assert(s[i] != s[i-1] && casenum);
	}

	cout << s << endl;
}

int main()
{
   ios_base::sync_with_stdio(false);
   LL T;
   cin >> T;
   for (LL i=1;i<=T;++i)
   {
	   solve(i);
   }


   return 0;
}
