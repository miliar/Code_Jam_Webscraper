
#include <bits/stdc++.h>
#define fr freopen("sub-7.in","r",stdin);
#define fw freopen("output2.txt","w",stdout);
using namespace std;

int main() {
    fr;fw;
	long long t,k,n,l,r;
	string s ;

	cin>>t;//to be replaced by file input
	for(int u=1;u<=t;u++)
	{
	    cin>>n>>k;
	    long long level=log2(k);
	    level++;
	    long long pow=1;
	    for(int i=0;i<level;i++)
        {
            if(k>=pow && k<pow*2)
            {
                long long m=n-pow+1;
                long long ex=m%pow;
                if(k<=ex+pow-1){
                    long long nn=(m/pow);
                    long long h=nn/2;
                    l=(nn%2)==0?h:h+1;
                    r=nn/2;
                }
                else{
                   long long nn=(m/pow)-1;
                    long long h=nn/2;
                    l=(nn%2)==0?h:h+1;
                    r=h;
                }
            }
            pow*=2;
        }
	    cout<<"Case #"<<u<<": "<<l<<" "<<r<<"\n";
	}
	return 0;
}
