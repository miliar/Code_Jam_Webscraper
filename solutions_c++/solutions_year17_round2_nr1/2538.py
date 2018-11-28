#include <bits/stdc++.h>
using namespace std;

int main(){

	freopen("in1.in","r",stdin);
	freopen("out1.out","w",stdout);

	int Case=0,t;
	cin>>t;

	for(Case=1;Case<=t;Case++){
		cout<<"Case #"<<Case<<": ";

		int ans;
		int d,n;
		cin>>d>>n;
		int i;
		int k[1100],s[1100];
		
		int pos=0;
		float maxi=0;

		for(i=0;i<n;i++){
			cin>>k[i]>>s[i];
			if((d-k[i])>maxi*s[i]){
				maxi=((float)(d-k[i]))/s[i];
				pos=i;
			}
			
		}
		
		printf("%.7f\n",d/maxi);
		



	}
	return 0;
}