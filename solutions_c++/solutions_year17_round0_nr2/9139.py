#include<bits/stdc++.h>
using namespace std;

int main(){
	int t,i,j,l,k,r,res=0;
	string s;
	bool f=false,u;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>s;
		res=0;
		r=0;
		f=false;
		u=false;
		if(s.size()>1)
		for(j=1;j<s.size();j++){
			if(s[j-1]>s[j]){
				k=j;
		//		cout<<"1 "<<s<<endl;
				while(k<s.size()){
					s[k++]='9';
				}
				u=true;
				k=j-1;
		//		cout<<"2 "<<s<<endl;
				s[k]--;
				if(k==0 ){
					if(s[k]=='0')
						f=true;
					break;
				}
		//		cout<<k<<" "<<s[k]<<"\n";
		//		cout<<"3 "<<s<<endl;
				if(s[k]=='0'){
					while(k>=0 ){
		//			cout<<"6 "<<s<<endl;
						if(k==0){
							f=true;
							break;						
						}
						s[k]='9';
		//			cout<<"5 "<<s<<endl;
						k--;
					}
				}else if(k-1>=0 && s[k-1]>s[k]){ //s[k]!=0
		//				cout<<"5 "<<s<<endl;
					while(k-1>=0){
						s[k-1]--;
						s[k]='9';
						k--;
					}	
				}
				if(f==true)
				break;
			}
		}
		if(f){
			cout<<"Case #"<<i<<": "<<s.substr(1,s.size())<<"\n";
		}else{
			cout<<"Case #"<<i<<": "<<s<<"\n";
		}
	}
	return 0;
}

