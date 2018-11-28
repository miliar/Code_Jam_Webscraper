 #include <bits/stdc++.h>
using namespace std;

int n, sz;
string in;

long long Calc(int x)
{
    long long ret=0;
    for(int i=0;i<x;i++)
        ret*=10, ret+=9;
    return ret;
}

long long Pow(int x)
{
    long long ret=1;
    for(int i=0;i<x;i++)
        ret*=10;
    return ret;
}

int main()
{
   freopen("r.txt","r",stdin);
   freopen("out.txt","w",stdout);
   cin>>n;
   for(int i=0;i<n;i++){
      cin>>in;
      sz=in.size();
      long long ans=0, tmp=0;
      bool flag=false;
      for(int i=0;i<sz;i++){
         if(i>0 && in[i]<in[i-1])
            break;
         if(i==sz-1){
            flag=true;
            break;
         }
         if(in[i]>in[i-1]){
             tmp*=10, tmp+=in[i]-'0'-1;
             long long x=(tmp*Pow(sz-i-1))+Calc(sz-i-1);
             //cout<<tmp<<" "<<x<<"\n";
             ans=max(ans, x);
         }
         tmp/=10, tmp*=10, tmp+=in[i]-'0';
      }
      if(flag)
        cout<<"Case #"<<i+1<<": "<<in<<"\n";
      else
        cout<<"Case #"<<i+1<<": "<<ans<<"\n";
   }
    return 0;
}
