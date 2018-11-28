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


void Solve()
{
	RIII(seats, riders, tickets_sold);
	vector<pair<int, int>> tickets(tickets_sold);
	vector<int> tickets_of_rider(riders, 0);
	for(auto &t: tickets)
	{
		scanf("%d %d", &t.first, &t.second);  // position, rider id
		++tickets_of_rider[t.second-1];
	}
	int number_of_cars=*max_element(ALL(tickets_of_rider));
	vector<int> promotions_per_seat(seats+1, 0);

	sort(ALL(tickets));
	int left_over=0;
	for(int served_seat=1; served_seat<=seats; ++served_seat)
	{
		left_over+=number_of_cars;
		int tickets_for_seat=(int)count_if(ALL(tickets), [served_seat](auto &t) { return served_seat==t.first; });
		promotions_per_seat[served_seat]=max(0, tickets_for_seat-number_of_cars);
		left_over-=tickets_for_seat;
		while(left_over<0)
		{
			++number_of_cars;
			left_over+=served_seat;
			for(int s=1; s<=served_seat; ++s)
			{
				if(promotions_per_seat[s]>0)
					--promotions_per_seat[s];
			}
		}
	}

	printf("%d %d\n", number_of_cars, accumulate(ALL(promotions_per_seat), 0));
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
	//	int t=1;
	//	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		printf("Case #%d: ", tc);
		Solve();
	}
}