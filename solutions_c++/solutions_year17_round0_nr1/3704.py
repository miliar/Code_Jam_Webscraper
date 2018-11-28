#include<bits/stdc++.h>
using namespace std;
int main (){
	 freopen("count.in","r",stdin);
    freopen("count.txt","w",stdout);
	int t;
	cin>>t;
	for(int q=1;q<=t;q++){
		string str;
		cin>>str;
		int x;
		cin>>x;
		int count=0;
		for(int i=0;i<=str.size()-x;i++){
			if(str[i]=='-'){
				count++;
				for(int j=0;j<x;j++){
					if(str[i+j]=='-'){
						str[i+j]='+';
					}else{
						str[i+j]='-';
					}
				}
			}
		}
		cout<<"Case #"<<q<<": ";
		int check=0;
		for(int i=0;i<str.size();i++){
			if(str[i]=='-'){
				check=1;break;
			}
		}		
		if(check==1){
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<count<<endl;
		}
	}
}
