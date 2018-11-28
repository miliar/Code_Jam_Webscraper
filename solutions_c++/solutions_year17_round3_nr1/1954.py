#define MOD 1000000007
#define P printf(" yes ")
#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,tt=0;
	freopen("30al.in","r",stdin);
	freopen("30al.out","w",stdout);
	cin>>t;
	for(tt=1;tt<=t;tt++){
		long long int n,k,i,aa,bb,ans=0,l,j;
		cin>>n>>k;
		pair<long long int, long long int> a[n];
		for(i=0;i<n;i++){
			cin>>aa>>bb;
			a[i].first=aa;
			a[i].second=bb;
		}
		sort(a,a+n);
	/*	for(i=0;i<n;i++){
			cout<<"testing "<<endl;
			cout<<a[i].first<<" "<<a[i].second<<endl;
		}*/
		for(i=0;i<n;i++){
		//	cout<<"aa "<<a[i].first<<endl;
			if(a[i].first>=a[k-1].first){
		//		cout<<"a "<<a[i].first<<endl;
				long long int sum=0;
				long long int b[n];
				for(j=0;j<n;j++){
					if(j!=i){
						b[j]=a[j].first*a[j].second;
					}
					else
					b[j]=0;
				}
				sort(b,b+n);
				for(l=n-1;l>n-k;l--){
					sum=sum+b[l];
				}
				//cout<<"sum "<<sum<<endl;
				sum=sum+(a[i].first*a[i].second);
				sum=sum*2;
				sum=sum+(a[i].first*a[i].first);
				ans=max(ans,sum);
				//cout<<"ans"<<ans<<endl;
			}
		}cout<<"Case #"<<tt<<": ";
	cout<<setprecision(20)<<3.14159265359*ans<<endl;
	}
}

