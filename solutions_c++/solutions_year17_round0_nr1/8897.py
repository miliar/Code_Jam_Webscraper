#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,i,j,l,k,r,res=0;
	string s;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>s>>k;
		res=0;
		r=0;
		for(j=0;j<s.size();j++){
			if(s[j]=='-')
			break;
		}
		//cout<<j<<"  --1"<<endl;
		for(;j<s.size();j++){
			
		//	cout<<j<<"  --4"<<j-k+1<<endl;
			if(j-k+1 >=0 && s[j-k+1]=='-'){
				r++;
			//	cout<<j<<"  --2"<<endl;
				for(l=j-k+1;l<=j;l++){
					s[l]=(s[l]=='+'?'-':'+');
			//		cout<<k<<" =k "<<s<<"\n";
				}
			}
		}
	//	cout<<r<<"  --3"<<endl;
		for(j=0;j<s.size();j++){
			if(s[j]=='-'){
			r=-1;
			break;
			}
		}
		if(r==-1){
			cout<<"Case #"<<i<<": IMPOSSIBLE\n";
		}else{
			cout<<"Case #"<<i<<": "<<r<<"\n";
		}
	}
	return 0;
}

