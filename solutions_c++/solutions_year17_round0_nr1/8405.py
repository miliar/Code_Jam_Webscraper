#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void flip_pancakes(string &pancakes, int indx, int length)
{
	for (int i = 0; i < length; i++)
	{
		if (pancakes[indx + i] == '-') 
		{
			pancakes[indx + i] = '+';
		} 
		else
		{
			pancakes[indx + i] = '-';
		}
	}
}

bool check_pancakes(string &pancakes, int length)
{
	for (int i = pancakes.size() - length + 1; i < pancakes.size(); i++)
	{
		if (pancakes[i] == '-') return false;
	}

	return true;
}

int main()
{

	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");

	int t;
	fin >> t;
	
	for (int i = 1; i <= t; i++)
	{
		string pancakes;
		int k;
		fin >> pancakes >> k;

		int cnt = 0;

		for (int idx = 0; idx <= pancakes.size() - k; idx++)
		{
			if (pancakes[idx] == '-')
			{
				flip_pancakes(pancakes, idx, k);
				cnt++;
			}
		} 		
		
		if (check_pancakes(pancakes, k))
		{
			fout << "Case #" << i <<": " << cnt << endl;
		} else fout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}	
	
	fin.close();
	fout.close();
	return 0;
}
