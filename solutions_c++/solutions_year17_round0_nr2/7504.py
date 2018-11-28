#define MOD 1000000007
#define P printf(" yes ")
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,jj;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>t;
	for(jj=1;jj<=t;jj++){
	long long int n,i=0,ii=0,k=0,j=0,sum=0,a[20],nn,cnt=0;
	cin>>n;
	nn=n;
	while(nn!=0){
		a[ii]=nn%10;
		nn=nn/10;
		ii++;
	}
	for(i=ii-1;i>0;i--){
		if(a[i]<=a[i-1]){
			cnt++;
		}
	}
	if(cnt==ii-1){
	}
	else{
		//cout<<"cnt "<<cnt<<" "<<ii<<endl;
	for(i=ii-1;i>0;i--){
		if(a[i]>=a[i-1]){
			a[i]=a[i]-1;
		
			for(j=i-1;j>=0;j--){
				a[j]=9;
			}
			break;
		}
	}
}
	for(i=0;i<ii;i++){
		for(k=0;k<i;k++){
			a[i]=a[i]*10;
		}
		sum=sum+a[i];
	}
	cout<<"Case #"<<jj<<": "<<sum<<endl;
	}
}

