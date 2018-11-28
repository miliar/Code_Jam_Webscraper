#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <climits>
#include <map>
#include <set>
#include <bitset>
#include <iomanip>
#define mod 1000000007
#define lli long long int
using namespace std;
bool mycmp(pair<double,double> &a,pair<double,double> &b)
{
       if(a.first > b.first)
       return true;
       else 
       return false;
}
double myfunc(vector<pair<double,double> > &v,int n,double d)
{
    double time=0,res,distance,t;
	for(int i=0;i<n;i++)
	{
		distance=d-v[i].first;
		t=distance/v[i].second;
		if(t>=time)
			time=t;
	}
	res=d/time;
	return res;
}
int main()
{
	int t,counter=1;
	scanf("%d",&t);
	while(t--)
	{
		double d;
		int n;
		cin >> d;
		scanf("%d",&n);
		vector<pair<double ,double> >v;
		for(int i=0;i<n;i++)
		{
			double x;
			double y;
			cin >> x >> y;
			pair<double,double> temp;
			temp.first=x;
			temp.second=y;
			v.push_back(temp);
		}
		sort(v.begin(),v.end(),mycmp);
		double ans = myfunc(v,n,d);
	    printf("Case #%d: ",counter);
	    cout << fixed ;
		cout << setprecision(6) << ans << endl;
		counter+=1;
	}
}
				
