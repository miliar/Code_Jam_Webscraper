// codejam.cpp : definisce il punto di ingresso dell'applicazione console.
//

#include "stdafx.h"

#include <algorithm>
#include <iostream>
#include <utility>
#include <map>

#define ULL unsigned long long

int main ()
{
	int testCases = 0;
	std::cin >> testCases;
	ULL zero = 0L;

	for (int i = 0; i < testCases; ++i)
	{
		std::multimap<ULL, ULL> mapSegments;

		ULL stallsCount = 0ULL;
		ULL peopleCount = 0ULL;
		std::cin >> stallsCount >> peopleCount;

		if (stallsCount == peopleCount)
		{
			std::cout << "Case #" << (i + 1) << ": 0 0\n";
			continue;
		}

		mapSegments.insert (std::pair<ULL, ULL> (_ULLONG_MAX - stallsCount, zero));

		while (true)
		{
			auto itrFirst = mapSegments.begin ();

			//ULL segmentLength = -(itrFirst->first - _ULLONG_MAX);
			ULL segmentLength = _ULLONG_MAX - itrFirst->first;
			ULL startIndex = itrFirst->second;

			mapSegments.erase (itrFirst);

			ULL maxIndex = startIndex + segmentLength - 1;
			ULL newSegmentLength = segmentLength / 2ULL;
			ULL middleIndex = startIndex + newSegmentLength;

			if (segmentLength % 2ULL == 0)
			{
				--middleIndex;
			}

			ULL length1 = middleIndex - startIndex;
			ULL length2 = maxIndex - middleIndex;

			ULL maxLen = std::max<ULL> (length1, length2);
			ULL minLen = std::min<ULL> (length1, length2);

			if (peopleCount == 1)
			{
				std::cout << "Case #" << (i + 1) << ": " << maxLen << " " << minLen << "\n";
				break;
			}

			mapSegments.insert (std::pair<ULL, ULL> (_ULLONG_MAX - length1, startIndex));
			mapSegments.insert (std::pair<ULL, ULL> (_ULLONG_MAX - length2, middleIndex + 1));

			--peopleCount;
		}

		int asd = 0;
	}

	return 0;
}