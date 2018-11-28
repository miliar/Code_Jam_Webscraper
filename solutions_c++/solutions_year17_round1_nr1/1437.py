#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,z=1;
	cin>>t;
	while(t--){
		cout<<"Case #"<<z<<": \n";
		z++;
		int r,c,i,j;
		char x;
		cin>>r>>c;
		vector<string> v(r);
		string s;
		vector<bool> f(r,false);
		for(i=0;i<r;i++){
			cin>>v[i];
			s=v[i];
			bool flag=false;
			for(j=0;j<c;j++){
				if(s[j]!='?'){
					x=s[j];
					flag=true;
					break;
				}
			}
			if(!flag){
				f[i]=false;
				continue;
			}
			else f[i]=true;
			for(j=0;j<c;j++){
				if(s[j]=='?')	s[j]=x;
				else	x=s[j];
			}
			v[i]=s;
		}
		int q;
		for(i=0;i<r;i++){
			if(f[i]){
				q=i;
				break;
			}
		}
		for(i=0;i<r;i++){
			if(f[i]){
				q=i;
			}
			else{
				v[i]=v[q];
			}
			cout<<v[i]<<endl;
		}
	}
	return 0;
}