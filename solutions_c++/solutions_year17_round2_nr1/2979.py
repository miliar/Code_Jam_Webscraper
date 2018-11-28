#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
	ifstream in;
	ofstream out;
	in.open("in.txt");
	out.open("out.txt");
	int t;
	in >> t;
	for(int pt=1;pt<=t;pt++)
	{
		out.setf(ios::fixed);
		double d,n;
		in >> d >> n;
		vector<pair<double,double> > p;
		vector<double> q;
		for(int e=0;e<n;e++)
		{
			double a,b;
			in >> a >> b;
			p.push_back(make_pair(a,b));
		}
		out.precision(6);
		for(int e=0;e<n;e++)
		{
			q.push_back((d-p[e].first)/p[e].second);
		}
		sort(q.begin(),q.end());
		out <<"Case #"<<pt<<": "<< d/q[q.size()-1] << endl;
	}
}
