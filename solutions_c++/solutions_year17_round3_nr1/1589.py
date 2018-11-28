#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <cmath>
#include <algorithm>
using namespace std;
const double pi = 3.1415926535897;
long long C(int n, int r) {
	if (r > n / 2) r = n - r; // because C(n, r) == C(n, n - r)
	long long ans = 1;
	int i;

	for (i = 1; i <= r; i++) {
		ans *= n - r + i;
		ans /= i;
	}

	return ans;
}
int main() {
	ifstream inStream;
	ofstream outStream;

	inStream.open("A-large (1).in");
	outStream.open("output.txt");

	int loop;
	inStream >> loop;


	for (int count = 1; count <= loop; count++)
	{
		int N;
		inStream >> N;
		int K;
		inStream >> K;
		vector<pair<double, double>> pancakes(N); //1st is top area, second is side area
		for (int i = 0; i < N; i++)
		{
			double radius;
			inStream >> radius;
			double height;
			inStream >> height;
			pancakes[i].first = pi * pow(radius, 2);
			pancakes[i].second = 2 * pi*radius*height;
		}
		sort(pancakes.begin(), pancakes.end());

		vector<double> areas(N-K+1);
		for (int k = 0; k < N-K+1; k++)
		{
			vector<pair<double, double>> pancakes1 = pancakes;
			double ans = pancakes1[pancakes1.size() - 1 - k].first + pancakes1[pancakes1.size() - 1 -k].second;
			pancakes1[pancakes1.size() - 1 - k].second = 0;
			for (int i = 0; i < pancakes1.size(); i++)
			{
				double temp1 = pancakes1[i].first;
				pancakes1[i].first = pancakes1[i].second;
				pancakes1[i].second = temp1;
			}

			sort(pancakes1.begin(), pancakes1.end());

			for (int i = 0; i < K - 1; i++)
			{
				ans += pancakes1[pancakes1.size() - i - 1].first;
			}
			areas[k] = ans;
		}
		sort(areas.begin(), areas.end());
		cout.setf(ios::fixed);
		outStream.setf(ios::fixed);
		cout.setf(ios::showpoint);
		outStream.setf(ios::showpoint);
		cout.precision(9);
		outStream.precision(9);
		cout << "Case #" << count << ": " << areas[areas.size()-1] << endl;
		outStream << "Case #" << count << ": " << areas[areas.size() - 1] << endl;


	}

	inStream.close();
	outStream.close();

	return(0);
}