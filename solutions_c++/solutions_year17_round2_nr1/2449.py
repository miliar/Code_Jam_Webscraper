#include<bits/stdc++.h>
using namespace std;
	    int mark[1000009]={0};

int main()
{
	int t;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;

	unsigned long long int n,lane,val,p,r,x;

	for (int test = 1; test <= t; ++test)
	{
        double d,n,k,s,ans=-1;
        cin>>d>>n;

        for(int i=1;i<=n;i++){
            cin>>k>>s;
            ans=max(ans,( (d-k)/s) );
        }
        std::cout << std::fixed;
        cout<< "Case #"<<test<<": " <<  std::setprecision(6)<<d/ans<<endl;



	}



	return 0;
}
