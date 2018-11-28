#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
    
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	
    int t;
    int p=1;
    cin>>t;
    while(t--)
    {
        double a,b,d,ma=0;
        int n;
        cin>>d>>n;
        for(int i=0;i<n;i++)
        {
            cin>>a>>b;
            ma=max(ma,(d-a)/b);
        }
        //cout<<setprecision(6)<<d/ma<<"\n";
        printf("Case #%d: %0.6lf\n",p,d/ma);
        p++;
    }
    
    
    
    
	return 0;
}

