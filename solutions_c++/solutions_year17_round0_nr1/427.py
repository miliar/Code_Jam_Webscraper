#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string.h>
using namespace std;

void flip(char* str, int start, int k){
   for(int i=start; i<=start+k-1;i++){
      if(str[i]=='+') str[i]='-';
      else if(str[i]=='-') str[i]='+';
   }
}

int main(){
   int n;
   cin >> n;
   for(int i=0; i<n; i++){
   	   char str[1500]; 
   	   int s,k;
   	   cin >> str >> k;
   	   s = strlen(str);
   	   bool possible; 
   	   
   	   int start = 0;
   	   int end = s-1;
   	   // find first - and last -
   	   int flip_count = 0;
   	   while(start<=end){
           if(str[start] == '+')  start++;
		   else break;
	   }
	   if(start>end){
	   	   cout << "Case #" << i+1 << ": 0\n";
	   	   continue;
	   }
	   while(start<=end){
	   	   if(str[end] == '+') end--;	
		   else break;
	   }
	   while(start+k-1 < end){
	       flip(str,start,k);
	       flip_count++;
	       // calculate newstart
	       int newstart = start;
	       while(str[newstart]=='+') newstart++;
		   start = newstart;  
	   }
	   if(start+k-1==end){
	       possible = 1; 
	       for(int j=start; j<=end; j++){
		      if(str[j]=='+') possible = 0;
		   }
		   flip_count++;
	   }
	   else{
	       possible = 0;
	   }
	   
	   if(possible){
	       cout << "Case #" << i+1 << ": " << flip_count << "\n";
	   }
	   else{
	       cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
	   }
   }
}

