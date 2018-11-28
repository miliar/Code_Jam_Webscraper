#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int o=0;o<t;o++)
    {
       int n,k;
       cin>>n>>k;
       vector<int> v(n);
       for(int i=0;i<n;i++)
       {
          cin>>v[i];
       }
       int ans=0;
       if(k==2)
       {
          int chet=0,nechet=0;
          for(int i=0;i<n;i++)
          {
             if(v[i]&1)
             {
                nechet++;
             }
             else
             {
                chet++;
             }
          }
          ans=chet+(nechet+1)/2;
       }
       else if(k==3)
       {
          int a=0,b=0,c=0;
          for(int i=0;i<n;i++)
          {
             if(v[i]%3==0)
             {
                a++;
             }
             else if(v[i]%3==1)
             {
                b++;
             }
             else
             {
                c++;
             }
          }
          ans=a+min(b,c);
          int last=0;
          if(b<c)
          {
             c-=b;
             ans+=c/3;
             if(c%3)ans++;
          }
          else
          {
             b-=c;
             ans+=b/3;
             if(b%3)ans++;
          }
       }
       else
       {
          int a=0,b=0,c=0,d=0;
          for(int i=0;i<n;i++)
          {
             if(v[i]%4==0)
             {
                a++;
             }
             else if(v[i]%4==1)
             {
                b++;
             }
             else if(v[i]%4==2)
             {
                c++;
             }
             else
             {
                d++;
             }
          }
       }
       cout<<"Case #"<<o+1<<": "<<ans<<'\n';

    }
    return 0;
}
