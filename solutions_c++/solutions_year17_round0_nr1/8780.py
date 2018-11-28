#include <iostream>
using namespace std;
const int INF = 20000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(int a[], int M, int N, int want) {
  int s[M]; FOR(i,M) s[i] = 0;
  int sum=0, ans=0;
  FOR(i,M) {
    s[i] = (a[i]+sum)%2 != want;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return INF;
  }
  return ans;
}

int main() {
	freopen("A.in", "r", stdin);
    freopen("A.txt","w",stdout);
  int count;
  int t;
  cin>>t;
  for(int z=0;z<t;z++){	
  	count=0;
  	string s;
  	int k,l;
  	cin>>s>>k;
  	l=s.length();
  	int a[l];
  	for(int i=0;i<l;i++){
  		if(s[i]=='+')a[i]=1;
  		else a[i]=0;
	}
	 count=flips(a, l, k, 1);
  	if(count==INF){
  		cout<<"Case #"<<z+1<<": "<<"IMPOSSIBLE"<<endl;
  		
  	}
  	else cout<<"Case #"<<z+1<<": "<<count<<endl;
  }
  return 0;
}
