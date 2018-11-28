#include <iostream>
using namespace std;
#define ll long long int 
ll flip(ll a[], ll n, ll k) {
  ll s[n],i;
  for(i=0;i<n;i++)
     s[i]=0;
  ll sum=0, res=0;
  for(i=0;i<n;i++) 
  {
    s[i] = (a[i]+sum)%2 != 1;
    sum += s[i] - (i>=k-1?s[i-k+1]:0);
    res += s[i];
    if(i>n-k and s[i]!=0) return -1;
  }
  return res;
}

int main() {
	
 freopen("inp21.txt","r",stdin);
 freopen("op21.txt","w",stdout);

  ll t,k,n;
  string s;
  ll a[100005];
  cin>>t;
  for(ll i=1;i<=t;i++)
  {
  	cin>>s>>k;
  	n = s.length();
  	for(ll i=0;i<s.length();i++)
  		a[i] = (s[i]=='+');
  	long long int res = flip(a, n, k);
	if(res == -1)
		cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl; 
    else
		cout<<"Case #"<<i<<": "<<res<<"\n";
 }
}
