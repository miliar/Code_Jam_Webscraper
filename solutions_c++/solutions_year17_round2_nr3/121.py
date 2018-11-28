// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string> 
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <queue>
using namespace std;

struct Horse
{
	int E, S;
};

vector<vector<double> > distances;
vector<Horse> horseList;
vector<vector<double> > distanceMatrix, timeMatrix;

void calculateDistanceMatrix()
{
	for (int k = 0; k < distances.size(); k++)
		for (int i = 0; i < distances.size(); i++)
			for (int j = 0; j < distances.size(); j++)
				distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j]);

	for (int i = 0; i < distances.size(); i++)
	{
		double maxDistance = horseList[i].E;
		for (int j = 0; j < distances.size(); j++)
			if (distances[i][j] > maxDistance)
				distances[i][j] = 1e100;
	}
	
}

double getTime(int start, int end)
{
	priority_queue<pair<double, int> > pq;
	int N = distances.size();
	vector<int> visited(N, 0);

	pq.push(make_pair(0, start));
	
	while (!pq.empty())
	{
		
		int curCity = pq.top().second;
		double curTime = -1*pq.top().first;
		
		pq.pop();
		if (curCity == end)
			return curTime;
		if (visited[curCity])
			continue;
		visited[curCity] = 1;
		double horseSpeed = horseList[curCity].S;

		for (int i = 0; i < N; i++)
			if (!visited[i] && distances[curCity][i] < 1e20)
				pq.push(make_pair(-1*(curTime + distances[curCity][i] / horseSpeed), i));
	}
	return -1;
}

int main(int argc, char* argv[])
{

	fstream In("c-large.in", ios::in);
	fstream Out("c-large.out", ios::out);

	int cases;
	In >> cases;

	for (int h = 0; h < cases; h++)
	{
		int N, Q;
		In >> N >> Q;
		horseList.resize(N);
		distances = vector<vector<double> >(N, vector<double>(N, 0));
		timeMatrix = vector<vector<double> >(N, vector<double>(N, 1e18));
		for (int i = 0; i < N; i++)
			In >> horseList[i].E >> horseList[i].S;

		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
			{
				In >> distances[i][j];
				if (distances[i][j] < -0.5)
					distances[i][j] = 1e100;
			}

		calculateDistanceMatrix();
		
		Out << "Case #" << (h + 1) << ": ";
		
		for (int i = 0; i < Q; i++)
		{
			int start, end;
			In >> start >> end;
			Out << setprecision(8) <<  getTime(start-1, end-1) << " ";
		}


		Out << endl;
	}

	return 0;
}

