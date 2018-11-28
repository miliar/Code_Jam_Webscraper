#include <iostream>
#include <algorithm> 
#include <queue>
#include <vector>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <map>
using namespace std;

struct mode
{
	int k,s;
};

mode horse[1000];
double goal[1000];

double maxs(double a,double b)
{
	if(a>b) return a;
	return b;
}

int main()
{
	int T,x=0,d,n,i,j;
	double max;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&d,&n);
		for(i=0;i<n;i++) scanf("%d%d",&horse[i].k,&horse[i].s);
		for(i=0;i<n;i++)
		{
			goal[i]=((double)d-(double)horse[i].k)/(double)horse[i].s;
			for(j=0;j<i;j++) if(horse[i].k<horse[j].k && goal[i]<goal[j]) goal[i]=goal[j];
		}
		for(i=0,max=0;i<n;i++) max=maxs(max,goal[i]);
		printf("Case #%d: %.6lf\n",++x,(double)d/max);
	}
}
