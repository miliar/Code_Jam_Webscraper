#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,k;
	char s[1005];
	cin>>t;
	int x=0;
	while(t--){
		 x++;
		int swap=0;
		cin>>s>>k;
		int l=strlen(s);
		for(int i=l-1;i>=0;i--){
			if(s[i]=='-'){
				if(i>=k-1)
					swap++;
				for(int j=i;j>=i-k+1;j--){
					if(i<k-1){
						break;
					}
					
					if(s[j]=='-'){
						s[j]='+';
					}
					else if(s[j]=='+'){
						s[j]='-';
					}
				}
			//	cout<<s<<endl;
				
			}
		}
		int flag=0;
		for(int i=0;i<l;i++){
			if(s[i]=='-'){
				flag=1;
				break;
			}
		}
		if(flag==1){
			cout<<"Case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<"Case #"<<x<<": "<<swap<<endl;
		}
	}
	
	
}
