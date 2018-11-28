//#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <cfloat>

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
	int n, k;
	double u;



	for (int t = 0; t < T; ++t)
	{
		input >> n >> k;
		input >> u;
		vector<double> cores(n);
		for (int i = 0; i < n; ++i)
		{
			input >> cores[i];
		}

		sort(cores.begin(), cores.end());

		while (u > 0 && abs(cores[0] - 1) > DBL_EPSILON)
		{
			int left = 0;
			int right = 1;

			while (right < n && abs(cores[left] - cores[right]) < DBL_EPSILON)
			{
				++right;
			}

			double diff = 0;

			if (right == n)
			{
				for (int i = 0; i < right; ++i)
				{
					diff += min(1 - cores[i], u / right);
					cores[i] += min(1 - cores[i], u / right);
				}
				u -= diff;
			}
			else
			{
				for (int i = 0; i < right; ++i)
				{
					diff += min(cores[right] - cores[i], u / right);
					cores[i] += min(cores[right] - cores[i], u / right);
				}
				u -= diff;
			}
		}

		double ans = 1;
		for (int i = 0; i < n; ++i)
		{
			ans *= cores[i];
		}

		output << "Case #" << t + 1 << ": " << ans << endl;



	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
