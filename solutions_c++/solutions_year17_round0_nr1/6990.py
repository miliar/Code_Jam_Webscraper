#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	int o=1;
	while(t--){
		cout<<"Case #"<<o++<<": ";
		string a;
		cin>>a;
		int k;
		cin>>k;
		int flag = 1,c=0;
		int l=a.length();
		for(int i=0;i<l;i++){
			if(a[i]!='+'){
				if(i+k<=l){
					c++;
					for(int j=i;j<i+k;j++){
						if(a[j]=='-')
							a[j]='+';
						else
							a[j]='-';
					}
				}
				else{
					flag =0;
					break;
				}
			}
		}
		if(flag)
			cout<<c<<'\n';
		else
			cout<<"IMPOSSIBLE\n";
	}
}
			
