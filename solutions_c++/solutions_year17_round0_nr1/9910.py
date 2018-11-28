//
//  main.cpp
//  Problem A. Oversized Pancake Flipper
//
//  Created by Zixuan Wang on 4/8/17.
//  Copyright © 2017 Zixuan Wang. All rights reserved.
//

#include <iostream>
#include <string>
#include <queue>
#include <assert.h>
#include <unordered_map>
#include <fstream>
#include <limits>

//#define TEST

int main(int argc, const char * argv[]) {
	std::streambuf *cinbuf = nullptr;

#ifdef TEST
	std::ifstream in(argv[1]);
	assert(in.is_open());
	cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
#endif

	int total;
	int counter = 0;
	std::cin >> total;
	assert(total >= 0); //prevent count error

	while (counter++ < total) {
		std::string t;
		int k;

		std::cin >> t;
		std::cin >> k;

		const int tLen = static_cast<int>(t.length());
		assert(tLen >= k); //prevent k error

		const std::string endStat = std::string(tLen, '+');

		std::unordered_map<std::string, std::pair<std::string, int>> traceMap;
		traceMap[endStat] = std::make_pair("", std::numeric_limits<int>::max());
		traceMap[t] = std::make_pair("", 0);

		std::queue<std::string> q;
		q.push(t);

		auto generateNext = [&k](const std::string & currentStat, const int & pos)->std::string {
			auto nextStat(currentStat);
			for (int i = pos; i < pos + k; i++) {
				if (nextStat[i] == '-') {
					nextStat[i] = '+';
				}
				else {
					nextStat[i] = '-';
				}
			}
			return nextStat;
		};

		while (!q.empty()) {
			//check if need to stop
			if (traceMap[endStat].second != std::numeric_limits<int>::max()) {
				break;
			}

			auto currentStat = q.front();
			const auto & currentStatData = traceMap[currentStat]; //key always exists
			q.pop();
			for (int i = 0; i <= tLen - k; i++) {
				std::string nextStat = generateNext(currentStat, i);
				//stat not exists
				if (traceMap.find(nextStat) == traceMap.end()) {
					traceMap[nextStat] = std::make_pair(currentStat, currentStatData.second + 1);
					q.push(nextStat);
				}
				//stat already exists
				else {
					auto & existNextData = traceMap[nextStat];
					//current generated next stat is better than previous generated next stat
					if (existNextData.second > currentStatData.second + 1) {
						existNextData.first = currentStat;
						existNextData.second = currentStatData.second + 1;
						q.push(nextStat);
					}
				}
			}
		}

		std::cout << "Case #" << counter << ": ";
		if (traceMap[endStat].second != std::numeric_limits<int>::max()) {
			std::cout << traceMap[endStat].second << std::endl;
		}
		else {
			std::cout << "IMPOSSIBLE" << std::endl;
		}
	}

#ifdef TEST
	std::cin.rdbuf(cinbuf);   //reset to standard input again
#endif

	return 0;
}
