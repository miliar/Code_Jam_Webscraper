#include <bits/stdc++.h>
using namespace std;

int main() {
	int T,t,n,count,temp,k;
	cin>>T;
	for(t=1;t<=T;t++){
		string s;
		cin>>s>>k;
		n=s.length();
		count=0;
		temp=0;
		int flag=0;
		for(int i=0;i<n;i++){
			if(s[i]=='-'){//cout<<i<<" ";
				if(i+k-1<n){
					for(int j=0;j<k;j++){
						if(s[i+j]=='-'){
							s[i+j]='+';
							// cout<<s[i+j]<<endl;;
						}
						else s[j+i]='-';
					}
					
						// cout<<s<<endl;
				}
				else{
					for(int j=0;j<k;j++){
						if(s[n-1-j]=='-')s[n-1-j]='+';
						else s[n-1-j]='-';
					}
				}
				count++;
				// cout<<s<<endl;
			}
		}
		
						// cout<<s<<endl;
		for(int i=0;i<n;i++){
			if(s[i]=='-'){
				temp++;
				flag=1;
			}
		}
		cout<<"Case #"<<t<<": ";
		if(flag==1){
			if(temp<k)cout<<"IMPOSSIBLE\n";
		}
		else cout<<count<<endl;
	}
	return 0;
}