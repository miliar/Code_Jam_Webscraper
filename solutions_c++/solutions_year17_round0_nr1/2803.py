#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,x;
	cin>>t;
	for(x=1;x<=t;x++){
		string str;
		int l,i,j,k,sum=0,flag=0;
		cin>>str;
		cin>>k;
		cout<<"Case #"<<x<<": ";
		l=str.length();
		for(i=0;i<l;i++){
			if(str[i]=='-'&&(l-i)>=k){
				sum++;
				for(j=i;j<i+k;j++){
					if(str[j]=='+')
						str[j]='-';
					else
						str[j]='+';
				}	
			}else if(str[i]=='-'&&(l-i)<k){
				break;
			}
		}
		//cout<<str<<" ";
		if(i<l)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<sum<<endl;
	}
	return 0;
}
