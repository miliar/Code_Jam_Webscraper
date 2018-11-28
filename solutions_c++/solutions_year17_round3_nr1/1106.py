// Ample Syrup.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <unordered_set>
#include <algorithm> 

#define _USE_MATH_DEFINES

#include <math.h>

class pancake
{
public:
	long long height;
	long long radius;
	long long area()
	{
		return radius * radius + 2 * height* radius;
	}

	long long heightArea()
	{
		return height * radius * 2;
	}
};

bool byRadius(pancake p1, pancake p2)
{
	return p1.radius > p2.radius;
}

bool byHeightArea(pancake p1, pancake p2)
{
	return p1.heightArea() > p2.heightArea();
}

double getArea(std::vector<pancake> &pancakes, int K)
{
	std::sort(pancakes.begin(), pancakes.end(), byRadius);
	std::vector<pancake> sortedByHeight = pancakes;
	std::sort(sortedByHeight.begin(), sortedByHeight.end(), byHeightArea);
	std::vector<pancake> output;

	long long smallestHeightArea = std::numeric_limits<long long>::max();
	long long largestRadius = std::numeric_limits<long long>::min();
	long long totArea = 0;

	for (int i = 0; i < K; i++)
	{
		pancake current = sortedByHeight[i];
		output.push_back(current);
		totArea += current.heightArea();
		if (smallestHeightArea > current.heightArea()) smallestHeightArea = current.heightArea();
		if (largestRadius < current.radius) largestRadius = current.radius;
	}
	totArea += largestRadius * largestRadius;

	long long bestAreaDiff = 0;

	for (int i = 0; i < pancakes.size(); i++)
	{
		pancake current = pancakes[i];
		if (current.radius <= largestRadius) break;
		long long areaDiff = current.area() - largestRadius * largestRadius - smallestHeightArea;
		if (areaDiff > bestAreaDiff) bestAreaDiff = areaDiff;
	}

	return (totArea + bestAreaDiff) * M_PI;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int nootests;
	std::cin >> nootests;
	for (int i = 1; i <= nootests; i++)
	{
		int N, K;
		std::cin >> N >> K;

		std::vector<pancake> pancakes;
		for (int j = 1; j <= N; j++)
		{
			pancake newPancake;
			std::cin >> newPancake.radius >> newPancake.height;
			pancakes.push_back(newPancake);
		}

		double area = getArea(pancakes, K);

		std::cout << "Case #" << i << ": ";
		std::printf("%.6f", area);
		
		std::cout << std::endl;

	}
	return 0;
}
