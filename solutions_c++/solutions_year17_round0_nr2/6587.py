#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;
vector<ll>f,temp;
int target;

void func(int prev)
{
   if(temp.size()==target)
   {
       ll v = 0;
       for(int j=0;j<target;j++)
       {
         v = v * 10 + temp[j];
       }
       f.push_back(v);
       return;
   }
   for(int j=prev;j<=9;j++)
   {
       temp.push_back(j);
       func(j);
       temp.pop_back();
   }
}

ll binarySearch(ll v)
{
  ll low=0,high=f.size(),mid;
  ll m=0;
  while(low<=high)
  {
      mid = (low+high)/2;
      if(f[mid]>v)
      {
         high = mid - 1;
      }
      else if(f[mid] == v) return f[mid];
      else
      {
        low = mid + 1;
        m = max(m,f[mid]);
      }
  }
  return m;

}

int main()
{

   for(int i=1;i<=18;i++)
   {
       target=i;
       func(1);
       //cout<<f.size()<<endl;
   }
   /*for(int i=0;i<=10;i++)
   {
       cout<<f[i]<<endl;
   }*/
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   ll T,t;
   scanf("%lld",&T);
   vector<ll> :: iterator it,it1;
   it = f.begin();
   for(t = 1; t <= T; t++)
   {
       ll n;
       cin>>n;
       ll v = binarySearch(n);
       printf("Case #%lld: %lld\n",t,v);
   }
   return 0;
}
