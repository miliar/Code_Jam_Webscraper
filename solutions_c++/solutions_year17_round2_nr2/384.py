#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <vector>
#include <memory>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <numeric>
#include <string>
#include <set>
#include <tuple>
#include <functional>
#include <cstring>
#include <deque>
#include <array>
#include <map>
#include <random>

#undef max
#undef min

#ifdef __GNUC__ 
#pragma GCC diagnostic ignored "-Wunused-result"
#endif

char *crash_please=(char *)42;

#ifdef _DEBUG
#define ASSERT(x) if(!(x)) __debugbreak()
#else
#define ASSERT(x) 
//if(!(x)) { printf("%s failed",#x); *crash_please=33; }
#endif

#include <chrono>

class cLogPerformance_Guard
{
	std::chrono::time_point<std::chrono::high_resolution_clock> mStartTime=std::chrono::high_resolution_clock::now();
	const char *mName;
public:
	cLogPerformance_Guard(const char *Name): mName(Name) {}
	~cLogPerformance_Guard()
	{
		auto EndTime=std::chrono::high_resolution_clock::now();
		auto Elapsed=std::chrono::duration_cast<std::chrono::milliseconds>(EndTime-mStartTime);
		//		printf("--- Elapsed %llu ms in %s ---\n", (unsigned long long)Elapsed.count(), mName);
	}
};

using namespace std;
using namespace std::string_literals;
using ull=unsigned long long;
using ll=long long;
constexpr ll mod=1'000'000'007;

template<class I> auto rev(I i) { return std::reverse_iterator<I>(i); }

#define RI(var_name) int var_name; scanf("%d", &var_name);
#define RIV(var_name, size) vector<int> var_name(size); for(auto &item_of_##var_name: var_name) scanf("%d", &item_of_##var_name);
#define RII(var_name1, var_name2) int var_name1, var_name2; scanf("%d %d", &var_name1, &var_name2);
#define RIII(var_name1, var_name2, var_name3) int var_name1, var_name2, var_name3; scanf("%d %d %d", &var_name1, &var_name2, &var_name3);
#define RIIII(var_name1, var_name2, var_name3, var_name4) int var_name1, var_name2, var_name3, var_name4; scanf("%d %d %d %d", &var_name1, &var_name2, &var_name3, &var_name4);
#define RL(var_name) ll var_name; scanf("%lld", &var_name);
#define RLV(var_name, size) vector<ll> var_name(size); for(auto &item_of_##var_name: var_name) scanf("%lld", &item_of_##var_name);
#define RLL(var_name1, var_name2) ll var_name1, var_name2; scanf("%lld %lld", &var_name1, &var_name2);
#define RLLL(var_name1, var_name2, var_name3) ll var_name1, var_name2, var_name3; scanf("%lld %lld %lld", &var_name1, &var_name2, &var_name3);
#define RD(var_name) double var_name; scanf("%lf", &var_name);
#define RDV(var_name, size) vector<double> var_name(size); for(auto &item_of_##var_name: var_name) scanf("%d", &item_of_##var_name);
#define RDD(var_name1, var_name2) double var_name1, var_name2; scanf("%lf %lf", &var_name1, &var_name2);
#define RDDD(var_name1, var_name2, var_name3) double var_name1, var_name2, var_name3; scanf("%lf %lf %lf", &var_name1, &var_name2, &var_name3);
#define ALL(cont) cont.begin(), cont.end()
#define FOR(var, max_value) for(int var=0;var<max_value;++var)
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//#define EXTRA_LOGS

// struct cHorse
// {
// 	ll start;
// 	ll speed;
// };

struct cColor
{
	char color;
	char subchar;
	int count;
	int subs_count;
};

void Solve()
{
	RI(n);
	RIII(r, o, y);
	RIII(g, b, v);
	if (y < v * 2 || b < o * 2 || r < g * 2)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	y -= v;
	b -= o;
	r -= g;
	vector<cColor> cs(3);
	cs[0].color = 'R';
	cs[1].color = 'Y';
	cs[2].color = 'B';
	cs[0].subchar = 'G';
	cs[1].subchar = 'V';
	cs[2].subchar = 'O';
	cs[0].count = r;
	cs[0].subs_count = g;
	cs[1].count = y;
	cs[1].subs_count = v;
	cs[2].count = b;
	cs[2].subs_count = o;
	sort(ALL(cs), [](auto &a, auto &b) { return a.count < b.count; });
	if(cs[2].count>cs[1].count+cs[0].count)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	int overshot = cs[1].count + cs[0].count - cs[2].count;
	vector<char> result(n);
	for (int p=0; p<n;)
	{
		auto PlaceC = [&p, &result](cColor &color)
		{
			--color.count;
			result[p] = color.color;
			++p;
			if (color.subs_count > 0)
			{
				result[p] = color.subchar;
				++p;
				result[p] = color.color;
				++p;
				--color.subs_count;
			}
		};
		PlaceC(cs[2]);
		if (cs[1].count)
		{
			PlaceC(cs[1]);
			if (overshot)
			{
				PlaceC(cs[0]);
				--overshot;
			}
		}
		else
			PlaceC(cs[0]);
	}
	printf("%.*s\n", n, result.data());
}

int Init()
{
	RI(t);
	//	int t=1;
	return t;
}

int main()
{
	//	std::ios::sync_with_stdio(false);
	int t=Init();
	for(int tc=1; tc<=t; ++tc)
	{
		printf("Case #%d: ", tc);
		Solve();
	}
}