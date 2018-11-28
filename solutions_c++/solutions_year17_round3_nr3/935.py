// Core Training.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <unordered_set>
#include <algorithm>

void BestTraining(std::vector<double> &probability, double trainingUnits)
{
	sort(probability.begin(), probability.end());
	int unitsInTraining = 0;
	while (unitsInTraining < probability.size() && trainingUnits > 0)
	{
		double currentProb = probability[unitsInTraining];
		unitsInTraining += 1;
		double target;
		double currentImprovement;
		if (unitsInTraining < probability.size())
		{
			target = probability[unitsInTraining];
		}
		else
		{
			target = 1;
		}
		if (target > trainingUnits / unitsInTraining + currentProb)
		{
			currentImprovement = trainingUnits / unitsInTraining;
			trainingUnits = 0;
		}
		else
		{
			currentImprovement = target - currentProb;
			trainingUnits -= currentImprovement*unitsInTraining;
		}
		for (int i = 0; i < unitsInTraining; i++)
		{
			probability[i] += currentImprovement;
		}
	}
}

double getProbability(std::vector<double> &probability, int needed)
{
	if (needed == probability.size())
	{
		double prob = 1;
		for (auto nextProb : probability)
		{
			prob *= nextProb;
		}
		return prob;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int nootests;
	std::cin >> nootests;
	for (int i = 1; i <= nootests; i++)
	{
		int N, K;
		std::cin >> N >> K;

		std::vector<double> probability;
		double trainingUnits;
		std::cin >> trainingUnits;

		for (int j = 1; j <= N; j++)
		{
			double prob;
			std::cin >> prob;
			probability.push_back(prob);
		}
		
		BestTraining(probability, trainingUnits);

		std::cout << "Case #" << i << ": ";
		std::printf("%.6f", getProbability(probability, K));
		std::cout << std::endl;
	}
	return 0;
}
