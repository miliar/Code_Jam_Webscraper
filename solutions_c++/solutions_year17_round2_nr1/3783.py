#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
  int T;
  cin>>T;
  for(int i=1;i<=T;i++)
  {
    double D; 
    int N;  cin>>D>>N;
    double maxtime=-1,so;
    for(int j=0;j<N;j++)
    {
      int a,b;
      cin>>a>>b;
      so=(D-a)/b;
      if(so>maxtime)  maxtime=so;  

    }
    
    cout<<"Case #"<<i<<": "<<setprecision(6)<<fixed<<D/maxtime;
    cout<<endl;
  }
  return 0;
}