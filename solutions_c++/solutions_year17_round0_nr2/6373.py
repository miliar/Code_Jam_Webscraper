//If you want to get the logic visit my website codemaniac.tech
#include <iostream>
#include <vector>
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
	freopen("B-large.in","r",stdin);
	freopen("outputLB.in","w",stdout);
	int T,t;
	cin>>T;
    for(t=1;t<=T;++t){
    	long long n,m;
    	long long res=0;
    	int i,j,k;
    	cin>>n;
    	vector<int> v;
    	m=n;
    	while(m!=0) {
          v.pb(m%10);
          m/=10;
    	}
    	int l=v.size();
    	if(l<=1){
    		res=n;
    	}
    	else {
    		reverse(v.begin(), v.end());
            for(i=0;i<l-1;++i) {
            	if(v[i]>v[i+1]){
            		j=i;
            		while(j>=0 && v[j]==v[i])
            			--j;
            		++j;
            		v[j++]-=1;
            		while(j<l)
            		{
            			v[j]=9;
            			++j;
            		}
            		break;
            	}
            }
            if(v[0]==0){
            	for(i=1;i<l;++i){
                    res=(res*10)+9;
            	}
            }
            else{
            	for(i=0;i<l;++i){
            		res=(res*10)+v[i];
            	}
            }
    	}
    	cout<<"Case #"<<t<<": "<<res<<endl;
    }
	return 0;
}