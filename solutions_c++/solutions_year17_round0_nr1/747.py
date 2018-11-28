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
   int T, K;
   string input;
   scanf("%d",&T);
   for(int i=0;i<T;i++) {
	   int count=0;
	   cin>>input>>K;
	   for(int j=0;j<=input.length()-K;j++) {
		   if(input[j]=='-') {
			   for(int k=0;k<K;k++) {
				   input[j+k]=((input[j+k]=='-') ? '+':'-');
			   }
			   count++;
		   }
	   }
	   for(int j=input.length()-K;j<input.length();j++) {
		   if(input[j]=='-') {
			   count=-1;
			   break;
		   }
	   }
	   count==-1 ? printf("Case #%d: IMPOSSIBLE\n",i+1):printf("Case #%d: %d\n",i+1,count);
   }
   return 0;
}