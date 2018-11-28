#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("resultcode2.out","w",stdout);
	int t;
	cin>>t;
	for(int x=0;x<t;x++){
		string s;
		cin>>s;
		int k;
		cin>>k;
		int l=s.length();
		int a[l];
		for(int i=0;i<l;i++){
			if(s[i]=='+')
			a[i]=1;
			else
			a[i]=0;
		}
		int sol=0;
		for(int i=0;i<=l-k;i++){
			if(a[i]==0){
				for(int j=i;j<=i+k-1&&j<l;j++){
					if(a[j]==0)
					a[j]=1;
					else
					a[j]=0;
				}
				sol++;
			}
		}
		int flag=1;
		for(int i=l-1;i>l-1-k;i--){
			if(a[i]==0){
				flag=0;
				break;
			}
		}
		if(flag==1){
			cout<<"Case "<<"#"<<x+1<<": "<<sol<<endl;
		}
		else
		cout<<"Case "<<"#"<<x+1<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}

