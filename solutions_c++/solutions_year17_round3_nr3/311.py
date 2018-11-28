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

string problem_name = "C-small-1-attempt0(1)";

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
		

		double res = 1;
		vector <double> val;
		int n,k;
		cin >> n >> k;
		double u;
		cin >> u;
		for (int i=0;i<n;i++)
		{
			double t;
			cin >> t;
			val.push_back(t);
		}

		sort(all(val));
		val.push_back(1);
		
		for (int i=1;i<=n;i++)
		{
			double need = 0;
			double sum = 0;
			for (int j=0;j<i;j++) {
				sum+=val[j];
				need+=val[i]-val[j];
			}
			if (need>u)
			{
				for (int j=0;j<i;j++)
					val[j] = (sum+u)/i;

				res = val[0];
				for (int j=1;j<n;j++)
					res*=val[j];
				break;

			}
			
		
		}	
	
	

		printf("Case #%d: %.9lf\n",cas,res);
		
		
		//printf("Case #%d: IMPOSSIBLE\n",cas);
		
	}
	

	return 0;
}