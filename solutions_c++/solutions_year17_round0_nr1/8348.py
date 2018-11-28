#include<fstream>
#include<iostream>
#include<string>
using namespace std;

int main()
{
	ifstream input;
	ofstream output;
	int test_num;
	input.open("input.in");
	input >> test_num;
	for (int k = 0; k < test_num; k++)
	{
		string surface;
		int flipper_size;
		int flips_count = 0;
		input >> surface;
		input >> flipper_size;

		//solve for flips_count
		for (int i = 0; i < surface.length(); i++)
		{
			//if found blank side, switch this pancake and all adjasoned
			if (surface[i] == '-' && i + flipper_size <= surface.length())
			{
				for (int j = 0; j < flipper_size; j++)
				{
					switch (surface[i + j])
					{
					case '+': surface[i + j] = '-'; break;
					default: surface[i + j] = '+';
					}
				}
				flips_count++;
			}
		}
		
		output.open("output.txt", ofstream::app);
		bool done = true;
		for (int i = 0; i < surface.length(); i++)
		{
			if (surface[i] == '-')
			{
				done = false;
				output <<"Case #"<<k+1<< ": IMPOSSIBLE" << endl;
				break;
			}			
		}
		if (done)
		{
			output << "Case #" << k + 1 << ": "<<flips_count << endl;
		}
		output.close();
	}
}
