#include <iostream>  
#include <fstream>

using namespace std;

void main()
{
	long long int t, m,n, people;

	char temp[100];

	ifstream inFile("C-large.in");
	ofstream outFile("test.txt");

	inFile.getline(temp, 100);
	t = atoi(temp);

	n = 0;
	people = 0;

	for (m = 1; m <= t; ++m)
	{
		bool flag = false;
		char ch;

		while (inFile.get(ch))
		{
			if (ch == '\n')
				break;
			else if (ch == ' ')
			{
				flag = true;
			}
			else if (ch != ' ' && !flag)
			{
				n = n * 10 + (ch - '0');
			}
			else if (ch != ' ' && flag)
			{
				people = people * 10 + (ch - '0');
			}
		}

		while (1)
		{
			if (people == 1)
				break;
 			else if(n %2 == 0 && people %2 ==1)
			{
				n /= 2;
				n -= 1;
				people /= 2;
			}
			else
			{
				n /= 2;
				people /= 2;
			}
		}
		if (n % 2 == 1)
		{
			//cout << "Case #" << m << ": " << n / 2 << " " << n / 2 << endl;
			outFile << "Case #" << m << ": " << n / 2 << " " << n / 2 << endl;
		}
		else
		{
			//cout << "Case #" << m << ": " << n / 2 << " " << n / 2 -1<< endl;
			outFile << "Case #" << m << ": " << n / 2 << " " << n / 2 -1<< endl;
		}

		n = 0;
		people = 0;
	}
}