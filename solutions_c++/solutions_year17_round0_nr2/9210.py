#include <iostream>
using namespace std;
#include <bits/stdc++.h>
int main(){

   int t;
   cin>>t;
   for(int i=1;i<=t;i++){

        long long int n;
        cin>>n;
        vector<int> v;
        while(n!=0){
            v.push_back(n%10);
            n/=10;
        }

        reverse(v.begin(),v.end());
        int pos=-1;
        for(int i=0;i<v.size()-1;i++){
            if(v[i+1]<v[i]){
                pos=i+1;
                break;
            }
        }

        //int c=v[pos-1];
        if(pos!=-1){
        for(int i=pos;i<v.size();i++){
            v[i]=9;
        }
        int j;
        for(j=pos-1;j>=0;j--){

            if(v[j]==v[j-1]){
                v[j]=9;
            }
            else{
                break;
            }
        }
        v[j]-=1;
    }
 cout<<"Case #"<<i<<":"<<" ";
   if(v[0]!=0){
    cout<<v[0];
   }
   for(int i=1;i<v.size();i++){

    cout<<v[i];
   }
cout<<endl;


   }




}


