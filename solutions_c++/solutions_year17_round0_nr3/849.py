#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

struct setCompare
{
	bool operator()(const pair<long long, long long>& left, const pair<long long, long long>& right) const
	{
		if (left.second - left.first == right.second - right.first)
		{
			return left.first < right.first;
		}
		return left.second - left.first > right.second - right.first;
	}
};

//pair<long long, long long> stall(long long N, long long K)
//{
//	if (N == K) return pair<long long, long long>(0, 0);
//	set<pair<long long, long long>, setCompare> ranges;
//	ranges.insert(pair<long long, long long>((long long)1, N));
//	pair<long long, long long> res;
//	for (int i = 1; i <= K; ++i)
//	{
//		pair<long long, long long> target = *ranges.begin();
//		ranges.erase(target);
//		long long mid = (target.first + target.second) / 2;
//		res.first = mid - target.first;
//		res.second = target.second - mid;
//		if (res.first < res.second) swap(res.first, res.second);
//		if (i == K)
//			break;
//		if (target.first <= mid - 1)
//			ranges.insert(pair<long long, long long>(target.first, mid - 1));
//		if (mid + 1 <= target.second)
//			ranges.insert(pair<long long, long long>(mid + 1, target.second));
//	}
//	return res;
//}

pair<long long, long long> stall(long long N, long long K)
{
	if (N == K) return pair<long long, long long>(0, 0);
	while (K != 1)
	{
		if (N % 2 == 0)
		{
			if (K % 2 == 0)
			{
				N = N / 2;
				K /= 2;
			}
			else
			{
				N = N / 2 - 1;
				K = (K - 1) / 2;
			}
		}
		else
		{
			if (K % 2 == 0)
			{
				N = N / 2;
				K = K / 2;
			}
			else
			{
				N = N / 2;
				K = K / 2;
			}
		}
	}
	long long mid = (N + 1) / 2;
	long long left = mid - 1;
	long long right = N - mid;
	return pair<long long, long long>(max(left, right), min(left, right));
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i)
	{
		long long N, K;
		cin >> N >> K;
		pair<long long, long long> res = stall(N, K);

		cout << "Case #" << i << ": " << res.first << " " << res.second <<'\n';
	}
	return 0;
}