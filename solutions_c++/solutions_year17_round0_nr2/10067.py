#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int sheep(int n)
{
	int A[10];
	for (int i = 0;i < 10;i++) A[i] = 0;

	if (n == 0) return -1;

	else {
		int c = 1;
		int norig = n;
		while (true)
		{
			n = c*norig;
		
			for (int i = 0;i < 10;i++)
			{
				int n1 = n;
				int d = 0;
				while (n1 > 0)
				{
					d = n1 % 10;
					n1 = n1 / 10;
					if (d == i)
					{
					
						A[i] = 1;
					}

				}
				bool sleep = true;
				for (int j = 0;j < 10;j++)
				{

					if (A[j] == 0)
					{
						sleep = false;
							break;
					}

				}
				if (sleep) return  n;

				
			}

			c++;
		}

	}

}


int pancakes(string s)
{
	int flips = 0;
	while (true)
	{

		for (int i = 0;i < s.length();i++)
		{


		}


	}
	return flips;

}


int tidy(unsigned long long n)
{

	
	for (unsigned long long i = n;i >= 1;i--)
	{
		string a = to_string(i);
		bool sorted = true;
		for (int j = 0;j<a.length()-1;j++)
		{
			if (a[j + 1] < a[j]) { sorted = false;break; }

		}
		if (sorted) return i;


	}




}


int main()
{
	ifstream in;
	ofstream out;
	string dir = "C:\\Users\\Hussein\\Documents\\Visual Studio 2015\\Projects\\codejam_prac\\sheep.txt";
	in.open(dir);
	dir = "C:\\Users\\Hussein\\Documents\\Visual Studio 2015\\Projects\\codejam_prac\\tidysol.txt";
	out.open(dir);

	if (in) {
		int a;
		in >> a;
		unsigned long long cases;
		for(int i=1;i<=a;i++)
		{

			in >> cases;
			out << "Case #" << i << ": ";
			int result = tidy(cases);

			 out << result << endl;


		}
	}
	in.close();
	out.close();


}

