#include<iostream>
#include<iomanip>
#include<cstdio>
#include<utility>
#include<vector>
#include<queue>
#include<cmath>
#include<algorithm>
using namespace std;
class compare
{
public:
    bool operator()(long long int& node1,long long int& node2)
    {
        if(node1<node2)
            return true;
        else
            return false;
    }
};

int main()
{
  long long int t,n,i,j,k,c=0;
  cin>>t;

  while(t--)
  {
    cin>>n>>k;
    c++;
     priority_queue<long long int,vector<long long int >,compare> q;
    long long int ans=n,ans2;
    q.push(n);
    for(i=0;i<k-1;i++)
    {
      ans=q.top();
      q.pop();
      if(ans%2==0)
      {
        q.push(ans/2);
        q.push(ans/2-1);
      }
      else
      {
        q.push(ans/2);
        q.push(ans/2);
      }

    }
    ans=q.top();
    q.pop();
    cout<<"Case #"<<c<<": ";
    if(ans%2==0)
      cout<<ans/2<<" "<<ans/2-1<<endl;
    else
      cout<<ans/2<<" "<<ans/2<<endl;
  }

    




return 0;  
}