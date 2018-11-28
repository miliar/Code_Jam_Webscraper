#include <bits/stdc++.h>
#define ld long double
using namespace std;

int main()
{
	freopen("be.txt","r",stdin);
	freopen("ki.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=0;tc<t;tc++) {
        int n, k;
        ld add;
        cin>>n>>k;
        cin>>add;
        vector<ld> x(n);
        ld sum=add;
        for(int i=0;i<n;i++) {
            cin>>x[i];
            sum+=x[i];
        }
        ld avg=sum/(ld)n;
        sort(x.begin(),x.end());
        reverse(x.begin(),x.end());
        int it=0;
        while(it<n && avg<=x[it])  {
            sum-=x[it];
            it++;
        }
        if(it!=n) {
            int u=n-it;
            ld z=sum/(ld)u;
            for(;it<n;it++) {
                x[it]=z;
            }
        }
        ld prod=1.0000000000000;
        for(ld f:x) {
            prod=prod*f;
        }
        cout<<"Case #"<<tc+1<<": "<<fixed<<setprecision(10)<<prod<<endl;
	}
    return 0;
}
