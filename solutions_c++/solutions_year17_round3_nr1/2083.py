#include<bits/stdc++.h>
using namespace std;
#define pi 3.14159265359

void getmaxer(vector<pair<long long,long long> >&v,long long n,long long k,long long i,double x,double &z,long long a)
{ //cout<<k<<" "<<x<<"\n";
  if(k==0)
  {
    z=max(z,x);
    //cout<<k<<" "<<x<<"\n";
    return;
  }
  if(i>=n||i<0)
  {
    return;
  }
  //cout<<x<<"\n";

  //getmaxer(v,n,k,i+1,x,z,a);
  //cout<<a<<(v[i].first)*(v[i].first)<<i<<"\n";
  double d=(double)(((pi*(v[i].first)*(v[i].first))-(pi*(a)*(a)))+(double)(2*pi*(v[i].first)*(v[i].second)));
  //cout<<d<<"\n";
  getmaxer(v,n,k-1,i+1,(double)x+d,z,v[i].first);
  getmaxer(v,n,k,i+1,x,z,a);
}

int main()
{
    long long i,j,k,t,n,p,a,b;
    vector<pair<long long,long long> >v;
 ifstream fin;
 fin.open("D:\\A-small-attempt0 (7).in",ios::in);
 ofstream fout;
 fout.open("D:\\cjout.txt",ios::out);
 fin>>t;
 cout<<t<<"\n";
 for(p=0;p<t;p++)
 {
   fin>>n>>k;
   cout<<n<<k<<"\n";
   for(i=0;i<n;i++)
   {
     fin>>a>>b;
     v.push_back(make_pair(a,b));
   }
   sort(v.begin(),v.end());
   /*for(i=0;i<v.size();i++)
   {
       cout<<v[i].first<<" "<<v[i].second<<"\n";
   }*/
   double z=0.0;
   getmaxer(v,n,k,0,0.0,z,0);
   fout<<"Case #"<<p+1<<": "<<fixed<<setprecision(6)<<z<<"\n";
   cout<<fixed<<setprecision(6)<<z<<"\n";
 v.clear();
 }










return 0;
}
