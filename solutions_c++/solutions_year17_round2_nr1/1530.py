#include <iostream>
#include <fstream>
#include <iomanip> 

using namespace std;

int main() {
	int T;
	ifstream file1("A-large.in");
	ofstream file2("1.out");
	file2 << setiosflags(ios::fixed);
	file1 >> T;
	for (int i = 0; i < T; i++)
	{
		double D, K,maxt=0;
		file1 >> D >> K;
		for (int j = 0; j < K; j++)
		{
			double x, y;
			file1 >> x >> y;
			if ((D - x) / y > maxt)
				maxt = (D - x) / y;
		}
		file2 << setprecision(6) << "Case #" << i + 1 << ": " << D / maxt << endl;
	}
	return 0;
}