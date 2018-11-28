#include<iostream>
#include<fstream>
#include<string>
#include<iterator>
#include<map>
#include<queue>
#include<vector>
#include<cmath>
#include <iomanip>
using namespace std;

int main()
{
	string line;
	ifstream inFile("A-large.in");
	ofstream outFile("output_problem1_large.out");
	int testCases;
	if (inFile.is_open())
	{
		getline(inFile, line);
		testCases = stoi(line);
		long long D, N, Ki, Si, min_speed, slowest_hourse;
		for (int i = 0; i < testCases; i++){
			
			inFile >> D >> N;
			
			double maxTime;
			for (int j = 0; j < N; j++)
			{
				inFile >> Ki >> Si;

				double numOfKilos = D - Ki;
				double Time = numOfKilos / Si;

				if (j == 0){
					min_speed = Si;
					slowest_hourse = Ki;
					maxTime = Time;
				}
				if (Time > maxTime)
					maxTime = Time;
				/*if (Si < min_speed && Ki < D)
				{
					min_speed = Si;
					slowest_hourse = Ki;
				}*/
			}
		    
			double AnneSpeed = D / maxTime;
			//AnneSpeed = floor(1000000 * AnneSpeed) / 1000000;
			if (outFile.is_open())
			{
				outFile << "Case #" << i + 1 << ": " << fixed << setprecision(6)<<AnneSpeed << endl;

			}

		}
		outFile.close();
		inFile.close();
	}
	return 0;
}

