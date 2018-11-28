#include <bits\stdc++.h>
#define ll long long
using namespace std;

int T;

void test(int nom)
{     map <ll,ll> q;
      ll n,c,k,v,t,mi,ma;
      cin>>n>>c;
      q[n]=1;
      c-=1;
      while (c)
      {
       k=q.rbegin()->first; v=q.rbegin()->second;
       t=min(v,c);
       q[k]-=t;
       c-=t;
       if (q[k]==0) q.erase(k);
       if (k%2==1) q[k/2]+=t*2;
       else {q[k/2-1]+=t; q[k/2]+=t;}
      }
      ma=q.rbegin()->first/2;
      mi=ma-(q.rbegin()->first%2==0);
      cout<<"Case #"<<nom<<": "<<ma<<" "<<mi<<"\n" ;
}

int main ()
{
 freopen("C:\\users\\Sergiy\\Downloads\\C-large.in","r",stdin);
 freopen("answer.txt","w",stdout);
 cin>>T;
 for(int i=1;i<=T;++i) test(i);
}
