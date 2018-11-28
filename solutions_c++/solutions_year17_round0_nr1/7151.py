#include <bits/stdc++.h>
using namespace std;

int main()
{
freopen("A-large.in","rt",stdin);
freopen("out.txt","wt",stdout);
int n,k;
cin>>n;
string s;

for(int i=0;i<n;i++)
{
    map<string,bool>ma;
    cin>>s;
    cin>>k;
    int cnt=0;
    while(true){
    if(ma[s]==1){
        cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        break;
    }
    else
    {
        ma[s]=1;
        int pos=-1;
       for(int j=0;j<s.size();j++)
       {
           if(s[j]=='-')
           {
               pos=j;
               break;
           }
       }
       if(pos+k>=s.size()&&pos!=-1)
         pos=s.size()-k;
       else if(pos==-1)
       {
           cout<<"Case #"<<i+1<<": "<<cnt<<endl;
           break;
       }
       int l=0;
       for(int j=pos;j<s.size()&&l<k;j++)
       {
           if(s[j]=='-')
            s[j]='+';
           else s[j]='-';
           l++;
       }
       cnt++;
    }
    }
}


}
