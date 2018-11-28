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
//  freopen("input.txt","r",stdin);
 //freopen("output.txt","w",stdout);
long long t;
cin>>t;
for(int lauda=1;lauda<=t;lauda++)
{
string s;
int k;
cin>>s>>k;
int n=s.size();
bool possible=true;
int count=0;
for(int i=0;i<n;i++)
{

  if(s[i]=='+')
  continue;
  else
  {
    if(i+k>n)
    {
      possible=false;
      break;
    }
   else
    {
      for(int j=i,l=0;l<k;j++,l++)
      {
       if(s[j]=='+')
        s[j]='-';
        else
        s[j]='+';
      }
      count++;
    }
//    cout<<s<<endl;
  }
}

cout<<"Case #"<<lauda<<": ";
if(possible)
cout<<count<<endl;
else
cout<<"IMPOSSIBLE"<<endl;
}


  return 0;
}
