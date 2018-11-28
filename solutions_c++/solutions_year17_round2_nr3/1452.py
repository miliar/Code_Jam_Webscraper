
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <vector>

#define FO(X,Y) for(int X = 0; X < (Y); X++)

using namespace std;

struct Horse
{
	int speed;
	int distance;
};

struct City
{
	Horse horse;
	vector<int> distances;
	bool horseBeenCollected;
};

struct Network
{
	int numberOfCities;
	vector<City> cities;
};

vector<long double> historicBest;

long double recursiveSolve(Network network, int currentCity, int to, Horse horse, vector<int> visitedCitiesByThisHorse)
{
	Network testNetwork;
	Horse testHorse;
	long double bestTime = -1.0f;
	visitedCitiesByThisHorse.push_back(currentCity);
	for (int i = 0; i < network.numberOfCities; i++)
	{
		// if it is a legitimate route
		if (network.cities[currentCity].distances[i] != -1)
		{
			// prevent backtracking
			bool hasVisitedWithThisHorse = false;
			for (int test : visitedCitiesByThisHorse)
			{
				if (test == i)
				{
					hasVisitedWithThisHorse = true;
				}
			}
			if (!hasVisitedWithThisHorse)
			{
				// can current horse reach this place?
				if (horse.distance >= network.cities[currentCity].distances[i])
				{
					testHorse = horse;
					long double horseTime = (network.cities[currentCity].distances[i] / long double(testHorse.speed));
					if (i == to)
					{
						long double testTime = horseTime;
						if (bestTime < 0.0f || testTime < bestTime)
						{
							bestTime = testTime;
						}
					}
					else
					{
						testNetwork = network;
						testHorse.distance -= network.cities[currentCity].distances[i];
						long double testTime = recursiveSolve(testNetwork, i, to, testHorse, visitedCitiesByThisHorse);
						if (testTime >= 0.0)
						{
							testTime += horseTime;
							if (bestTime < 0.0f || testTime < bestTime)
							{
								bestTime = testTime;
							}
						}
					}
				}
			}
				// also try swapping horses, but only if we've not already taken this horse
			if (!network.cities[currentCity].horseBeenCollected)
			{
				// only trade to a faster or more endurant horse
				if (network.cities[currentCity].horse.speed > horse.speed || network.cities[currentCity].horse.distance > horse.distance)
				{
					testHorse = network.cities[currentCity].horse;
					long double horseTime = (network.cities[currentCity].distances[i] / long double(testHorse.speed));
					if (i == to)
					{
						long double testTime = horseTime;
						if (bestTime < 0.0f || testTime < bestTime)
						{
							bestTime = testTime;
						}
					}
					else
					{
						testNetwork = network;
						testNetwork.cities[currentCity].horseBeenCollected = true;
						testHorse.distance -= network.cities[currentCity].distances[i];
						vector<int> newHorseList = vector<int>();
						newHorseList.push_back(currentCity);
						long double testTime;
						// if we've tried using this horse before, just skip and use that result
						if (historicBest[currentCity] > 0.0)
						{
							testTime = historicBest[currentCity];
						}
						else
						{
							testTime = recursiveSolve(testNetwork, i, to, testHorse, newHorseList);
							historicBest[currentCity] = testTime;
						}
						if (testTime >= 0.0)
						{
							testTime += horseTime;
							if (bestTime < 0.0f || testTime < bestTime)
							{
								bestTime = testTime;
							}
						}
					}
				}
			}
		}
	}

	return bestTime;
}

void solve(istream& in, ostream& out)
{
	Network network;
	int totalTests;
	in >> network.numberOfCities;
	in >> totalTests;

	for (int i = 0; i < network.numberOfCities; i++)
	{
		City city;
		city.horseBeenCollected = false;
		in >> city.horse.distance;
		in >> city.horse.speed;
		network.cities.push_back(city);
	}
	for (int i = 0; i < network.numberOfCities; i++)
	{
		for (int j = 0; j < network.numberOfCities; j++)
		{
			int d;
			in >> d;
			network.cities[i].distances.push_back(d);
		}
	}

	Horse badHorse;
	badHorse.distance = 0;
	badHorse.speed = 1;
	char output[512];
	for (int i = 0; i < totalTests; i++)
	{
		if (i != 0)
		{
			out << " ";
			cout << " ";
		}
		int from;
		int to;
		in >> from;
		in >> to;
		historicBest = vector<long double>();
		for (int j = 0; j < network.numberOfCities; j++)
		{
			historicBest.push_back(-1.0);
		}
		long double value = recursiveSolve(network, from - 1, to - 1, badHorse, vector<int>());
		sprintf_s(output, 500, "%0.6f", value);
		out << output;
		cout << output;
	}
}

void main()
{
	ifstream in = ifstream("C-small-attempt1.in");
	ofstream out = ofstream("C-small-attempt1.out");

	int numberOfCases;
	in >> numberOfCases;

	for (int i = 0; i < numberOfCases; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		out << "Case #" << i + 1 << ": ";
		solve(in, out);
		cout << endl;
		out << endl;
	}

	in.close();
	out.close();
}


