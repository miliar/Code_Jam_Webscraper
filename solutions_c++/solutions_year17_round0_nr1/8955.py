#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("aa.in","r",stdin);
    freopen("nn.out","w",stdout);
    int t,k,ans;
    cin>>t;
    string s;
    for(int z=1;z<=t;z++)
    {
       cin>>s;
       cin>>k;
       ans=0;
       int arr[255]={0};
       if(s.length()==k)
       {
           for(int i=0;i<s.length();i++)
           {
               arr[s[i]]++;
           }
           if(arr['+']&&!arr['-'])
           {
               cout<<"Case #"<<z<<": "<<0<<"\n";
           }
           else if(arr['-']&&!arr['+'])
           {
               cout<<"Case #"<<z<<": "<<1<<"\n";
           }
           else{cout<<"Case #"<<z<<": "<<"IMPOSSIBLE\n";}
       }
       else
       {
           for(int i=0;i<=s.length()-k;i++)
           {
               if(s[i]=='-')
               {
                   ans++;
                   s[i]='+';
                   for(int j=i+1;j<i+k;j++)
                   {
                       if(s[j]=='-'){s[j]='+';}
                       else{s[j]='-';}
                   }
               }
           }
           bool val=true;
           for(int i=s.length()-k;i<s.length();i++)
           {
               if(s[i]=='-')
               {
                   cout<<"Case #"<<z<<": "<<"IMPOSSIBLE\n";
                   val=false;
                   break;
               }
           }
           if(val){cout<<"Case #"<<z<<": "<<ans<<"\n";}

       }
    }
}
