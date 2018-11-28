#include<bits/stdc++.h>
using namespace std;
 int main()
 {
     long long int t,i,j,n,m,sum,x,y,z;
     fstream in("A-large.in",ios::in);
     ofstream fout("fileoutput.txt",ios::out);
     in>>t;
     for(i=0;i<t;i++)
     {
         unsigned long long int a;
         string s;
         in>>s;
         in>>a;
         sum=0;
         j=0;
         int check=1;
         while(j<s.length())
         {
             if(s[j] == '-')
             {
                 if(s.length()>=a+j)
                 {
                     string temp = s.substr(j,a);
                     string tempStr = "";
                     for(z=0;z<temp.length();z++)
                     {
                         if(temp[z] == '+')
                            tempStr+="-";
                         else
                            tempStr+="+";
                     }
                     int bn,en;
                     bn = j;
                     if(j+a>=s.length())
                     {
                         en = s.length();
                     }
                     else
                     {
                         en = j+a;
                     }
                     s = s.substr(0,bn)+tempStr+s.substr(en);
                     sum+=1;
                 }
                 else
                 {
                     check=0;
                     j = s.length();
                 }
                 j++;
             }
             else
             {
                 j++;
             }
         }
         if(check ==1)
         {
             fout<<"Case #"<<i+1<<": "<<sum<<endl;
         }
         else{
             fout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
         }
     }
     return 0;
 }
