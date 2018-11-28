#include<bits/stdc++.h>
using namespace std;
int main()
{
  long long t,y;
  cin>>t;
  for(y=0;y<t;y++)
  {
    long long n,k,i,j,minn,maxx;
    cin>>n>>k;
    priority_queue<long long> m;
    m.push(n);
    while(k!=0)
    {
      n=m.top();
      m.pop();
      if(n%2==0)
      {
        i=n/2;
        j=n/2-1;
        m.push(j);
        m.push(i);
      }
      else
      {
        i=n/2;
        j=n/2;
        m.push(i);
        m.push(j);
      }
      k--;
    }
    minn=min(i,j);
    maxx=max(i,j);
    cout<<"Case #"<<y+1<<": "<<maxx<<" "<<minn<<endl;
 }
 return 0;
 }
