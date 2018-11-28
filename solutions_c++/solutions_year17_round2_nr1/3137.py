#include <stdio.h>
#include <iostream>
#include <math.h>
#include <cmath>
#include <algorithm>
#include <limits>
#include <iomanip>
using namespace std;

struct horse{
	int k, s;
};

bool cmp(horse a, horse b)
{
	if(a.k > b.k)
		return true;
	else if(a.k < b.k)
		return false;
	else
	{
		if(a.s>b.s)
			return false;
		return true;		
	}
}

int main()
{
	int T, D, N;
	horse h[1000];
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>D>>N;
		int k, s;
		int index=0;
		for(int n=0;n<N;n++)
		{
			cin>>k>>s;
			if(k<D)
			{
				h[index].k=k;
				h[index].s=s;
				index++;
			}
		}
		sort(h, h+index, cmp);
		
		double t=(double)(D-h[0].k)/((double)h[0].s);
		for(int n=1;n<index;n++)
		{
			double slower=(double)(D-h[n].k)/t;
			if(slower>h[n].s)
			{
				t=(double)(D-h[n].k)/((double)h[n].s);
			}
		}
		double speed=(double)D/t;
		cout<<fixed<<setprecision(6)<<"Case #"<<i<<": "<<speed<<endl;
	}
	return 0;
}
