#include<bits/stdc++.h>
using namespace std;

#define i64 long long int
#define eps 1e-8

i64 K[1009],S[1009];
i64 D,N;


bool check(double speed)
{
	double t = D/speed;
	for(int i=0;i<N;i++){
		double d = K[i] + (S[i] * t); 
		if(d<D)return 0;
	} 
	return 1;
}

double bsearch(double lo, double hi)
{
	double mid, ans=eps;
	for(int i=0;i<1000 && lo+eps<hi && !(fabs(hi-lo)<eps);i++)
	{
		//cout<<lo<<" "<<hi<<endl;
		mid = (lo + hi)/2.0;
		//cout<<mid<<endl;
		bool t=check(mid);
		if(t && mid>ans){
			ans=mid;
			lo=mid+eps; 
		} else {
			hi=mid-eps;
		}
		//if(t)cout<<"true"<<endl;
		//else cout<<"false"<<endl;
	}
	//cout<<"ans: "<<ans<<endl;
	return ans;
}

int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	//cout<<"hello"<<endl;
	int T,cas=0;
	cin>>T;
	while(T--){
		
		cin>>D>>N;
		for(i64 i=0;i<N;i++){
			cin>>K[i]>>S[i];
		}		
		double ans=bsearch(eps,1e16);
		//cout<<ans<<endl;
		printf("Case #%d: %.7lf\n",++cas,ans);
	}
	return 0;
}
