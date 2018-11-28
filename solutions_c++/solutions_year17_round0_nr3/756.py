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
   long long N, K;
   scanf("%d",&T);
   for(int i=0;i<T;i++) {
	   long long arr[2][2][2]={};
	   cin>>N>>K;
	   if(K==1) {
		   printf("Case #%d: %lld %lld\n",i+1,(N>>1),(N&1) ? (N>>1):(N>>1)-1);
	   }
	   else {
		   long long result=0;
		   arr[0][0][0]=N;
		   arr[0][0][1]=1;
		   for(;!result;) {
			   for(int j=0;j<2;j++) {
				   if(!arr[0][j][0])
					   continue;
				   K-=arr[0][j][1];
				   if(K<=0) {
					   result=arr[0][j][0];
					   break;
				   }
				   if(arr[0][j][0]&1) {
					   if(arr[1][0][0]==0) {
						   arr[1][0][0]=arr[0][j][0]>>1;
						   arr[1][0][1]+=2*arr[0][j][1];
					   }
					   else if(arr[1][0][0]==arr[0][j][0]>>1) {
						   arr[1][0][1]+=2*arr[0][j][1];
					   }
					   else {
						   arr[1][1][1]+=2*arr[0][j][1];
					   }
				   }
				   else {
					   arr[1][0][0]=arr[0][j][0]>>1;
					   arr[1][1][0]=(arr[0][j][0]>>1)-1;
					   arr[1][0][1]+=arr[0][j][1];
					   arr[1][1][1]+=arr[0][j][1];
				   }
			   }
			   for(int j=0;j<2;j++) {
					for(int k=0;k<2;k++) {
						arr[0][j][k]=arr[1][j][k];
						arr[1][j][k]=0;
					}
			   }
		   }
		   printf("Case #%d: %lld %lld\n",i+1,result>>1,(result&1) ? result>>1:(result>>1)-1);
	   }
   }
   return 0;
}