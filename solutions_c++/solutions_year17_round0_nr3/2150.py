#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stdio.h>
#include <vector>
#include <memory>
#include <unordered_map>
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

#ifdef _DEBUG
#define ASSERT(x) if(!(x)) __debugbreak()
#else
char *crash_please=(char *)42;
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
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

char buf[2017];

void Solve()
{
	RLL(n, k);
	ll last=n;
	vector<pair<ll, ll>> h;
	h.emplace_back(n, 1ll);
	auto Insert=[&h](ll s, ll c)
	{
		auto i=find_if(ALL(h), [s](auto &i) {return i.first==s; });
		if(i!=h.end())
		{
			i->second+=c;
			return;
		}
		h.emplace_back(s, c);
		push_heap(ALL(h));
	};
	for(;;)
	{
		if(k<=0)
		{
			ll a=last/2ll, b=last/2ll;
			if((last&1ll)==0)
				--b;
			printf("%lld %lld\n", a, b);
			return;
		}
		auto top=h.front();
		pop_heap(ALL(h));
		h.pop_back();
		last=top.first;
		k-=top.second;
		Insert(top.first/2ll, top.second);
		Insert(top.first&1ll?top.first/2ll:top.first/2ll-1ll, top.second);
	}
}

int Init()
{
	RI(t);
	return t;
}

int main()
{
	//	std::ios::sync_with_stdio(false);
	int t=Init();
//	int t=1;
	//	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		printf("Case #%d: ", tc);
		Solve();
	}
}