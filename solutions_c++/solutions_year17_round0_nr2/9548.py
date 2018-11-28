#include <stdio.h>
#include <iostream>
#include <sstream>
#include <math.h>
#include <string.h>
#include <map>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#define INF 100000
#define MAX 100005

using namespace std;
#define For(i, a, b) for ( int i = (a); i < (b); i++ )
#define Fors(i, sz) for ( size_t i = 0; i < sz.size (); i++ )
#define Set(a, s) memset (a, s, sizeof (a))
 #define EXPLORED 2
#define VISITED 1
#define UNVISITED 0
typedef long long int ll;
 typedef pair<int,int> ii;
 typedef vector<ii> vii;
 typedef vector <int > vi;

int main()
{
  //int ans[10000][100000];
   freopen("B-large.in","r",stdin);
 freopen("output.txt","w",stdout);
ll tc,ind,flag=0,cnt=0,f=0;
string str,ans;
 cin>>tc;
 while(tc--)
 {
  cnt++;
  cout<<"Case #"<<cnt<<": ";
  cin>>str;
  for(ll i=str.size()-1;i>=1;i--)
  {
    if(str[i]>=str[i-1])
      continue;
    else
    {
      //str[i]='9';
      str[i-1]=str[i-1]-1;
      for(ll j=i;j<str.size();j++)
        str[j]='9';
    }
  }
 // cout<<str<<" ";
  if(str[0]=='0')
  {
    for(ll i=1;i<str.size();i++)
      cout<<str[i];
  }
  else
  cout<<str;
cout<<endl;
 }
return 0;

}