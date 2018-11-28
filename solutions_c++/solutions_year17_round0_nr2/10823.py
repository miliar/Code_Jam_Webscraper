#include <bits/stdc++.h>
using namespace std;
int main()
{
  long long i,j,n,temp,t;
  std::vector<long long> v,v1;
  cin>>t;
  j=t;
  j+=1;
 while(t>0)
 {
  cin>>n;
  while(1)
  {
      temp=n;
      v.clear();
      v1.clear();
      while(temp>0)
      {
        v.push_back(temp%10);
        temp=temp/10;
      }
      reverse(v.begin(),v.end());
      v1=v;
      sort(v1.begin(),v1.end());
      if(v1==v)
      {
        cout<<"Case #"<<j-t<<": "<<n<<endl;
        break;
      }
      n--;
  }
  t--;
}
}
