#include <bits/stdc++.h>

#define lli long long int

using namespace::std;

const double PI = 3.141592653589793;

lli recur(pair<lli,lli> a[],lli n,lli k,lli i,lli flag){
	if(k==0){
		return 0;
	}
	if(i==n-1 && flag==1){
		return a[i].first+(lli)pow(a[i].second,2);
	}else if(i==n-1){
		return a[i].first;
	}
	lli ans=0;
	if(flag==1){
		ans=a[i].first+(lli)pow(a[i].second,2)+recur(a,n,k-1,i+1,0);
	}
	ans=max(ans,a[i].first+recur(a,n,k-1,i+1,flag));
	ans=max(ans,recur(a,n,k,i+1,flag));
	//cout<<ans<<endl;
	return ans;
}

int main(){
	int t;
	cin>>t;
	int z=0;
	while(t--){
		z++;
		lli n,k;
		cin>>n>>k;
		pair<lli,lli> p;
		pair<lli,lli> a[n];
		for(lli i=0;i<n;i++){
			cin>>p.second>>p.first;
			p.first=2*p.first*p.second;
			a[i]=p;
		}
		lli ans=recur(a,n,k,0,1);
		/*
		sort(a,a+n);
		lli ans=0;
		for(lli i=1;i<n;i++){
			a[i].first=a[i].first+a[i-1].first;
		}
		if(n==k){
			ans=a[n-1].first+(lli)pow(a[n-1].second,2);
		}
		for(lli i=n-1;i-k>=0;i--){
			lli x=a[i].second;
			for(lli j=i;j>i-k;j--){
				x=max(x,a[j].second);
			}
			ans=max(ans,a[i].first-a[i-k].first+(lli)pow(x,2));
		}*/
		cout<<setprecision(9)<<fixed;
		cout<<"Case #"<<z<<": "<<ans*PI<<endl;
	}
	return 0;
}