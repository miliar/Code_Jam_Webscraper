#include <bits/stdc++.h>
using namespace std;
double area;
		double n,k,r,h;
		vector<pair<double,double> >v;
void Area(double radius,int idx,int selected,double a)
{
	if(selected==k)
	{
		if(a>area)
			area=a;
	}
//	cout<<idx<<" "<<radius<<endl;
	if(radius<v[idx].first&&idx<(int)n)
	Area(v[idx].first,idx+1,selected+1,a-M_PI*radius*radius+M_PI*v[idx].first*v[idx].first+2*M_PI*v[idx].first*v[idx].second);
	if(radius>=v[idx].first&&idx<(int)n)
	Area(radius,idx+1,selected+1,a+2*M_PI*v[idx].first*v[idx].second);	
	if(idx<(int)n)
	Area(radius,idx+1,selected,a);
}
int main()
{
	int t,q=1;
	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		for(int i=0;i<(int)n;i++)
		{
			cin>>r>>h;
			v.push_back(make_pair(r,h));
		}
		stable_sort(v.rbegin(),v.rend());
		area=0;
		Area(0,0,0,0);
		printf("Case #%d: %.9lf\n",q,area);
		q++;
		v.clear();
	}
	return 0;
}