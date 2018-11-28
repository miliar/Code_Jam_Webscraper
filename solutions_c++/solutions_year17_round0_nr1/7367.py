#include<bits/stdc++.h>
using namespace std;
int check(string a,int k){
	int l=a.length();
	int ans=0;
	for(int i=0;i<l;i++){
		if(a[i]=='-'){
			if(i+k>l)
				return -1;
			else{
				ans++;
				for(int j=i;j<i+k;j++){
					if(a[j]=='-')
						a[j]='+';
					else
						a[j]='-';
				}
			}
		}
	}
	return ans;
}
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		string s;
		cin>>s;
		int k;
		cin>>k;
		int ans=check(s,k);
		cout<<"Case #"<<i<<": ";
		if(ans==-1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;	
	}
	return 0;
}