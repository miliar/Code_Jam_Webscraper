#include <iostream>  
#include <fstream>
#include<vector>
using namespace std;

void main()
{
	long long int t, n, m, i;
	vector<int> num;
	vector<int> tidy_num;
	char temp[100];

	ifstream inFile("B-small-attempt1.in");
	ofstream outFile("test.txt");

	inFile.getline(temp, 100);
	t = atoi(temp);

	for (m = 1; m <= t; ++m)
	{
		inFile.getline(temp, 100);
		n = atoi(temp);
		while (n != 0)
		{
			num.push_back(n % 10);
			n /= 10;
		}
		reverse(num.begin(), num.end());
		
		for (i = 0; i < num.size(); i++)
		{
			tidy_num.push_back(9);
		}

		tidy_num[0] = num[0];

		i = 1;

		if (i == num.size())
		{
			goto outside;
		}

		while (1)
		{
			if (num[i] >= tidy_num[i - 1])
			{
				tidy_num[i] = num[i];
				i++;
				if (i== num.size())
					break;
			}
			else 
			{
				while (1)
				{
					if ((i- 1 == 0) || (tidy_num[i - 1] - 1 >= tidy_num[i - 2]) )
					{
						tidy_num[i - 1]--;
						goto outside;
					}
					else
					{
						i--;
					}
				}
			}
		}
		outside:

		for (; i < num.size(); i++)
			tidy_num[i] = 9;

		long long int tn = 0,s =1;

		for (i = tidy_num.size()-1; i >= 0; i--)
		{
			tn += s* tidy_num[i];
			s *= 10;
		}
		tidy_num.clear();
		num.clear();
		//cout << "Case #" << m << ": " << tn <<endl;
		outFile << "Case #" << m << ": " << tn << endl;
	}
}