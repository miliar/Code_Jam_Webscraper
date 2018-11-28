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
		int i=0;
		while(a[i+1] && a[i]<=a[i+1]) 
			i++;
		if(a[i+1]){
			//~ cout<<i<<'\n';
			int k=i;
			char p=a[i];
			while(a[k]==p && k>=0)
				k--;
			k++;
			a[k]--;
			//~ cout<<a<<'\n';
			for(int j=k+1;a[j];j++)
				a[j]='9';
		}
		int j=0;
		while(a[j]=='0')
			j++;
		//~ int y=0;
		for(int i=j;a[i];i++){
			cout<<a[i];
			//~ y++;
		}
		cout<<'\n';
	}
}
