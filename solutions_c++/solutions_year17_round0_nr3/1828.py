#include <iostream>

using namespace std;

pair<long long, long long> getStall(long long order, long long totalStall)
{
	pair<long long, long long> result;
	long long remainStall = totalStall;
	long long currentDepthNode = 1;
	long long currentMaxNode = 1;

	while(true)
	{
		remainStall -= currentDepthNode;

		if(order <= currentMaxNode)
		{
			long long plusOneNode = remainStall % currentDepthNode;
			remainStall /= currentDepthNode;
			if(order - currentMaxNode / 2 <= plusOneNode)
				remainStall++;
			break;
		}

		currentDepthNode *= 2;
		currentMaxNode = currentMaxNode * 2 + 1;
	}

	result.first = result.second = remainStall / 2;
	if(remainStall % 2 == 1)
		result.second++;

	return result;
}

int main()
{
	int t;
	long long k, n;

	cin >> t;

	for(int idxCase = 0; idxCase < t; idxCase++)
	{
		cin >> n >> k;
		pair<long long, long long> stallValue = getStall(k, n);
		cout << "Case #" << idxCase + 1 << ": " << stallValue.second << " " << stallValue.first << endl;
	}
	return 0;
}
