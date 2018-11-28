#include<fstream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<iomanip>

using namespace std;

#define pi (double)3.14159265358979323846
#define N 1000

struct panc
{
	double side, face;

	//bool operator<(const panc& other)
	//{
	//	return this->side < other.side;
	//}
};

bool comp(const panc& p1, const panc& p2)
{
	if (p1.side == p2.side) return p1.face > p2.face;
	return p1.side > p2.side;
}



static panc pc[N];

void maxr_minh(int k, double& f, double& s)
{
	f = 0;
	s = numeric_limits<double>::infinity();

	for (int i = 0; i < k; i++)
	{
		if (pc[i].face > f)
		{
			f = pc[i].face;
			//s = pc[i].side;
		}
		/*else if (pc[i].face == f && pc[i].side < s)
		{
			s = pc[i].side;
		}*/
	}
	for (int i = 0; i < k; i++)
	{
		if (pc[i].side < s) s = pc[i].side;
	}
}

double get_len(double r)
{
	return (double)2.*/*pi**/(double)r;
}

double get_surface(double r, double h)
{
	return (double)h*(double)get_len(r);
}

ifstream& operator>>(ifstream& stream, panc& p)
{
	double r, h;
	stream >> r >> h;
	p.face = (double)/*pi**/r*r;
	p.side = get_surface(r, h);
	return stream;
}

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	in >> T;
	
	for (int test_case = 0; test_case < T; test_case++)
	{
		int n, k;
		double result = 0, max_face, min_side, temp;

		in >> n >> k;

		for (int i = 0; i < n; i++)
		{
			in >> pc[i];
		}

		sort(&pc[0], &pc[0] + n, comp);

		for (int i = 0; i < k; i++)
		{
			result += pc[i].side;
		}
		maxr_minh(k, max_face, min_side);
		result += max_face;
		temp = max_face + min_side;
		result -= temp;
		for (int i = k; i < n; i++)
		{
			if (temp < pc[i].face + pc[i].side && max_face<pc[i].face) temp = pc[i].face + pc[i].side;
		}
		result += temp;
		result *= pi;

		out << "Case #" << test_case + 1 << ": " << setprecision(20) << result << endl;
	}
}