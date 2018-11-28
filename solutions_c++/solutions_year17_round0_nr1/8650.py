#include<iostream>
#include<cstring>
using namespace std;
int main(){
	int t,k,i,j,count,n,cased=1;
	cin>>t;
	while(t--){
		count=0;
		string s;
		cin>>s;
		cin>>k;
		n=s.size();
		for(i=0;i<(n-k+1);i++){
			if(s[i]=='-'){
				for(j=i;j<i+k;j++){
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				count++;
			}
		}
	//	cout<<s[i]<<endl;
		if(s[i]=='-')
			cout<<"Case #"<<cased<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<cased<<": "<<count<<endl;
		cased++;
	}
}
