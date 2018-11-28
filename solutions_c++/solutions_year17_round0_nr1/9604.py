#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,m;
    cin>>t;
    m=t;
 //  freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);
    while(t--)
    {
        string s;
        int k,count=0,temp=0;
        cin>>s>>k;

        for(int i=0;i<s.length()-k;i++)
        {
            if(s[i]=='-')
            { for(int j=i;j<i+k;j++)
                   {
                       if(s[j]=='-')
                          s[j]='+';
                       else s[j]= '-' ;
                   }

//cout<<s<<"\n";
count++;  }
        }
        for(int i=s.length()-k;i<s.length()-1;i++)
        {
            if(s[i]!=s[i+1])
                temp=1;
        }
        if (temp==1)
            cout<<"Case #"<<m-t<<": "<<"IMPOSSIBLE\n";
        else if(temp==0)
        {  if(s[s.length()-k]=='-')
               cout<<"Case #"<<m-t<<": "<<count+1<<"\n";
            else
                cout<<"Case #"<<m-t<<": "<<count<<"\n";

        }
    }
return 0;}
