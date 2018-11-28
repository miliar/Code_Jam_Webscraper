
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<math.h>
#include<string>
#include<string.h>
#include<stack>
#include<queue>
#include<vector>
#include<utility>
#include<set>
#include<map>
#include<stdlib.h>
#include<iomanip>

using namespace std;

#define ll long long
#define ld long double
#define EPS 0.0000000001
#define INF 1e9
#define MOD 1000000007
#define rep(i,n) for(i=0;i<n;i++)
#define loop(i,a,n) for(i=a;i<n;i++)
#define all(in) in.begin(),in.end()
#define shosu(x) fixed<<setprecision(x)
#define int ll
typedef vector<int> vi;
typedef pair<int,int> pii;

signed main(void) {
  int i,j;
  int t;
  cin>>t;
  rep(i,t){
    int n;
    cin>>n;
    while(n>0){
      int a=10;
      int tmp=n;
      bool c=true;
      while(tmp){
	if(a<tmp%10){
	  c=false;
	  break;
	}
	a=tmp%10;
	tmp/=10;
      }
      if(c)break;
      n--;
    }
    cout<<"Case #"<<i+1<<": "<<n<<endl;
  }
}
