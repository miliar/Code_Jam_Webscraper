/*
MADE BY SUDHANSH AGGARWAL
GOOGLE CODE JAM 2017
saggarw2@stevens.edu
*/

#include <iostream>

using namespace std;

void minmax(int t, int n, int k){
   cout<<"Case #"<<t<<": ";
   int max, ls, rs,new1, new2, pos; // for greatest ls-rs=max
   // ls is left most stall, rs is right most
   // new 1 and new 2 compare the new diff to the previous max
   bool stall[1002]={false}; //false = free, true = occupied
   for(int i=0;i<n+2;i++)
       stall[i]=false;
   stall[0]=stall[n+1]=true;
   for(int i=0;i<k;i++){ //for k people
       ls=rs=new1=new2=max=0;
       for(int j=1;j<n+2;j++){
           if(stall[j]){
               new1=new2;
               new2=j;
               if((new2-new1)>max){
                   ls=new1;
                   rs=new2;
                   max=rs-ls;
//                    cout<<"RS = "<<rs<<", LS = "<<ls<<endl;
               }
           }
       }
       // set stall to occupied; that is true
       pos = ls+((max+1)/2);
       stall[pos]=true;
   }
   int sm, big;
   sm = (rs-pos > pos - ls)?(pos - ls):(rs - pos);
   big =  (rs-pos < pos - ls)?(pos - ls):(rs - pos);
//    read and redo the output
   cout<<big-1<<" "<<sm-1<<endl;
   return;
}

int main()
{
   int t,n,k;
   //cout<<"Enter number of test cases\n";
   cin>>t;
   for(int i=1;i<=t;i++){
       //cout<<"Enter number of stalls and number of people\n";
       cin>>n>>k;
       minmax(i,n,k);
   }
   return 0;
}

