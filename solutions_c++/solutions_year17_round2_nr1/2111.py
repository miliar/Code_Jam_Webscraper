#include<fstream>
#include<iomanip>
#include<iostream>
#include<algorithm>

using namespace std;

#define N 1000

struct horse
{
	double s, k;

	bool operator<(const horse& h)
	{
		return this->s < h.s;
	}
};

istream& operator>>(istream& stream, horse& h)
{
	stream >> h.k >> h.s;
	return stream;
}

horse horses[N];

double K[N], S[N];

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	in >> T;

	for (int test_case = 0; test_case < T; test_case++)
	{
		double d, end = 0, result;
		int n;

		in >> d >> n;
		for (int i = 0; i < n; i++)
		{
			//in >> horses[i];
			in >> K[i] >> S[i];
		}

		for (int i = 0; i < n; i++)
		{
			double t = (d - K[i]) / S[i];
			if (end < t) end = t;
		}
		
		result = d / end;
		out << "Case #" << test_case + 1 << ": " << setprecision(20) << result << endl;
	}
}