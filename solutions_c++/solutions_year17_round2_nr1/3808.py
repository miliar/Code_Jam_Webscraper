// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cmath>

#define rep(i, a, b) for (int i=a;i<b;i++)

using namespace std;

int main()
{
	ifstream reader("input.txt");
	ofstream writer("output.txt");
	int T;
	reader >> T;
	rep(Ti, 0, T) {
		int N;
		double P, S, D;
		double ans = 0;
		reader >> D >> N;
		rep(i, 0, N)
		{
			reader >> P >> S;
			ans = max(ans, (D - P) / S);
		}
		writer.precision(6);
		writer << "Case #" << fixed << Ti + 1 << ": " << D/ans << endl;
	}

	system("pause");
	return 0;
}

