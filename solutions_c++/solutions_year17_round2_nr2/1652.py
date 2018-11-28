#include<bits/stdc++.h>
using namespace std;
#define N 100005
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long 
#define mod 1000000007
#define barn cin.sync_with_stdio(0);cin.tie(0)
pair<int,int> p[N];
int arr[N];
int check(int ind,int n,int val)
{

    int x,y;
    x=ind-1;
    if(x<1)
      x=n;
    y=ind+1;
    if(y>n)
      y=1;
    if(arr[ind]==-1 && arr[x]!=val && arr[y]!=val)
      return 1;
    return 0;
}
int main()
{
  barn;
  //freopen("inputf.in","r",stdin);
  //freopen("outputf.in","w",stdout);
  int t,k,n,a,pos;
  cin>>t;
  for(k=1;k<=t;k++)
  {
    int i,j,flag,che=0,x,y,s_pos;
     cin>>n;
     for(i=0;i<=n;i++)
      arr[i]=-1;
     for(i=0;i<6;i++)
     {
       cin>>a;
       p[i]=mp(a,i+1);
     }
     sort(p,p+6);
     pos=1;
     for(i=5;i>=0;i--)
     {
        x=p[i].ff;
        y=p[i].ss;
        s_pos=pos;
        while(x!=0)
        {
              if(check(pos,n,y)==1)
              {
                 x--;
                 arr[pos]=y; 
              }
              pos++;
              if(pos>n)
                pos=1;
              if(pos==s_pos)
                break;
        }
        if(x!=0)
         che=-1;
       /*  for(j=1;j<=n;j++)
      cout<<arr[j]<<" ";*/ 
    //cout<<"\n";
     }
     cout<<"Case #"<<k<<": ";
     if(che==-1)
      cout<<"IMPOSSIBLE\n";
    else
    {
      for(i=1;i<=n;i++)
      { 
        if(arr[i]==1)
          cout<<"R"; 
        if(arr[i]==2)
          cout<<"O"; 
        if(arr[i]==3)
          cout<<"Y"; 

        if(arr[i]==4)
          cout<<"G"; 
        if(arr[i]==5)
          cout<<"B"; 
        if(arr[i]==6)
          cout<<"V"; 
      }
      cout<<"\n";
    }
  }
  return 0;
}