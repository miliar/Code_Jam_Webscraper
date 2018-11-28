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

void SolveCase(int caseId)
{
	auto N = Read<lint>();
	auto s = to_string(N);

	auto convertToNineI = s.length();
	for(int i = s.length() - 1; i > 0; --i)
	{
		if(s[i] < s[i-1])
		{
			--s[i-1];
			convertToNineI = i;
		}
	}
	
	for(int i = convertToNineI; i < s.length(); ++i)
	{
		s[i] = '9';
	}
	
	auto result = stoll(s);
	
	WriteLine("Case #", caseId, ": ", result);
}


