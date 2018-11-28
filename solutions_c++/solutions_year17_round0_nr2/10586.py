#include <iostream>
#include <fstream>
#include <stack>
using namespace std;
bool isNon_Dec(int n)
{
	stack<int> ss;
	int rem=-1;
	if (n < 10)
	{
		return true;
	}
	else
	{
		while (n != 0)
		{
			rem = n % 10;
			ss.push(rem);
			n = n / 10;
		}
		while (ss.size()!=1)
		{
			int vr = ss.top();
			ss.pop();
			if (vr > ss.top())
			{
				return false;
			}
		}
		return true;
	}
}
void main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("out.txt");
	stack<int> s;
	int a,b,c;
	fin >> a;
	if (a <= 100 && a >= 1)
	{
		for (int i = 1; i <= a; i++)
		{
			fin >> b;
			if (b <= 1000 && b >= 1)
			{
				for (int j = 1; j <= b; j++)
				{
					if (isNon_Dec(j))
					{
						s.push(j);
					}
				}
				c = s.top();
				fout << "Case #" << i << ": " << c << endl;
			}
		}
	}
	system("pause");
}