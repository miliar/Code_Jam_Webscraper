#include <fstream>
#include <cstring>

using namespace std;

int main(void)
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	
	int t;
	in >> t;
	for(int index = 0; index < t; index++)
	{
		string sequenza;
		int K;
		in >> sequenza >> K;
		
		int counter = 0;
		for(int i = 0; i <= sequenza.size()-K; i++)
		{
			if(sequenza[i] == '-')
			{
				counter++;
				for(int j = 0; j < K; j++)
				{
					if(sequenza[i+j] == '+')
					{
						sequenza[i+j] = '-';
					}
					else
					{
						sequenza[i+j] = '+';
					}
				}
			}
		}
		
		bool control = true;
		for(int i = sequenza.size()-K+1; i < sequenza.size(); i++)
		{
			if(sequenza[i] == '-')
			{
				control = false;
				break;
			}
		}
		
		if(control)
		{
			out << "Case #" << index+1 << ": " << counter << endl;
		}
		else
		{
			out << "Case #" << index+1 << ": IMPOSSIBLE" << endl;
		}
	}
	
	return 0;
}
