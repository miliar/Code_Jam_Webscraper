#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

typedef struct {
	long double k;
	long double s;
	long double dst;
} Horse;

bool sortfunc(const Horse& a, const Horse& b) {
	return a.k < b.k;
}

int main(int argc, char **argv)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T, d, n;
	vector<Horse> h (1001);;
	long double maxspeed, meetTime, dstTime;
	
	scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
		scanf("%d%d",&d,&n);
		
		for (int i=0;i<n;i++) {
			scanf("%llf%llf",&h[i].k,&h[i].s);
			h[i].dst = d;
		}
		sort(h.begin(),h.begin()+n,sortfunc);
		
		for (int i=n-2;i>=0;i--) {
			for (int j=i+1;j<n;j++) {
				if (h[i].s==h[j].s) continue;
				if (abs(h[i].k-h[j].k) < 0.00000001) {
					h[i].dst = h[j].dst;
					continue;
				}
				if (h[i].s < h[j].s) continue;
				meetTime = ((h[j].k-h[i].k)/(h[i].s-h[j].s));
				dstTime = (h[j].dst-h[j].k)/h[j].s;
				//printf("----%d %llf %llf %llf %llf %llf\n",j,h[j].k,h[j].s,h[j].dst,meetTime,dstTime);
				
				if (meetTime <= dstTime) {
					h[i].dst = meetTime*h[i].s + h[i].k;
					//printf("%d catched %d at time %llf and location %llf, with dstTime %llf\n",i,j,meetTime,h[i].dst,dstTime);
					break;
				}
			}
		}
		
		
//		for (int i=0;i<n;i++) {
//			printf("%d %llf %llf %llf\n",i,h[i].k,h[i].dst,h[i].s);
//		}
		
		maxspeed = 99999999999999;
		
		for (int i=n-1;i>=0;i--) {
			if (abs(h[i].dst-h[i].k)<0.0000001) continue;
			maxspeed = min(maxspeed, h[i].dst*(h[i].s/(h[i].dst-h[i].k)));
		}
		
		printf("Case #%d: %llf\n", t, maxspeed);
	}
}