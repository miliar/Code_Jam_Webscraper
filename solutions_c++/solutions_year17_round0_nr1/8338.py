#include <bits/stdc++.h>
using namespace std;
map<string ,int> dp;

string change(string s,int k,int i)
{ for (int j=i;j<i+k;j++)
   {
        if ( s[j]=='+') {s[j]='-';}
        else s[j]='+';
   }
    return s;
}
bool check(string s)
{
    for (int i=0;i<s.size();i++)
    {
         if (s[i]=='-') {return false ;}
    }
    return true;   }


    int f(string s,int k,int i)
    {     if (check(s)) {return 0;}
         if (i>s.size()-k) {return 1000000;}

         if (dp[s]!=0) {return dp[s];}
         return dp[s]=min(f(s,k,i+1),1+f(change(s,k,i),k,i+1));

    }


int main()
 {
 //freopen("in.txt","r",stdin);
 //freopen("out.txt","w",stdout);
 int t;
 string s;
 cin>>t;
 int a;
 for (int i=1;i<t+1;i++)
 { cin>>s>>a;
   dp.clear();
    int sol=f(s,a,0);

     if  (sol!=1000000) {cout<<"Case #"<<i<<": "<<sol<<endl;}
     else {cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;}
 }
}
