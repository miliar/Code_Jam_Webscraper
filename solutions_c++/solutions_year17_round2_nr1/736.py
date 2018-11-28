#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <set>
#include <iomanip>

using namespace std;

void solve(double d, int n, const vector<pair<double, double> >& horses, int c, ofstream& out)
{
    out<<"Case #"<<c<<": ";
	double ans=-1;
	for (int i=0; i<n; ++i)
	{
	    double t=(d-horses[i].first)/horses[i].second;
		double tmp_ans=d/t;
		if (tmp_ans<ans || ans==-1)
			ans=tmp_ans;
	}
	out<<setprecision(6)<<fixed<<ans<<"\n";
}

int main()
{
    ifstream in("A-large.in");
	ofstream out("output.txt");
    int t;
	in>>t;
	int i=1;
	while (t--)
	{
	    double d;
		int n;
		in>>d>>n;
		vector<pair<double, double> > horses(n);
		for (int i=0; i<n; ++i)
			in>>horses[i].first>>horses[i].second;
	    solve(d, n, horses, i, out);
		++i;
	}
	return 0;
}