#include <stdio.h>  
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	ifstream in;
	int c;
	string a;
	int b;
	int x = 1;
	in.open("A-large.in");
	ofstream out("A-large.out");
	in >> c;
	while (c>0) 
	{
		int i = 0;
		int j = 0;
		int h = 0;
		
		in >> a;
		in >> b;
		while (a[i + b - 1] == '+' || a[i + b - 1] == '-')
		{
			if (a[i] == '-')
			{
				int k = 1;
				a[i] = '+';
				while (k < b)
				{
					if (a[i + k] == '+')
						a[i + k] ='-';
					else
						a[i + k] = '+';
					k++;
	
				}
				j++;
			}
			i++;
		}
		while (h < b - 1)
		{
			if (a[i + h] != '+')
				break;
			h++;
		}
		if(h==b-1)
			out <<"Case #"<< x<<": "<<j << "\n";
		else
			out << "Case #" << x << ": " << "IMPOSSIBLE" << "\n";
		c--;
		x++;
		
	}
	in.close();
	out.close();
	getchar();
	getchar();
	return 0;
}