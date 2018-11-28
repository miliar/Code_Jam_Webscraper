#include<iostream>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int x=1; x<=t; x++){
		int s,p;
		cin>>s;
		s=s+2;
		cin>>p;
		int a[s+1],b[s+1];
		for(int i=2; i<s; i++){
			a[i]=i-2;
			b[i]=s-i-1;
		}
		a[1]=-1;
		a[s]=-1;
		b[1]=-1;
		b[s]=-1;
		cout<<"Case #"<<x<<": ";
		for(int j=0;j<p;j++){
			int maxi=-1;
			int mini=-1;
			int ss=2;
			for(int i=2; i<s; i++){
				if(a[i]!=-1){
					if(a[i]<b[i]){
						if(a[i]>maxi){
							maxi=a[i];
							ss=i;
							mini=b[i];
						}else if(a[i]==maxi){
							if(b[i]>mini){
								maxi=a[i];
								ss=i;
								mini=b[i];
							}
						}
					}else{
						if(b[i]>maxi){
							maxi=b[i];
							ss=i;
							mini=a[i];
						}else if(b[i]==maxi){
							if(a[i]>mini){
								maxi=b[i];
								ss=i;
								mini=a[i];
							}
						}
					}
				}
			}
			if(j==p-1){
				if(a[ss]>b[ss]){
					cout<<a[ss]<<" "<<b[ss];
				}else{
					cout<<b[ss]<<" "<<a[ss];
				}
				break;
			}
			for(int i=2; i<ss; i++){
				if(b[i]>ss-i-1){
					b[i]=ss-i-1;
				}
			}
			for(int i=ss+1; i<s; i++){
				if(a[i]>i-ss-1){
					a[i]=i-ss-1;
				}
			}
			a[ss]=-1;
			b[ss]=-1;
		}	
		cout<<endl;
	}
	return 0;
}
