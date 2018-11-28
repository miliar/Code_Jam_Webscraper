#include<iostream>
#include<cstring>
using namespace std;
int main(){
	bool flag=true;
	int t,k,i,j,incre,n,cased=1;
	cin>>t;
	while(t--){
		flag = true;
		incre=0;
		string s;
		cin>>s;
		cin>>k;
		n=s.size();
		for(i=0;i<(n-k+1);i++){
			if(s[i]=='-'){
				for(j=i;j<(i+k);j++){
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				incre++;
			}
		}
		for(j=i;j<n;j++){
			if(s[j]=='-'){
				flag=false;
				break;
			}
		}
		if(flag)
			cout<<"Case #"<<cased<<": "<<incre<<endl;
		else
			cout<<"Case #"<<cased<<": "<<"IMPOSSIBLE"<<endl;
		cased++;
	}
}