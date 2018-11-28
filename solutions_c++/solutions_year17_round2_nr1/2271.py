#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <string>

using namespace std;

int T, D, N, K, S;
double result;

int main()
{
   //*
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   //*/
   scanf("%d",&T);
   for(int i=0;i<T;i++) {
	   scanf("%d%d",&D,&N);
	   result=0;
	   for(int j=0;j<N;j++) {
		   scanf("%d%d",&K,&S);
		   result=max(result,(double)(D-K)/S);
	   }
	   printf("Case #%d: %.6lf\n",i+1,D/result);
   }
   /*
   system("PAUSE");
   //*/
   return 0;
}