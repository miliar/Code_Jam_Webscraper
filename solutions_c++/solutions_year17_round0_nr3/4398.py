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

struct segment
{
	LL start;
	LL len;
	segment(LL s, LL l) { start = s; len = l; }

	bool operator<(const segment& rhs) const
	{
		if (len != rhs.len)
			return len > rhs.len;
		else
			return start < rhs.start;
	}
};

using segset = set<segment>;

void solve(LL casenum)
{
	cout << "Case #" << casenum << ": ";
	LL N,K;

	cin >> N >> K;
	segset myset;

	segment s(0, N);
	myset.insert(s);

	LL ret1,ret2;

	for (LL i=1;i<=K;++i) {
//		cout << " printing set for i = " << i << endl;
//		for (auto it : myset)
//			cout << "\n" << it.start << " " << it.len << endl;

		assert(!myset.empty());
		segment curr = *myset.begin();
		myset.erase(myset.begin());

		assert(curr.len > 0);

		if (curr.len % 2 == 1)
		{
			segment s1(curr.start, curr.len/2);
			segment s2(curr.start + curr.len/2 + 1, curr.len/2);
			if (s1.len > 0) myset.insert(s1);
			if (s2.len > 0) myset.insert(s2);
			if (i==K) { ret1 = max(s1.len, s2.len); ret2 = min(s1.len, s2.len); }
		}
		else
		{
			segment s1(curr.start, curr.len/2-1);
			segment s2(curr.start + curr.len/2, curr.len/2);
			if (s1.len > 0) myset.insert(s1);
			if (s2.len > 0) myset.insert(s2);
			if (i==K) { ret1 = max(s1.len, s2.len); ret2 = min(s1.len, s2.len); }
		}
	}
	cout << ret1 << " " << ret2 << endl;
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
