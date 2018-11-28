#include <bits/stdc++.h>
using namespace std;
const int INF = 20000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(int a[], int M, int N, int want) {
  int s[M]; FOR(i,M) s[i] = 0;
  int sum=0, ans=0;
  FOR(i,M) {
    s[i] = (a[i]+sum)%2 != want;
    //cout<<s[i]<<" ";
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    //cout<<sum<<endl;
    ans += s[i];
    if(i>M-N and s[i]!=0) return INF;
  }
  return ans;
}

int main() {
  int n,k;
  int p=1;
  cin>>n;
  while(n--)
  {
  	string s;
  	int a[100010];
  	cin>>s>>k;
  	for(int i=0;i<s.length();i++)
	{
		if(s[i]=='-')
			a[i]=0;
		else
			a[i]=1;

	}  
	int ans=flips(a,s.length(),k,1);
	if(ans==INF)
		cout<<"Case #"<<p<<": "<<"IMPOSSIBLE"<<endl;
	else

	cout<<"Case #"<<p<<": "<<ans<<endl;
p++;
  }
}