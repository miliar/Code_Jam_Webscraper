#include<iostream>
#include<iomanip>
#include<cstdio>
#include<utility>
#include<vector>
#include<queue>
#include<cmath>
#include<algorithm>
using namespace std;



//dejbfwdf
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




//sddm



int main()
{
  long long int t,n,i,j,k,c=0;
  cin>>t;



  for(i=0;i<0;i++);
    if(1);


  while(t--)
  {
    cin>>n>>k;
    c++;
     priority_queue<long long int,vector<long long int >,compare> tmkc;
    long long int lulz=n,lulz2;
    tmkc.push(n);
    for(i=0;i<k-1;i++)
    {
      lulz=tmkc.top();
      tmkc.pop();
      if(lulz%2==0)
      {
        tmkc.push(lulz/2);
        tmkc.push(lulz/2-1);
      }
      else
      {
        tmkc.push(lulz/2);
        tmkc.push(lulz/2);
      }

    }
    lulz=tmkc.top();
    tmkc.pop();
    cout<<"Case #"<<c<<": ";
    if(lulz%2==0)
      cout<<lulz/2<<" "<<lulz/2-1<<endl;
    else
      cout<<lulz/2<<" "<<lulz/2<<endl;
  }

    




return 0;  
}