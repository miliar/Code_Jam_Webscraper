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


enum class eHeapStype { Min, Max };

template<class T, eHeapStype HeapStype = eHeapStype::Max>
class tHeap
{
	std::vector<T> mItems;
	static size_t GetParentIndex(size_t i) { return (i - 1) / 2; }
	static size_t GetLeftChildIndex(size_t i) { return (i * 2) + 1; }
	static size_t GetRightChildIndex(size_t i) { return GetLeftChildIndex(i) + 1; }
	static bool IsStronger(const T &a, const T &b) { return a < b; }
	size_t BubbleUp(size_t i)
	{
		while (i) // at most until it is at the root
		{
			auto ParentIndex = GetParentIndex(i);
			if (IsStronger(mItems[i], mItems[ParentIndex]))
			{
				std::swap(mItems[i], mItems[ParentIndex]);
				i = ParentIndex;
			}
			else
				break;
		}
		return i;
	}
	void FixHeap(size_t i)
	{
		for (;;)
		{
			auto LeftChildIndex = GetLeftChildIndex(i);
			if (LeftChildIndex >= mItems.size())
				break;
			auto &LeftChild = mItems[LeftChildIndex];
			auto RightChildIndex = GetRightChildIndex(i);
			bool IsRightBiggerThanLeft = RightChildIndex < mItems.size() && IsStronger(mItems[RightChildIndex], mItems[LeftChildIndex]);
			auto &ItemToCompare = mItems[IsRightBiggerThanLeft ? RightChildIndex : LeftChildIndex];
			if (IsStronger(ItemToCompare, mItems[i]))
			{
				std::swap(ItemToCompare, mItems[i]);
				i = IsRightBiggerThanLeft ? RightChildIndex : LeftChildIndex;
			}
			else
				break;
		}
	}
public:
	void push(T Item)
	{
		size_t i = mItems.size();
		mItems.emplace_back(Item);
		BubbleUp(i);
	}
	void erase(size_t i)
	{
		if (i == mItems.size() - 1)
		{
			mItems.pop_back();
			return;
		}
		std::swap(mItems.back(), mItems[i]);
		mItems.pop_back();

		if (i != BubbleUp(i))
			return;
		FixHeap(i);
	}
	void erase(typename std::vector<T>::const_iterator i) { erase(i - mItems.begin()); }
	void heapify(std::vector<T> &&Items)
	{
		mItems = std::move(Items);
		if (mItems.size() <= 1)
			return;
		size_t i = GetParentIndex(mItems.size() - 1);
		for (;;)
		{
			FixHeap(i);
			if (i == 0)
				break;
			--i;
		}
	}
	const T &front() const { return mItems[0]; }
	T pop_front()
	{
		T t(std::move(mItems[0]));
		erase(0);
		return t;
	}
	size_t size() const { return mItems.size(); }
	bool empty() const { return mItems.empty(); }

	auto begin() { return mItems.begin(); }
	auto end() { return mItems.end(); }
	auto begin() const { return mItems.begin(); }
	auto end() const { return mItems.end(); }
};


struct cCity
{
	ll horse_dist;
	double horse_speed;
};

vector<cCity> cities;
vector<ll> dists;

struct cFrontierData
{
	int city;
	ll horse_mile_left;
//	double horse_speed;
	int horse_home_city;
	double time_used;
	cFrontierData(int city, ll horse_mile_left, int horse_home_city, double time_used) :
		city(city), horse_mile_left(horse_mile_left), horse_home_city(horse_home_city), time_used(time_used) {}
	bool operator<(const cFrontierData &a) const
	{
		return time_used < a.time_used;
	}
};



void Solve(int u, int v, int n)
{
//	vector<double> best_time(cities.size(), numeric_limits<double>::max());
	vector<unordered_map<int, double>> best_times;
	best_times.resize(n);
	tHeap<cFrontierData, eHeapStype::Min> frontier;
	frontier.push(cFrontierData(u, 0, u, 0.0));
	while (!frontier.empty())
	{
		cFrontierData top=frontier.front();
		frontier.pop_front();
		double &best_time = best_times[top.city][top.horse_home_city];
		if(best_time!=0.0&&top.time_used>=best_time)
			continue;
 		best_time = top.time_used;
		for (int target_city = 0; target_city < n; ++target_city)
		{
			auto dist = dists[top.city*n + target_city];
			if(dist==-1ll)
				continue;
			if (top.horse_mile_left >= dist)
			{
				double time_to_target = (double)dist / cities[top.horse_home_city].horse_speed;
				time_to_target += top.time_used;
				auto target_best_time = best_times[target_city][top.horse_home_city];
				if (target_best_time==0.0||time_to_target < target_best_time)
				{
					frontier.push(cFrontierData(target_city, top.horse_mile_left - dist, top.horse_home_city, time_to_target));
				}
			}
			if (cities[top.city].horse_dist >= dist)
			{
				double time_to_target = (double)dist / cities[top.city].horse_speed;
				time_to_target += top.time_used;
				auto target_best_time = best_times[target_city][top.city];
				if (target_best_time==0.0||time_to_target < target_best_time)
				{
					frontier.push(cFrontierData(target_city, cities[top.city].horse_dist - dist, top.city, time_to_target));
				}
			}
		}
	}
	auto i = min_element(ALL(best_times[v]), [](auto &a, auto &b) {return a.second < b.second; });
	printf("%.7f", i->second);
}

void Solve()
{
	RII(n, q);
	cities.resize(n);
	dists.resize(n*n);
	for (auto &city : cities)
		scanf("%lld %lf", &city.horse_dist, &city.horse_speed);
	for (auto &d : dists)
		scanf("%lld", &d);
	FOR(i, q)
	{
		RII(u, v);
		--u; --v;
		Solve(u, v, n);
		if (i != q - 1)
			printf(" ");
	}
	printf("\n");
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