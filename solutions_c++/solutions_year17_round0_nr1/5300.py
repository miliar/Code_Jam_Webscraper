#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>

using namespace std;

int CalculateMinFlips(string&, int);

int main(){
	ifstream in("input.txt");
  	ofstream out("output.txt");
  
  	string pancakeLine;
  	int nRighe;
  	in >> nRighe;

  	for(int i = 0; i < nRighe; i++)
  	{
  		int widthFlipper;
  		in >> pancakeLine;
  		in >> widthFlipper;

  		int res = CalculateMinFlips(pancakeLine, widthFlipper);

  		if(res != -1)
  			out << "Case #" << i + 1 << ": " << res << endl;
  		else
  			out << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
  	}
  
  	return 0;
}

int CalculateMinFlips(string &line, int width)
{
	int flips = 0;

	for(int i = 0; i < line.length() - width + 1; i++)
	{
		if(line[i] == '-')
		{
			for(int j = i; j < i + width; j++)
			{
				if(line[j] == '-')
					line[j] = '+';
				else
					line[j] = '-';
			}
			flips++;
		}
	}

	for(int i = 0; i < line.length(); i++)
		if(line[i] == '-')
			return -1;

	return flips;
}