#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
	string inFile(argv[1]);
	string outFile(inFile + ".out");
	ifstream in(inFile);
	ofstream out(outFile);

	int ts; in >> ts;
	for (int t = 1; t <= ts; ++t)
	{
		double d; in >> d;
		int n; in >> n;
		double mxtime = 0;
		for (int i = 0; i < n; i++)
		{
			double k, s; in >> k >> s;
			mxtime = max(mxtime, (d - k) / s);
		}
		out << "Case #" << t << ": " << fixed << setprecision(18) << d / mxtime << endl;
	}
	return 0;
}
