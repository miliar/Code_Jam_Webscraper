#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <list>
#include <string>

using namespace std;

int main()
{
   //*
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   //*/
   int T;
   string N, result;
   scanf("%d",&T);
   for(int i=0;i<T;i++) {
	   int t;
	   cin>>N;
	   t=N.length();
	   for(int j=1;j<N.length();j++) {
		   if(N[j-1]>N[j]) {
			   t=1;
			   for(int k=j-1;k>0;k--) {
				   if(N[k]!=N[k-1]) {
					   t=k+1;
					   break;
				   }
			   }
			   break;
		   }
	   }
	   if(t!=N.length()) {
			N[t-1]--;
			for(int j=t;j<N.length();j++) {
			   N[j]='9';
			}
	   }
	   printf("Case #%d: %s\n",i+1,N.c_str()+((t==1 && N[0]=='0') ? 1:0));
   }
   return 0;
}