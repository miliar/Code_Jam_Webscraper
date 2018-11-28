#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <iomanip>

using namespace std;

double CalculateTime(double finish);

vector<double> initialPositions;
vector<double> maxSpeeds;


int main(){
	ifstream in("input.txt");
  	ofstream out("output.txt");

  	int nRighe;
  	in >> nRighe;

  	for(int i = 0; i < nRighe; i++)
  	{
  		initialPositions.clear();
  		maxSpeeds.clear();

  		int finish, horses;
  		in >> finish >> horses;

  		for(int j = 0; j < horses; j++)
  		{
  			int iP, mS;
  			in >> iP >> mS;
  			initialPositions.push_back(iP);
  			maxSpeeds.push_back(mS);

  		}

  		double speed = CalculateTime(finish);

  		out << "Case #" << i+1 << ": " << fixed << std::setprecision(6) << speed << endl;
  	}
  
  	return 0;
}

double CalculateTime(double finish)
{
	double currentTime = 0;

	for(int i = 0; i < initialPositions.size(); i++)
	{
		double timeToFinish = (finish - initialPositions[i]) / maxSpeeds[i];

		if(timeToFinish > currentTime)
			currentTime = timeToFinish;
	}
	
	double finalMaxSpeed = finish / currentTime;
	return finalMaxSpeed;
}
