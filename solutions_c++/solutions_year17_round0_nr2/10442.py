#include <iostream>
using namespace std;
#include <bits/stdc++.h>
int main(){

   int t;
   cin>>t;
   for(int i=1;i<=t;i++){

        int n;
        cin>>n;
        for(int j=n;j>=1;j--){
            string Result;

            stringstream convert;

            convert << j;

            Result = convert.str();
            //cout<<Result<<endl;
            if(is_sorted(Result.begin(),Result.end())){
                cout<<"Case #"<<i<<":"<<" "<<Result<<endl;
                break;
            }

        }




   }




}
