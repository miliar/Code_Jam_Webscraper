#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <set>
#include <cassert>
using namespace std;

typedef unsigned long long ull;
class Solver
{
public:
	Solver(ull length, ull numberOfPeople) : m_length(length), m_numberOfPeople(numberOfPeople)
	{
	}
	pair<ull, ull> solve()
	{
		multiset<ull, greater<ull>> priorityQueue;
		priorityQueue.insert(m_length);

		pair<ull, ull> result = make_pair(0, 0);
		for (ull round = 1; round <= m_numberOfPeople; ++round)
		{
			const ull firstElement = *priorityQueue.begin();
			//cout << firstElement << endl;
			priorityQueue.erase(priorityQueue.begin());
			if (firstElement == 1)
				return make_pair(0, 0);

			if (firstElement % 2 == 0)
				result = make_pair(firstElement / 2, firstElement / 2 - 1);
			else
				result = make_pair(firstElement / 2, firstElement / 2);

			priorityQueue.insert(result.first);
			priorityQueue.insert(result.second);
		}
		return result;
	}
private:
	ull m_length;
	ull m_numberOfPeople;
};

void check(int length, int numberOfPeople, int first, int second)
{
	Solver s(length, numberOfPeople);
	pair<ull, ull> result = s.solve();
	assert(result.first == first && result.second == second);
}

int main()
{
//#define DEBUG
#ifdef DEBUG
	multiset<int, greater<int> > s;
	s.insert(2);
	s.insert(2);
	s.insert(3);
	s.insert(3);

	s.erase(s.begin());
	cout << s.count(2) << endl;
	cout << s.count(3) << endl;
	check(4, 2, 1, 0);
	check(5, 2, 1, 0);
	check(6, 2, 1, 1);
	check(1000, 1000, 0, 0);
	check(1000, 1, 500, 499);
	check(1, 1, 0, 0);
	check(2, 1, 1, 0);
	check(3, 1, 1, 1);
	check(4, 1, 2, 1);
	printf("Finished\n");
#endif
	int tests;
	scanf("%d", &tests);
	for (int testCase = 1; testCase <= tests; ++testCase)
	{
		ull length, numberOfPeople;
		scanf("%llu%llu", &length, &numberOfPeople);
		Solver s(length, numberOfPeople);
		printf("Case #%d: %llu %llu\n", testCase, s.solve().first, s.solve().second);
	}

	//system("pause");
	return 0;
}