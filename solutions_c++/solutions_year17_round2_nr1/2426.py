#include<bits/stdc++.h>
using namespace std;
int main()
{
  ifstream fin;
  fin.open("/home/anupam/Downloads/A-large (1).in",ios::in);
  ofstream fout;
  fout.open("/home/anupam/cjout.txt",ios::out);
  long long p,d,n,k,s,t;
  fin>>t;
  for(p=0;p<t;p++)
  { double x=0.0,f;
    fin>>d>>n;
    while(n--)
    {
      fin>>k>>s;
      f=(double)(d-k)/(s*1.0);
      x=max(x,f);
    }
    cout<<x<<" "<<(double)d/x<<"\n";
    fout<<fixed<<setprecision(6)<<"Case #"<<p+1<<": "<<(double)d/x<<"\n";
  }









}
