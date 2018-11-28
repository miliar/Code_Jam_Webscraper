#include <bits/stdc++.h>

using namespace std;

pair<long long, long long> getInfo(const long long& numberOfStalls, const long long& numberOfPeople)
{
    priority_queue<long long> intervals;
    long long currentInterval;
    intervals.push(numberOfStalls);
    for (int iteration = 0; iteration < numberOfPeople - 1; ++iteration)
    {
        currentInterval = intervals.top();
        intervals.pop();
        intervals.push(currentInterval / 2);
        intervals.push((currentInterval - 1) / 2);
    }
    currentInterval = intervals.top();
    return make_pair(currentInterval / 2, (currentInterval - 1)/2);
}

int main()
{
    int numberOfTests;
    long long numberOfStalls, numberOfPeople;
    scanf("%d", &numberOfTests);
    for (int test = 1; test <= numberOfTests; ++test)
    {
        scanf("%lld %lld", &numberOfStalls, &numberOfPeople);
        pair<long long, long long> answer = getInfo(numberOfStalls, numberOfPeople);
        printf("Case #%d: %lld %lld\n", test, answer.first, answer.second);
    }
	return 0;
}
