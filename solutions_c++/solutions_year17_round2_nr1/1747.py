// AUTHOR VINAYAK SINGLA
#include<bits/stdc++.h>
using namespace std;
#define ff first 
#define ss second 
#define lli long long int
#define f(i,o,n) for(int i=o;i<n;i++)


int main()
{
    int k,t,d,n,pt,s;
    long double max=-1,val,ans;
    cin>>t;
    cout<<fixed;
    for(int k=0;k<t;k++){
        cin>>d>>n;
        max=-1;
        for(int i=0;i<n;i++){
        	cin>>pt>>s;
        	val=(d-pt+0.0)/s;
        	if(val>max)max=val;
		}
		ans=d/max;
        cout<<"Case #"<<k+1<<": "<<setprecision(6)<<ans<<endl;
    }
    return 0;
}
