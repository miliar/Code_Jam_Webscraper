/*
MADE BY SUDHANDH AGGARWAL
CODE JAM Q2 - TIDY
saggarw2@stevens.edu
*/

#include<iostream>

using namespace std;

long long tidy(long long n){
   long long i,j,k,flag; //i = units position, j= tens position, k= numbers going down from n
   // for number to be tidy, i>=j
   int count=0;
   k=n;
   if (k%10==0)
       n--;
   while(n>=10){
       k=n;
       flag=1;
       count=0;
       while(k>=10){
          count++;
           i=k%10;
           j=(k/10)%10;
           if(j>i){
               k/=10;
               --k;
               for(int x=0;x<count;x++)
                  k=(k*10)+9;
               flag=0;
               n=k;
               break;
           }
           k/=10;
       }
       if (flag==1)
           return n;
   }
   return n;
}

int main(){
   long long t,n;
   //cout<<"Enter number of trials";
   cin>>t;
   for(long long i=1;i<=t;i++){
       cin>>n;
       cout<<"Case #"<<i<<": "<<tidy(n)<<endl;
   }
   return 0;
}
