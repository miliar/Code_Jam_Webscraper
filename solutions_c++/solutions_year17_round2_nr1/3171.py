#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

typedef unsigned long long ull;

int main(int argc, char const *argv[])
{	
	string sizes[2] = {"-small", "-large"};

	char prob_num = 'A';
	string data_size = sizes[1];

	string in_name = prob_num + data_size + ".in";
	string out_name = prob_num + data_size + ".out";

	ifstream infile(in_name.c_str());
	string line;
	int T;
	infile >> T;
	getline(infile, line);

	ofstream outfile(out_name.c_str());
	int D, N;
	for (int i = 0; i < T; i++)
	{
		infile >> D >> N;
		double max_speed = 1e14;
		vector<ull> K(N);
		vector<ull> S(N);
		vector<double> t(N);
		for (int j = 0; j < N; j++)
		{
			infile >> K[j] >> S[j];
			t[j] = 1.0 * (D - K[j]) / S[j];
			double speed = 1.0 * D / t[j];
			if (speed < max_speed)
			{
				max_speed = speed;
			}
		}
		cout.setf(ios::showpoint);
		cout.precision(6);
		cout.setf(ios::fixed);
		outfile << "Case #" << i + 1 << ": "
				<< setprecision(6) << setiosflags(ios::fixed | ios::showpoint)
				<< max_speed << endl;
	}

	return 0;
}