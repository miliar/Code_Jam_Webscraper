//If you want to get the logic visit my website codemaniac.tech
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#define MX 1000001
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define fs first
#define sec second
#define sc scanf
#define pr printf
typedef long long li;
using namespace std;
int main() {
	freopen("A-large (1).in","r",stdin);
	freopen("output1LA.in","w",stdout);
	int T,t;
	cin>>T;
    for(t=1;t<=T;++t){
      int k,n,d,i,j,s;
      cin>>d>>n;
      float res=0;
      float mx=0;
      for(i=0;i<n;++i){
      	cin>>k>>s;
        j=d-k;
        float time=j/((1.0)*s);
        if(mx<time)
        	mx=time;
      }
      res= (d*1.0)/mx;
      cout<<"Case #"<<t<<": "<<fixed<<setprecision(6)<<res<<endl;
    }
    return 0;
}