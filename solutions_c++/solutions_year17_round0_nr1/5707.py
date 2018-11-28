#include<iostream>
#include<string>
using namespace std;
int main(){
	
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		string s;
		cin>>s;
		int k;
		cin>>k;
		bool a[s.length()];
		int b[k];
		int ans=0;
		for(int x=0;x<k;x++){
			b[x]=0;
		}
		for(int j=0;j<s.length();j++){
			if(s[j]=='-'){
				a[j]=0;
			}else{
				a[j]=1;
			}
		}
		int j;
		int p=0;
		for(j=0;j<s.length()-k+1;j++){
//			for(int x=0;x<k;x++){
//				cout<<"b["<<j+x<<"]="<<b[x]<<"\n";
//			}
			if(a[j]^b[0]==0){
				ans++;
				p=1;
//				cout<<"j="<<j<<"\n";
			}else{
				p=0;
			}
			for(int x=0;x<k-1;x++){
				b[x]=b[x+1]^p;
			}
			b[k-1]=0;
		}
//		for(int x=0;x<k;x++){
//			cout<<"b["<<j+x<<"]="<<b[x]<<"\n";
//		}
		b[k-1]=0;
		int x=0;
		while(j+x<s.length()){
			if(a[j+x]^b[x]==0){
				ans=-1;
				//cout<<"j+x="<<j+x<<"\n";
				break;
			}
			x++;
		}
		if(ans>=0)
			cout<<"Case #"<<i<<": "<<ans<<"\n";
		else
			cout<<"Case #"<<i<<": IMPOSSIBLE\n";
	}
	return 0;
}
