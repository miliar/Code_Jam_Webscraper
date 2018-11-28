#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int N, K;
typedef struct {
	long R, H;
} t_rh;
vector<t_rh> rh;

bool compare(const t_rh &a, const t_rh &b)
{
    return a.R > b.R;
}

vector<int> c;
vector<double> maxarea;

void get(int n, int k)
{
	if(k == 0)
	{
//		cout << "D: "; for(int i = 0; i<c.size(); i++) cout << c[i] << " "; cout << endl;

		double all = 0;
		double u1 = 0;
		for(int i = c.size()-1; i>=0; i--)
		{
//			cout << "R, H: " << rh[c[i]].R << ", " << rh[c[i]].H << endl;
			double u = M_PI*rh[c[i]].R*rh[c[i]].R;
			double h = 2.0*M_PI*rh[c[i]].R*rh[c[i]].H;
			if(i==c.size()-1)
				all = all + u + h;
			else
				all = all + u + h - u1;
			u1 = u;
		}
		maxarea.push_back(all);

		return;
	}
	for(int i = n; i<=rh.size()-1; i++)
	{
		c.push_back(i);
		get(i+1, k-1);
		c.pop_back();
	}
}

double calc()
{
	double ret = 0;
	int k = K;

	get(0, k);

	ret = *max_element(maxarea.begin(), maxarea.end());

	return ret;
}

int main(int argc, char** argv)
{
	string line;
	getline(cin, line);

	istringstream ss(line);

	int T;
	ss >> T;

	for(int i=0; i<T; i++)
	{
		getline(cin, line);
		istringstream iss(line);

		iss >> N;
		iss >> K;
		for(int j = 0; j<N; j++)
		{
			getline(cin, line);
			istringstream iss(line);
			long R;
			long H;
			iss >> R;
			iss >> H;
			t_rh t; t.R=R; t.H=H;
			rh.push_back(t);
		}

		sort(rh.begin(), rh.end(), compare);

		double res = calc();

		cout << "Case #" << i+1 << ": " << fixed << setprecision(9) << res << endl;

		maxarea.clear();
		rh.clear();
	}

	return 0;
}

