/*
 *@author slingzor
 */
#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define ft first
#define sd second
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define ms0(X) memset((X), 0, sizeof((X)))
#define ms1(X) memset((X), -1, sizeof((X)))
#define len(X) strlen(X)
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mrg(a, b) a##b
#define gt(a) #a
#define rep(i,n) for(int i=0;i<n;i++)
#define endl '\n'
const int MOD = 1e9+7;
const int SIZE = 1e6+10;

vi v,d;

int bfs(vector<int>& v, vector<int>& d, int s, int t, int g){
  
  d[s] =0;
  queue<int> q;
  q.push(s);
  v[s]=1;
  while(!q.empty()){
    int f = q.front();
    q.pop();
    
    if(f==t)
      return d[f];
    int m = g;
    while(m<=t){
      
      int y = f^m;
      if(!v[y]){
	q.push(y);
	d[y] = d[f]+1;
	v[y] =1;
      }
      m = m<<1;
    }

  }
  return -1;
}

int main()
{
  ios::sync_with_stdio(0), cin.tie(0);
  int t;
  cin>>t;
  int k;
  string s;
  for(int tc = 1; tc<=t;tc++){
    
    cin>>s>>k;
    int n = s.length();
    
    v = vi(1<<n,0);
    d = vi(1<<n,0);
    
    int a = 0, p = 1<<(n-1);
    
    rep(i,n){
      
      if(s[i]=='+')
	a = a + p;
      p = p>>1;
	
    }
    int b = (1<<n)-1;
    int g = (1<<k)-1;
    int r = bfs(v,d,a,b,g);
    if(r==-1)
      cout<<"Case #"<<tc<<": "<<"IMPOSSIBLE"<<endl;
    else
      cout<<"Case #"<<tc<<": "<<r<<endl;
    v.clear();
    d.clear();
 
  }
  return 0;
}
