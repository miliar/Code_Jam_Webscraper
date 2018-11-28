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

int main(int argc, char* argv[])
{

	fstream In("b-large.in", ios::in);
	fstream Out("b-large.out", ios::out);

	int cases;
	In >> cases;

	for (int h = 0; h < cases; h++)
	{
		int N;
		vector<int> colors(6, 0);
		// R, O, Y, G, B, V;
		In >> N;
		//>> R >> O >> Y >> G >> B >> V;
		for (int i = 0; i < 6; i++)
			In >> colors[i];

		Out << "Case #" << (h + 1) << ": ";

		string ret = "";
		int prevIndex = -1;
		string colorList = "ROYGBV";

		// prep for mixed colors
		colors[0] -= colors[3];
		colors[2] -= colors[5];
		colors[4] -= colors[1];

		if ((colors[0] <= 0 && colors[3]>0) || (colors[2] <= 0 && colors[5] > 0) || (colors[4] <= 0 && colors[1] > 0))
		{
			int sum = 0;
			for (int i = 0; i < colors.size(); i++)
				sum += colors[i];

			if (colors[1] == sum)
			{
				string ret = "";
				for (int i = 0; i < sum; i++)
					ret += "OB"; 
				Out << ret << endl;
				continue;
			}
			else if (colors[3] == sum)
			{
				string ret = "";
				for (int i = 0; i < sum; i++)
					ret += "GR";
				Out << ret << endl;
				continue;
			}

			else if (colors[5] == sum)
			{
				string ret = "";
				for (int i = 0; i < sum; i++)
					ret += "VY";
				Out << ret << endl;
				continue;
			}

			Out << "IMPOSSIBLE" << endl;
			continue;
		}

		N = colors[0] + colors[2] + colors[4];
		for (int i = 0; i < N; i++)
		{
			int curIndex = -1;
			int curCount = 0;
			for (int j = 0; j < colors.size(); j+=2)
				if (j != prevIndex && colors[j] > curCount)
				{
					curCount = colors[j];
					curIndex = j;
				}
			if (curIndex == -1)
			{
				cout << "Current string: " << ret << endl
					<< "Nothing left to place" << endl;
				ret = "IMPOSSIBLE";
				break;
			}
			ret += colorList[curIndex];
			colors[curIndex]--;
			if (prevIndex == -1)
			{
				swap(colors[curIndex], colors[0]);
				swap(colorList[curIndex], colorList[0]);
				curIndex = 0;
			}
			prevIndex = curIndex;
		}

		if (ret != "IMPOSSIBLE")
		{
			if (colors[1] > 0) // O, needs to pair with B
			{
				string replaceString = "";
				for (int i = 0; i < colors[1]; i++)
					replaceString += "BO";
				int Bindex = 0;
				while (ret[Bindex] != 'B')
					Bindex++;
				ret.insert(Bindex, replaceString);
			}
			if (colors[3] > 0) // G, needs to pair with R
			{
				string replaceString = "";
				for (int i = 0; i < colors[3]; i++)
					replaceString += "RG";
				int Bindex = 0;
				while (ret[Bindex] != 'R')
					Bindex++;
				ret.insert(Bindex, replaceString);
			}

			if (colors[5] > 0) // V, needs to pair with Y
			{
				string replaceString = "";
				for (int i = 0; i < colors[5]; i++)
					replaceString += "YV";
				int Bindex = 0;
				while (ret[Bindex] != 'Y')
					Bindex++;
				ret.insert(Bindex, replaceString);
			}


		}
		if (ret[0] == ret[ret.size() - 1])
			ret = "IMPOSSIBLE";
		Out << ret << endl;
	}

	return 0;
}

