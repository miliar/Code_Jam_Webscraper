#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;
#define f(i,x,y) for(int i = x; i < y; ++ i)
typedef long long ll;

struct horse
{
	int kilometer;
	int speed;
	void read()
	{
		cin >> kilometer >> speed;
	}
	double computeAnnieSpeed(double distance)
	{
		return distance/(distance - kilometer) * speed;
	}
} horse[1005];


int main()
{
	int number_of_testcases;
	cin >> number_of_testcases;
	for (int testcase = 1; testcase <= number_of_testcases; ++ testcase)
	{
		cout << "Case #" << testcase << ": ";
		int totalDistance, n;
		cin >> totalDistance >> n;
		f(i, 0, n)
			horse[i].read();
		double minimalSpeed = 1e15;
		f(i, 0, n) minimalSpeed = min(minimalSpeed, horse[i].computeAnnieSpeed(totalDistance));

		cout << fixed << setprecision(8) << minimalSpeed << "\n";
	}
}

