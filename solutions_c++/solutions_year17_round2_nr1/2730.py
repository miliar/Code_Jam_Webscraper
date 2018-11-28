// Round12016.cpp : Defines the entry point for the console application.
//


#include<iostream>
#include<fstream>
#include<string>
#include <algorithm>
using namespace std;
int ingredients[50];
int packages[50][50][2];
char c[20];
char j[20];
int solveProblem(int n,int p)
{
	int count=0;
	
	return count;
}
int main(int argc, char*argv[])
{
	ifstream inputFile;
	FILE* fout;
	
	string line;
	int numValues;
	double result;
	inputFile.open("input.txt");
	fout = fopen("output.txt", "w");
	if (inputFile.is_open())
	{
		inputFile>>numValues;
		for (int numCase = 1; numCase <= numValues; numCase++) {
			double numKm;
			double numHorses;
			
			inputFile >> numKm>>numHorses;
			double speed, inPos;
			double maxTime=0.0;
			for (int i = 0; i < numHorses; i++)
			{
				inputFile >> inPos >> speed;
				if (((numKm - inPos) / speed) > maxTime)
				{
					maxTime = (numKm - inPos) / speed;
				}
			}
			fprintf(fout, "Case #%d: %Lf\n", numCase, numKm / maxTime);
			
			
			
		}
		
	}
	fclose(fout);
    return 0;
}
