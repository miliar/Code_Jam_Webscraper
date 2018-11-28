#include <bits/stdc++.h>
using namespace std;
const int IFT = 99999999;
#define rep(i,n) for(int i=0,_n=n; i<_n; ++i)
int a[2000];
long flips(int a[], int M, int N) {
  int s[M]; rep(i,M) s[i] = 0;
  long sum=0, ans=0;
  rep(i,M) {
    s[i] = (a[i]+sum)%2 !=1;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return IFT;
  }
  return ans;
}

int main() {
	freopen("cj2l.in","r",stdin);
freopen("cj2lo.out","w",stdout);
  int t,c=1,N,M,i;
  cin>>t;
  while(t>0){
  	char s[2000];
  	scanf("%s",s);
  	cin>>N;
  	M=strlen(s);
  	for(i=0;i<strlen(s);i++){
  		if(s[i]=='-')
  			a[i]=0;
  		else
  			a[i]=1;
	  }
  	long long h=flips(a, M, N);
  	cout<<"Case #"<<c<<": ";
  	if(h==IFT)
  		cout<<"IMPOSSIBLE"<<endl;
  	else
  		cout<<h<<endl;
  	c++;	
  	t--;
  }
}
