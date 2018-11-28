// CodeJamC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <queue>
#include <map>

using namespace std;

class MyQ
{
	struct classcomp {
		bool operator() (const long long& lhs, const long long& rhs) const
		{
			return lhs > rhs;
		}
	};

	map<long long,long long,classcomp> m;	// map of empty spaces and count, sorted from biggest element to smalleset

public:
	long long top()	// return the top item
	{
		map<long long, long long>::iterator it = m.begin();
		return it->first;
	}
	void pop()	// remove the top item
	{
		map<long long, long long>::iterator it = m.begin();
		if (it->second > 1)
			it->second = it->second - 1; // decrement the count
		else
			m.erase(it);
	}
	void push(long long val) // push new item
	{
		if (val <= 0)
			return;

		map<long long, long long>::iterator it = m.find(val);
		if (it == m.end())
			m.insert(make_pair(val, 1));
		else
			it->second = it->second + 1;	// increment the count
	}
};

void fillStalls2(long long n, long long k, long long &min, long long& max)
{
	min = 0; max = 0;
	// early return 
	if (k == n)
	{
		min = max = 0;
		return;
	}

	//priority_queue<long long> q;
	MyQ q;
	q.push(n);
	long long counter = 0;
	while (counter < k)
	{
		long long x = q.top();
		q.pop();

		//early return
		if (x == 1) 
		{
			max = min = 0;
			return;
		}

		max = x / 2;
		min = x - 1 - max;

		q.push(max);
		q.push(min);
		++counter;

		//printf("x max min (%d): %d \t%d \t%d\n", counter, x, max, min);

	}
}

void main() {
	long long t, n, k;
	long long min, max;
	cin >> t;
	for (long long i = 1; i <= t; ++i) {
		cin >> n >> k;  // read n and then m.
		fillStalls2(n, k, min, max);
		cout << "Case #" << i << ": " << max << " " << min << endl;
	}
}
