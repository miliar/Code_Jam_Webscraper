#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int h=0;
int co=1;
 int tidy(string s,int l)
 {
     int flag=0;
     for(int i=0;i<l-1;i++)
     {
         if((s[i])>(s[i+1])){
            flag=1;
         break;
         }
     }
     //cout<<flag;
     return flag;
 }
 void mkt(string s,int l,ofstream &out)
 {
     string s2;
    if(tidy(s,l)==0)
    {
        if(s[0]=='0')
        {
            s[0] = '9';
            s = s.substr(0,s.size()-1);

        }
            out<<"Case #"<<co++<<":"<<" "<<s<<endl;
        return;
    }
    else
    {
       for(int i=l-1;i>=0;i--)
      {
          if((i==l-1 || s[i]<s[i-1])&&h==0)
          {
            s[i]='9';
            s[i-1]--;
          }
          else if(s[i]<s[i-1])
          {
             s[i]='9';
          }
      }
      h++;
    mkt(s,l,out);
 }
 }

int main()
{
    ifstream in;
    ofstream out;
    in.open("B-large.in");
    out.open("output.txt");
    string s;
    int t;
    in>>t;
    while(t--)
    {
        h=0;
        in>>s;
   // cout<<s<<endl;
        int l=s.length();
    //cout<<l<<endl;
        mkt(s,l,out);
    //cout<<s;
    }
}
