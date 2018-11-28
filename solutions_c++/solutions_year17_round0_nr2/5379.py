#include<bits/stdc++.h>
#define tr(v,it) for(auto it=v.begin();it!=v.end();it++)
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define F first
#define S second
#define endl "\n"
#define mod 1000000007
#define pi 3.141592653589793
#define INF 1e18

using namespace std;


int main()
{
  //freopen("input1.txt","r",stdin);
  //freopen("output1.txt","w",stdout);
long long t;
cin>>t;
for(int lauda=1;lauda<=t;lauda++)
{
string s;
cin>>s;
long long sum=0;
vector<long long>v;
for(int i=0;i<s.size();i++)
{
  int x=s[i]-'0';
  v.pb(x);
}
/*
for(int i=0;i<v.size();i++)
cout<<v[i];
*/
for(int k=0;k<30;k++)
{
for(int i=0;i<v.size()-1;i++)
{
  if(v[i]>v[i+1])
  {
    v[i]--;
    for(int j=i+1;j<v.size();j++)
    v[j]=9;
    break;
  }
}
}
/*
for(int i=0;i<v.size();i++)
cout<<v[i];
*/

for(int i=0;i<v.size();i++)
{
  sum=sum*10+v[i];
}
cout<<"Case #"<<lauda<<": "<<sum<<endl;
}

  return 0;
}
