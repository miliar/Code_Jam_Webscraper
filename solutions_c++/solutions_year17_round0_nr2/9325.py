#include<bits/stdc++.h>
#define ll long long
#define sync ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;
int main() {
	// my code here
	sync
	freopen("in.in","r",stdin);
    freopen("out.in","w",stdout);
	ll tc=1,tt;
	cin>>tc;
	tt=tc;
	while(tc--)
	{
	    ll i,j,n=0,m,z,p=1,r=0,x,y;
	    cin>>y;
	    x=y;
	    vector<ll>a;
	    while(x>0){
            a.push_back(x%10);
            n++;
            x=x/10;
	    }
	    for(i=1;i<n;i++)
        {
            if(a[i-1]<a[i])
            {
                a[i]--;
                for(j=i-1;j>=0;j--)
                    a[j]=9;
            }
        }
        for(i=n-1;i>=0;i--){
            r=r*10+a[i];
        }
        cout<<"Case #"<<(tt-tc)<<": "<<r<<endl;
	}
	return 0;
}

