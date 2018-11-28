#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <utility>
#include <iomanip> 
#include <queue>

using namespace std;

#define pb push_back

#define N 1010

typedef long long ll;


struct Pancake{
	double r, h, a_top, a_side;
};

bool cmp(const Pancake &a, const Pancake &b)	{
	return a.r > b.r;
}

int n, k, t;
vector< double > a_top, a_side, dmax;
vector< vector<double> > d;
vector< Pancake > p;

int main() {

	//freopen("A-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(false);

	cin >> t;
	int testcase = 0;
	while (t--)	{
		cin >> n >> k;
		p = vector<Pancake> (n+1);
		d = vector< vector<double> > (n+1,vector<double>(k+1,0));
		dmax = vector<double> (n+1,0.0);
		
		for (int i = 1; i <= n; i++)
		{
			cin >> p[i].r >> p[i].h;
			p[i].a_top = M_PI*p[i].r*p[i].r;
			p[i].a_side = 2.0*M_PI*p[i].r*p[i].h;
			//cerr << a_top[i] << ' ' << a_side[i] << endl;
		}
		sort(p.begin()+1,p.end(),cmp);
		
		for (int i = 1; i <= n; i++)
		{
			d[i][1] = p[i].a_top + p[i].a_side;
			
			//cerr << dmax[1] << ' ' << a_side[i] << endl;
			
			for (int j = 2; j <= min(i,k); j++)
				d[i][j] = dmax[j-1]+p[i].a_side;
				
			for (int j = 1; j <= min(i,k); j++)
			{	
				dmax[j] = max(dmax[j],d[i][j]);
				//cerr << dmax[j] << ' ';
			}
			//cerr << endl;
		}		
		
		double ans = 0.0;
		for (int i = 1; i <= k; i++)
			ans = max(ans,dmax[i]);
		
		testcase++;
		cout << "Case #" << testcase << ": ";
		cout << setprecision(10) << fixed << ans << endl;
	}

	return 0;
}