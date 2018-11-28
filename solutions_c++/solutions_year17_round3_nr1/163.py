#include <bits/stdc++.h>

using namespace std;
#define int long long
pair<int,int> arr[1219];
#undef int
int main(){
	#define int long long
	int tc,tci=0;cin>>tc;
	while(tc-->0){
		tci++;
		int n,k;cin>>n>>k;
		for(int i=0;i<n;i++){
			cin>>arr[i].second>>arr[i].first;
			arr[i].first*=arr[i].second;
		}
		sort(arr,arr+n);
		reverse(arr,arr+n);
//		for(int i=0;i<n;i++){
//			cout<<arr[i].first<<' '<<arr[i].second<<endl;
//		}
		double ans=0;
		for(int i=0;i<n;i++){
			double nans=0;
			nans+=arr[i].second*arr[i].second+2*arr[i].first;
//			cout<<i<<' ';
			for(int j=0,no=0;j<k-1;j++,no++){
				if(no==i)no++;
//				cout<<no<<" \n"[j==k-2];
				nans+=arr[no].first*2;
			}
			cout<<(long long)nans<<endl;
			ans=max(ans,nans*acos(-1));
		}
		cout<<"Case #"<<tci<<": ";
		cout<<fixed<<setprecision(9)<<ans<<endl;
	}
	return 0;
}
