#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,b[1004],i,j,k,inv,n,te;
	char s[1004];
	cin>>t;
	te=0;
	while(t--){
		te++;
		inv=0;
		cin>>s>>k;
		n=strlen(s);
		for(i=0;i<n;i++){
			if(s[i]=='+'){
				b[i]=1;
			}else{
				b[i]=0;
			}
		}
		for(i=0;i+k<=n;i++){
			if(b[i]==0 ){
				inv++;
				for(j=i;j<i+k;j++){
					b[j] ^= 1;
				}
			}
		}
		bool flag=true;
		for(i=n-k;i<n;i++){
			if(b[i]!=1){
				flag=false;
				break;
			}
		}
		cout<<"Case #"<<te<<": ";
		if(flag==true){
			cout<<inv<<endl;
		}else{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}