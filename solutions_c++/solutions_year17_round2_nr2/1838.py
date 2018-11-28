#include <bits/stdc++.h>
using namespace std;
#define fori(n) for(int i=0;i<n;i++)
#define for0(i,n) for(int i=0;i<n;i++)
#define forit(i, c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ll long long
int n,r,o,y,g,b,v;
void solve();
int max(int x,int y,int z){return max(max(x,y),z);}
void display(vector<char> x)
{
vector<char>::iterator i=x.begin();
for(i;i!=x.end();i++)
cout << *i;	
	
}

vector<char> mix(vector<char> x,vector<char> y)
{
  vector<char> ans;
//  if(x.size()>y.size()) swap(x,y);
  reverse(y.begin(),y.end());
  vector<char>::iterator i=x.begin(),j=y.begin();
  
  while(i!=x.end()||j!=y.end())
  {
  	if(i!=x.end()) {ans.push_back(*i); i++;}
  	if(j!=y.end()) {ans.push_back(*j); j++;}
  }

  return ans;

}

	
int main()
{
  int T,t;
  cin >> T;
  t=T;
 
  while(T--)
  {
    cin >> n>>r>>o>>y>>g>>b>>v;

  cout <<"Case #"<<t-T<<": ";
solve();
    if(t>0) cout <<endl;
  }

	
	return 0;
}
void solve()
{
if(max(r,y,b)*2>r+y+b) {cout<<"IMPOSSIBLE"; return;}
vector<char> red(r,'R');
vector<char> yel(y,'Y');
vector<char> bul(b,'B');

if(max(r,y,b)==b) 
{
display(mix(bul,mix(red,yel)));	
}
else if(max(r,y,b)==r)
{
display(mix(red,mix(yel,bul)));

}
else display(mix(yel,mix(red,bul)));


	
	
}
