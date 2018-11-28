#include <bits/stdc++.h>

using namespace std;
int main(){

	freopen("B-large.in","r",stdin);
	freopen("output_file","w",stdout);

	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long long int n;
		cin>>n;
		long long int n1=n;
		int l =0;
		while(n1!=0){
			n1/=10;
			l++;
		}
		int a[l],x=0;

		while(n!=0){
			a[x]=n%10;
			n=n/10;
			x++;
		}

	for(int j=0;j<l-1;j++){
		if(a[j]<a[j+1]){ //conflict
			a[j+1]-=1;
			// memset(a,9,(j+1)*sizeof(int));
			for (int i = 0; i < j+1; ++i)
				a[i]=9;
		}
	}
	int flag=0;
	printf("Case #%d: ",i);
	for(int j=l-1;j>=0;j--){
		if(a[j]!=0)
			flag=1;
		if(flag==1)
			printf("%d",a[j]);
	}
	printf("\n");

	}
    return 0;
}
