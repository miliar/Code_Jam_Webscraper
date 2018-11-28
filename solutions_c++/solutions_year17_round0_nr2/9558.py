#include<iostream>
#include<fstream>
#include<math.h>
#include<cmath>
using namespace std;
int functiondec(uint64_t i)
{
	int len = (log10(i) + 1);
	for (int loop = len-1; loop >=0; loop--)
	{
		int last = i % 10;
		i = i / 10;
		int s_last = i % 10;
		if (last <s_last )
		{
			return len-loop;
		}

		
	}
	return 0;
}
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int loop=0;
	uint64_t count = 0;
	fin >> loop;
	for (int i = 0; i < loop; i++)
	{
		fin >> count;
		
		while (count>0)
		{
			
			int no = functiondec(count);
			if (no==0)
			{
				fout << "Case #" << i + 1 <<": "<< count<<endl;
				break;
			}
			else
			{
				if (count % 10 == 0)
					count--;
				else
				{
					
					uint64_t minus = 1;
					for (uint64_t ten = 0; ten < no; ten++)
						minus *= 10;
					count /= minus;
					count *= minus;
				}
			}
		}
		

	}
	//loop>> fin;
	return 0;

}