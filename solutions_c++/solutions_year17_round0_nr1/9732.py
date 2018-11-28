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


int pancakes(string s,int k)
{
	int flips = 0;
	bool happy = true;
		for (int i = 0;i < s.length();i++)
		{
			if (s[i] == '-') {
				happy = false;
				break;
			}
		}
		if (happy) return -1;

		for (int i = 0; i <= s.length()-k  ;i++)
		{
			
			if (s[i] == '-') {
				for (int j = i;j < i + k;j++) // now flip
				{
					if (s[j] == '-') s[j] = '+';
					else if (s[j] == '+') s[j] = '-';

				}
				flips++;

			}

			}
		
		 happy = true;
		for (int i = 0;i < s.length();i++)
		{
			if (s[i] == '-') {
				happy = false;
				break;
			}
		}
		if (happy) return flips;
		else return 0;


	
	return flips;

}


string tidy(string a)
{
			bool sorted = true;
			for (int j = 0;j < a.length() - 1;j++)
			{
				if (a[j + 1] < a[j]) {
					sorted = false;break;
				}

			}
				if (sorted) return a;
			
				while (true)
				{


					for (int j = 0;j < a.length() - 1;j++)
					{



						if (a[j + 1] < a[j])
						{
							if (a[j] == '0')
							{

							}
							else {
								char c = a[j] - 1;
								a[j] = c;
								for (int k = j + 1;k < a.length();k++)
								{
									a[k] = '9';
								}
								bool sorted = true;
								for (int j = 0;j < a.length() - 1;j++)
								{
									if (a[j + 1] < a[j]) {
										sorted = false;break;
									}

								}
								if (sorted) return a;
							}
						}




					}

					bool sorted = true;
					for (int j = 0;j < a.length() - 1;j++)
					{
						if (a[j + 1] < a[j]) {
							sorted = false;break;
						}

					}
					if (sorted) return a;

				}


}

//string stall(int n, int k)
//{
//
//	int *B = new int(n);
//	for (int i = 0;i < n;i++)
//	{
//		B[i] = 0;
//	}
//	for (int i = 0;i < k;i++)
//	{
//
//
//
//
//	}
//
//}





int main()
{
	ifstream in;
	ofstream out;
	string dir = "C:\\Users\\Hussein\\Documents\\Visual Studio 2015\\Projects\\codejam_prac\\input.txt";
	in.open(dir);
	dir = "C:\\Users\\Hussein\\Documents\\Visual Studio 2015\\Projects\\codejam_prac\\panckagesol.txt";
	out.open(dir);

	if (in) {
		int a;
		in >> a;
		string cases;
		for(int i=1;i<=a;i++)
		{
			int k;
			in >> cases;
			in >> k;
			out << "Case #" << i << ": ";
			int result = pancakes(cases,k);
			if (result == -1)
				out << "0" << endl;
			else if (result == 0)
				out << "IMPOSSIBLE" << endl;
			else out << result << endl;
			

		}
	}
	in.close();
	out.close();


}

