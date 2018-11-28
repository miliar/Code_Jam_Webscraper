#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <stdio.h>
#define lld long long int
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
    	lld dest;
    	int n;
    	cin>>dest>>n;
    	vector< pair<lld,lld> >data;
    	for(int a=0;a<n;a++)
    	{
    		lld pos,vel;
    		cin>>pos>>vel;
    		data.push_back(make_pair(pos,vel));
    	}
    	float time[n];
    	for(int a=0;a<n;a++)
    	{
    		if(data[a].first<dest)
    			time[a]=(dest-data[a].first)/(data[a].second*1.0);
    		else
    			time[a]=0;
    	}
    	float req=0;
    	for(int a=0;a<n;a++)
    	{
    		if(time[a]>req)
    			req=time[a];
    	}
    	if(req!=0)
    	printf("Case #%d: %.6f\n",test,dest*1.0/req);
    	else
    	printf("Case #%d: 0.000000\n",test);
    }
}