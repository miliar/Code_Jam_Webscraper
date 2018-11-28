#include <iostream>
#include "bits/stdc++.h"
using namespace std;

int main()
{
   //fstream in,ot;
   //in.open('sample.txt',r);
   fstream ob;
  fstream ot;
  ot.open("output.txt",ios::out);
  ob.open("A-large.in",ios::in);
   int T;

   //cin>>T;
   ob>>T;
   int n,j,i;
   string s;
   int tc=0;
   while(T--){
        tc+=1;
    //cin>>s;
    ob>>s;
    //cin>>n;
    ob>>n;
       //cout<<s<<endl;
   //cout<<n<<endl;
   int range=s.length();
   int moves=0;
   string t=s;
   for (i=0;i<=range-n;i++){
    if (s[i]=='-'){
        moves+=1;
        for (j=i;j<i+n;j++){
        if (s[j]=='+')s[j]='-';
        else  s[j]='+';
        }
        }
   }
   int chk=0;
   for(j=i;j<range;j++){
    if (s[j]=='-'){
        chk=1;
        break;
    }
   }
   int moves2=0;
   for(i=range-1;i>=n-1;i--){
       if (t[i]=='-'){
        moves2+=1;
        for (j=i;j>i-n;j--){
        if (t[j]=='+')t[j]='-';
        else  t[j]='+';
        }
        }
   }
   int chk1=0;
   for(j=i;j>=0;j--){
     if (t[j]=='-'){
        chk1=1;
        break;
    }
   }
   ot<<"Case #"<<tc<<": ";
   //cout<<"Case #"<<tc<<": ";
   if (chk1==1 &&chk==1){
    ot<<"IMPOSSIBLE\n";
    //cout<<"IMPOSSIBLE\n";
   }
   else if(chk==1){
    ot<<moves2<<endl;
    //cout<<moves2<<endl;
   }
   else if(chk1==1){
    //cout<<moves<<endl;
    ot<<moves<<endl;
   }
   else{
    ot<<min(moves2,moves)<<endl;
    //cout<<min(moves2,moves)<<endl;
   }

   }

}
