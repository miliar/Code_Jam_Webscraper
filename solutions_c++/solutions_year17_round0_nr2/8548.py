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
#define rep(i,n) for(i=0;i<n;i++)
#define endl '\n'
const int MOD = 1e9+7;
const int SIZE = 1e6+10;


vector<int> num(19);


ull fast_pow(ull base, ull n){

  if(n==0)
    return 1;
  if(n==1)
    return base;
  
  ull halfn = fast_pow(base, n/2);
  if(n%2==0)
    return halfn*halfn;
  else
    return halfn*halfn*base;

}

ull solve(ull n){

  ull w = n;
  int k=0;
  while(w){
    num[k++] = w%10;
    w/=10;
  }

  int i = k-1,j;
  
  if(i==0)
    return n;
  
  int c = 0;
  while(i>0){
    j = i-1;
    if(num[i]==num[j])
      c++;
    
    else if(num[i]>num[j]){
      
      i = i+c;
      j = i-1;
      
      ull x=0,y=0;
      while(j>=0){
	y = y*10 + num[j];
	j--;
      }
      
      x = num[i]*fast_pow(10,i)+y;
      y = y+1;
      x = x-y;
      int l = 0;
      while(l<=i){
	num[l++] = x%10;
	x/=10;
      }
	
      ull ans=0;
      j = k-1;
      while(j>=0){
        ans = ans*10 + num[j];
        j--;
      }

      return ans;
    }
    else
      c=0;
    i--;
  }

  return n;
}

int main()
{
  ios::sync_with_stdio(0), cin.tie(0);
  int t;
  cin>>t;
 
  for(int tc = 1; tc<=t;tc++){

    ull n;
    cin>>n;
    
    cout<<"Case #"<<tc<<": "<<solve(n)<<endl;
  }
  return 0;
}
