#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large(9)";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}



int main()
{	
	init();	

	int tst;
	cin >> tst;

	for (int cas = 1; cas<=tst; cas++)
	{
		
		double d;
		long long n;
		cin >> d >> n;
		vector <pair <double, double> > h;

		for (int i=0;i<n;i++)
		{
			double k,s;
			cin >> k >> s;
			h.push_back(make_pair(k,s));
		}
		sort(all(h));
		double res = 0;
		double mxtime = 0;
		for (int i=sz(h)-1;i>=0;i--)
		{
			double tm = (d-h[i].first)/h[i].second;
			mxtime = max(tm,mxtime);		
		}


		
		
		printf("Case #%d: %.9lf\n",cas,d/mxtime);
		//if (!ok) printf("Case #%d: IMPOSSIBLE\n",cas); else
//		printf("Case #%d: %s\n",cas,res.c_str());
	}
	

	return 0;
}