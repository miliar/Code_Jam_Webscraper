#include<iostream>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
  {
    long long n,k;
    cin>>n>>k;
    long long B=1;
    while(2*B<=k)
      B*=2;
    long long dad=(n-(B-1))/B;
    long long x=(n-(B-1))-(dad*B);
    if(k<B+x)
      dad++;
    if(dad%2==0)
      cout<<"Case #"<<t<<": "<<dad/2<<" "<<(dad/2)-1<<endl;
    else
      cout<<"Case #"<<t<<": "<<dad/2<<" "<<dad/2<<endl;
  }
  return 0;
}
