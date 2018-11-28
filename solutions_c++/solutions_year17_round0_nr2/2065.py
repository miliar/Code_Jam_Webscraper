#include<bits/stdc++.h>
using namespace std;
string getascnex(string s)
{ long long f,i,j,a,b;
   f=0;
   for(i=0;i<s.length()-1;i++)
   {
     a=s[i]-'0';
     b=s[i+1]-'0';
     if(a>b)
     {  f=1;
       break;
     }
   }
   cout<<s<<"\n";
   if(f==1)
   {
    s[i]='0'+a-1;
    for(j=i+1;j<s.length();j++)
    {
      s[j]='9';
    }
   }
   cout<<s<<"\n";
   for(i=s.length()-1;i>0;i--)
   {
     a=s[i]-'0';
     b=s[i-1]-'0';
     if(a<b)
     { f=1;
       s[i]='9';
       s[i-1]='0'+b-1;
     }
   }
   cout<<s<<"\n";
   string d="";
   long long k=0;
   for(i=0;i<s.length();i++)
   {
     if(s[i]!='0')
     {
       k=1;
       d+=s[i];
     }
     else if(s[i]=='0'&&k==1)
     {
       d+=s[i];
     }
   }
   return d;
}
int main()
{

 long long t,p;
 string x;
 ofstream fout;
 ifstream fin;
  fin.open("/home/anupam/B-large.in",ios::in);
  fin>>t;
  fout.open("/home/anupam/cjout.txt",ios::out);
  cout<<t<<"\n";
  for(p=0;p<t;p++)
  {
    fin>>x;
    cout<<x<<"\n";
    //cout<<getascnex(x)<<"\n";
    fout<<"Case #"<<p+1<<": "<<getascnex(x)<<"\n";
  }
return 0;
}
