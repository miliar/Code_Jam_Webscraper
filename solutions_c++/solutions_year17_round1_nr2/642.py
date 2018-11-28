#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <memory>
#include <utility>
#include <regex>
#include <functional>
#include <tuple>
#include <cassert>
#include <queue>

#ifndef NDEBUG
#define debug(...) WriteLine("Debug [", __LINE__ ,"]: ", __VA_ARGS__)
#define named(x) '[', #x, ": ", x, "] "
#else
#define debug(...)
#endif

namespace Enum
{
	class Range
	{
		using T = int;
		struct RangeIterator
		{
			T i;
			T operator * () const { return i; }
			auto operator ++ () { ++i; }
			auto operator != (const RangeIterator& other) const { return i < *other; }
		};
		const T from, to;
		public:
			Range(T from, T to) : from{from}, to{++to} {};
			RangeIterator begin() const { return {from}; }
    		RangeIterator end() const { return {to}; }
	};
};

using namespace std;
using lint = long long;
using ulint = unsigned long long;

template<class... Args> using HashSet = unordered_set<Args...>;
template<class... Args> using HashMap = unordered_map<Args...>;
template<class... Args> using Unique = unique_ptr<Args...>;
template<class... Args> using Shared = shared_ptr<Args...>;

#define range(x) x.begin(), x.end()
#define rev_range(x) x.rbegin(), x.rend()

template<class T> T Read()
{
	T in;
	cin >> in;
	return in;
}

template<class... Args> auto Read(Args&... args)
{
	(cin >> ... >> args);
}

auto ReadLine()
{
	while(isspace(cin.peek())) cin.ignore();
	string line;
	getline(cin, line);
	return line;
}

template<class... Args> auto Write(const Args&... args)
{
	(cout << ... << args);
}

template<class... Args> auto WriteLine(const Args&... args)
{
	Write(args..., '\n');
}

auto UseFixedDoubleDisplay(int precision)
{
	cout << fixed << setprecision(precision);
}

void SolveCase(int caseId);
int main()
{
	UseFixedDoubleDisplay(6);
	for(auto caseId : Enum::Range(1, Read<int>()))
		SolveCase(caseId);
	return 0;
}

int R[51], minR[51], maxR[51];
vector<pair<int,int>> Q[51];

void SolveCase(int caseId)
{
	auto N = Read<int>();
	auto P = Read<int>();

	for(int i = 0; i < N; ++i)
	{
		Q[i].clear();
		Read(R[i]);
		minR[i] = R[i] * 9;
		maxR[i] = R[i] * 11;
		R[i] = 0;
	}
	
	for(int i = 0; i < N; ++i)
	{
		for(int j = 0; j < P; ++j)
		{
			auto q = Read<int>() * 10;
			auto d1 = q / minR[i];
			auto d2 = q / maxR[i];
			if(d1 > (q / (maxR[i]+1)))
				Q[i].emplace_back(d2, d1); 
		}
		sort(range(Q[i]), [](const auto& x, const auto& y)
		{
			return x.first == y.first ? x.second < y.second : x.first < y.first;
		});
	}
	
	int kits = 0;
	bool done = false;
	while(true)
	{
		for(int i = 0; i < N; ++i)
			if(R[i] >= (int)Q[i].size())
				done = true;
		
		if(done)
			break;
		
		int leftQ = 0;
		int rightQ = 1000000000;
		for(int i = 0; i < N; ++i)
		{
			leftQ = max(leftQ, Q[i][R[i]].first);
			rightQ = min(rightQ, Q[i][R[i]].second); 
		}
		
		if(leftQ <= rightQ)
		{
			++kits;
			for(int i = 0; i < N; ++i)
				++R[i];
		}
		else
		{
			for(int i = 0; i < N; ++i)
				if(Q[i][R[i]].second < leftQ)
					++R[i];
		}
	}
	
	WriteLine("Case #", caseId, ": ", kits);
}


