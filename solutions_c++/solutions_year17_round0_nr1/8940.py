#include<iostream>
#include<string>
#include<fstream>
using namespace std;
 int main()
 {
     long long int t,i,j,k,n,m,sum,x,y,z;
     ifstream cin("A-large.in");
     ofstream cout("output_large.txt");
     cin>>t;
     for(i=1;i<=t;i++)
     {
         string s;
         cin>>s>>k;
         sum=0;
         j=0;
         int flag=1;
         while(j<s.length())
         {
             //cout<<s<<endl;
             //cin>>m;
             if(s[j] == '-')
             {
                 if((s.length() - j)>=k)
                 {
                     string temp = s.substr(j,k);
                     string tempStr = "";
                     for(z=0;z<temp.length();z++)
                     {
                         if(temp[z] == '-')
                            tempStr+="+";
                         else
                            tempStr+="-";
                     }
                     int bn,en;
                     bn = j;
                     if(j+k>=s.length())
                     {
                         en = s.length();
                     }
                     else
                     {
                         en = j+k;
                     }
                     s = s.substr(0,bn)+tempStr+s.substr(en);
                     sum++;
                 }
                 else
                 {
                     flag=0;
                     j = s.length();
                 }
                 j++;
             }
             else
             {
                 j++;
             }
         }
         if(flag ==1)
         {
             cout<<"Case #"<<i<<": "<<sum<<endl;
         }
         else{
             cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
         }
     }
     return 0;
 }
