#include <bits/stdc++.h>

using namespace std;
int main(){
	int tc;
	cin>>tc;
	int kas=1;
	while(tc-->0){
		string n;
		cin>>n;
		cout<<"Case #"<<kas<<": ";
		if(n=="0"){
			cout<<0<<endl;
			kas++;
			continue;
		}
		int flag=777888;
		for(int i=n.size()-2;i>=0;i--){
			if(n[i]<=n[i+1])continue;
			flag=i+1;
			n[i]--;
		}
		bool notlz=false;
		for(int i=0;i<n.size();i++){
			if(n[i]!='0')notlz=true;
			if(i>=flag)cout<<9;
			else if((n[i]=='0'&&notlz==true)||(n[i]!='0'))cout<<n[i];
		}
		cout<<endl;
		kas++;
	}
	return 0;
}
