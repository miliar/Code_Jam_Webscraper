/*
 * BathRoomStalls.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: mattias
 */

#include <iostream>
#include <map>
#include <utility>

std::pair<long long, long long> split(long long n)
{
	if (n == 0)
		return {0, 0};
	if (n % 2 == 1)
		return {(n-1)/2, (n-1)/2};
	return {n/2, n/2 -1};
}

int main()
{
	int T;
	std::cin >> T;
	long long N;
	long long K;

	std::pair<long long,long long> splitting;
	std::map<long long, long long, std::greater<long long>> stallInfo;
	decltype(stallInfo)::iterator findResult;
	long long last = -1;
	for (int caseNr = 0; caseNr < T; caseNr++)
	{
		std::cin >> N;
		std::cin >> K;
		stallInfo.clear();
		stallInfo[N] = 1;
		while (K >= 1)
		{
			auto &keyValue = *stallInfo.begin();
			K -= keyValue.second;
			last = keyValue.first;
			splitting = split(keyValue.first);

			findResult = stallInfo.find(splitting.first);
			if (findResult != stallInfo.end())
				findResult->second += keyValue.second;
			else
				stallInfo[splitting.first] = keyValue.second;

			findResult = stallInfo.find(splitting.second);
			if (findResult != stallInfo.end())
				findResult->second += keyValue.second;
			else
				stallInfo[splitting.second] = keyValue.second;
			stallInfo.erase(keyValue.first);
		}
		splitting = split(last);
		std::cout << "Case #" << (caseNr + 1) << ": " << splitting.first << " " << splitting.second << std::endl;

	}
	return 0;
}

