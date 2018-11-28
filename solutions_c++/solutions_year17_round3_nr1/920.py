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
	int n, k;
	int r;
	int h;
	
	

	for (int t = 0; t < T; ++t)
	{
		vector<pair<int, long double>> pancakes;
		input >> n >> k;
		
		for (int i = 0; i < n; ++i)
		{
			input >> r >> h;
			pancakes.push_back(make_pair(r, 2 * M_PI * r * h));
		}

		vector<int> solution;

		std::sort(pancakes.begin(), pancakes.end(), [](const std::pair<int, long double> &left, const std::pair<int, long double> &right) {
			if (left.first < right.first)
				return 1;
			if (left.first == right.first && left.second < right.second)
				return 1;
			return 0;
		});

		long double ans = 0;
		for (int i = 0; i < k; ++i)
		{
			solution.push_back(i);
			ans += pancakes[i].second;
		}
		ans += M_PI * pancakes[k - 1].first * pancakes[k - 1].first;

		for (int i = k; i < n; ++i)
		{
			vector<int> newBestSolution(k);
			long double newBestAns = ans;
			for (int j = 0; j < k; ++j)
			{
				vector<int> solutionCopy(k);
				std::copy(solution.begin(), solution.end(), solutionCopy.begin());
				double copy = ans;
				copy += pancakes[i].second;
				copy += M_PI * pancakes[i].first * pancakes[i].first;

				copy -= pancakes[solutionCopy[j]].second;

				copy -= M_PI * pancakes[solutionCopy[k - 1]].first * pancakes[solutionCopy[k - 1]].first;
				
				if (copy > newBestAns)
				{
					newBestAns = copy;
					solutionCopy.erase(solutionCopy.begin() + j);
					solutionCopy.push_back(i);
					std::copy(solutionCopy.begin(), solutionCopy.end(), newBestSolution.begin());
				}
			}
			if (newBestAns > ans)
			{
				ans = newBestAns;
				std::copy(newBestSolution.begin(), newBestSolution.end(), solution.begin());
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
