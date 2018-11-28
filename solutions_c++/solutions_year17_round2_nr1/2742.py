/*
 * A.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: Mattias De Charleroy
 */
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <iostream>
#include <iomanip>
int main()
    {
    int T;
    std::cin >> T;
    long D;
    int N;
    for (int caseNr = 1; caseNr <= T; caseNr++)
        {
	double maxHours = -1;
	std::cin >> D;
	std::cin >> N;
	long CK;
	long CD;
	double CHours;
	for (int i = 0; i < N; i++)
	    {
	    std::cin >> CD;
	    std::cin >> CK;
	    CHours = ((double) (D - CD)) / CK;
	    if (CHours > maxHours)
		maxHours = CHours;

	    }
	std::cout << "Case #" << caseNr << ": " << std::setprecision(12) << D / maxHours << std::endl;
	}
    return 1;
    }
