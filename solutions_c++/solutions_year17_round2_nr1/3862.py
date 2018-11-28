#include <cstdio>
#include <algorithm>
#include <queue>
#include <math.h>
#include <iostream>
#include <stdlib.h>
#include <map>
using namespace std;

int main() {
	freopen("A-large (2).in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int numCases;
	scanf("%d", &numCases);
	for (int i=0;i<numCases;i++)
	{
		printf("Case #%d: ",i+1);
		int ttlDis,numCase;
		float time=0;
		scanf("%d %d",&ttlDis,&numCase);
		for (int i=0;i<numCase;i++)
		{
			int start,speed;
			float ttime;
			scanf("%d %d",&start,&speed);
			ttime=(ttlDis-start);
			ttime/=speed;
			if (time<ttime)
				time=ttime;
		}
		printf("%.6f\n",ttlDis/time);
	}
}
