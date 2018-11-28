#include<iostream>
#include<fstream>

using namespace std;

void main()
{
	ifstream infile;
	ofstream outfile;
	long n;//number
	int t;// number of test cases

	int y;//last tidy number counted
	int last;
	bool found = false;
	int first;
	int copy;
	infile.open("B-small-attempt0.in");
	outfile.open("output.txt");
	infile >> t;
	for (int i = 1; i <= t; i++)
	{
		
		infile >> n;
		do
		{
			found = false;
			copy = n;
			last = copy % 10;
			copy /= 10;
			while (copy > 0)
			{
				first = copy % 10;
				copy /= 10;
				if (last < first)
				{
					found = true;
					break;
				}
				last = first;
			}
			if (found != true)
			{
				outfile << "Case #" << i<<": "<<n << endl;
				break;
			}
			n--;
		} while (n > 0);
	}
	outfile.close();
	infile.close();
	
	system("pause");
}