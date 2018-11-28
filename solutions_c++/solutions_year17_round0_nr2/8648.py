#include<iostream>
using namespace std;
#include<bits/stdc++.h>
#define f(i,n) for(int z=i; z<n; z++)
#define fe(i,n) for(int z=i; z<=n; z++)
bool checkTidy(long long int num){
    long long int i=0;
    long long int n=0;
    bool flag=true;
    long long int no=num;
    while(no>0){
      no=no/10;
      n++;
    }
    while(i<n){
        
        if(!flag) return false;
        if((num/(long long int)pow(10,i+1))%10>(num/(long long int)pow(10,i))%10){flag=false;}
          i++;
    }
    if(flag)return true;
    else return false;
}
int main()
{ int T;
 long long int num;
 cin>>T;
 f(0, T){
     cin>>num;
     while(1){
         if(checkTidy(num)) {cout<<num<<endl;break;}
         else{
            // cout<<num<<"  ";
             num=num-(num%10)-1;
         }
     }
 }
	
	return 0;
}