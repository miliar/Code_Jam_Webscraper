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

string problem_name = "A-large(10)";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

double pi = acos(-1.);
int main()
{	
	init();	

	int tst;
	cin >> tst;

	for (int cas = 1; cas<=tst; cas++)
	{
		

		vector <pair <double, double > > mas;
		int n,k;
		cin >> n >> k;
		for (int i=0;i<n;i++)
		{
			double r,h;
			cin >> r >> h;
			mas.push_back(make_pair(r,h));					
		}
		double res = 0;

		for (int i=0;i<n;i++)
		{
			vector <double> mas2;
			for (int j=0;j<n;j++)
				if (i!=j)
				if (mas[j].first<=mas[i].first)
					mas2.push_back(2*pi*mas[j].first*mas[j].second);
			if (sz(mas2)>=k-1)
			{
				sort(all(mas2));
				reverse(all(mas2));
				double cur = pi*mas[i].first*mas[i].first + 2*pi*mas[i].first*mas[i].second;
				for (int j=0;j<k-1;j++)
					cur+=mas2[j];
				res = max(res,cur);
			}		
			
		}

		
		

		printf("Case #%d: %.9lf\n",cas,res);
		
		
		//printf("Case #%d: IMPOSSIBLE\n",cas);
		
	}
	

	return 0;
}