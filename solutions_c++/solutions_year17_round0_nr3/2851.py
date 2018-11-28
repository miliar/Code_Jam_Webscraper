#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	int t,x;
	cin>>t;
	for(x=1;x<=t;x++){
		long long int n,k,i,j=0,l,r,m,ls,rs,f=2;
		cin>>n>>k;
		l=1,r=n;
		cout<<"Case #"<<x<<": ";
		int arr[61];
		for(i=1LL<<60;i>0;i=i/2){
			if(k&i)
				arr[j]=1;
			else
				arr[j]=0;
			j++;
		}
		for(i=0;i<61;i++){
			if(arr[i]==1)
				break;
		}
		i++;
		m=(l+r)/f;
		for(j=60;j>=i;j--){
			if(arr[j]==1)
				r=m-1LL;
			else
				l=m+1LL;
			m=(l+r)/f;
		}
		ls=m-l,rs=r-m;
		cout<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
	}
	return 0;
}
