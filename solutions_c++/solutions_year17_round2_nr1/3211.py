//============================================================================
// Name        : zadanie2.cpp
// Author      : Draxar
// Version     :
// Copyright   : Your copyright notice
// Description :
//============================================================================

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int num;
	cin>>num;

	for(int i=1;i<=num;i++)
	{
		double destiny;
		double slowestTime=0;
		int horses;

		cin>>destiny>>horses;
		for (int j=0;j<horses;j++)
		{
			double dist, speed, timeNeeded;
			cin>>dist>>speed;
			dist=destiny-dist;
			timeNeeded=dist/speed;
			if(timeNeeded>slowestTime)slowestTime=timeNeeded;
		}
		double topSpeed=destiny/slowestTime;
		cout<<"Case #"<<i<<": "<<fixed<< setprecision(6) << topSpeed<<"\n";
	}
}
