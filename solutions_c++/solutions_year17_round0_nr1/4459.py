#include<bits/stdc++.h>
using namespace std;
int main(){
	int T;
	cin>>T;
	for(int index=0;index<T;index++){
		string a;
		int count=0;
		cin>>a;
		int k;
		cin>>k;
		int sz=a.size();
		a=" "+a;
		for(int i=1;i<=sz-k+1;i++){
			if(a[i]=='+')continue;
			count++;
			for(int j=i;j<i+k;j++){
				if(a[j]=='+')a[j]='-';
				else{
					a[j]='+';
				}
			}
		}
		bool flag=true;
		for(int i=sz-k+1;i<=sz;i++){
			if(a[i]=='-')flag=false;
		}
		if(!flag){
			cout<<"Case #"<<index+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<"Case #"<<index+1<<": "<<count<<endl;
		}
	}
	return 0;
}
