//#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

typedef long long ll;

#define M_PI 3.1415926535897932384626433832795

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");
	output << std::fixed;
	output << std::setprecision(10);
	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;

	//string s;
	int ac, aj;
	


	for (int t = 0; t < T; ++t)
	{
	
		input >> ac >> aj;
		vector<int> c;
		vector<int> d;
		vector<int> j;
		vector<int> k;

		int tmp1, tmp2;
		for (int i = 0; i < ac; ++i)
		{
			input >> tmp1 >> tmp2;
			c.push_back(tmp1);
			d.push_back(tmp2);
		}
		for (int i = 0; i < aj; ++i)
		{
			input >> tmp1 >> tmp2;
			j.push_back(tmp1);
			k.push_back(tmp2);
		}


		int ans;

		if (ac + aj == 1)
		{
			ans = 2;
		}
		else
		{
			if (ac == 1)
			{
				ans = 2;
			}
			else
			{
				int b1, b2, e1, e2;
				if (ac == 2)
				{
					if (c[0] < c[1])
					{
						b1 = c[0];
						b2 = c[1];
						e1 = d[0];
						e2 = d[1];
					}
					else
					{
						b1 = c[1];
						b2 = c[0];
						e1 = d[1];
						e2 = d[0];
					}

				}
				else
				{
					if (j[0] < j[1])
					{
						b1 = j[0];
						b2 = j[1];
						e1 = k[0];
						e2 = k[1];
					}
					else
					{
						b1 = j[1];
						b2 = j[0];
						e1 = k[1];
						e2 = k[0];
					}
				}


				{
					if (b2 - e1 >= 720)
					{
						ans = 2;
					}
					else if (b1 + 24 * 60 - e2 >= 720)
					{
						ans = 2;
					}
					else
					{
						ans = 4;
					}
				}
			}
		}

		output << "Case #" << t + 1 << ": " << ans << endl;



	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
