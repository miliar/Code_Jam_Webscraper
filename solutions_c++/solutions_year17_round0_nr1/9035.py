#include<bits/stdc++.h>
using namespace std;
int main(){
	int T;
	char a,b,c;
	cin>>T;
	char s[1000];
	int k;	
	int count;
	int flag=0;
	int j;
	for(int i=0;i<T;i++){
		count=0;
		flag=0;
		cin>>s;
		cin>>k;
		if(strlen(s)<k){
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
			continue;
		}
		for(j=0;s[j+k-1]!='\0';j++){
			if(s[j]=='-'){
				count++;
				for(int l=1;l<k;l++){
					if(s[j+l]=='-'){
						s[j+l]='+';
					}
					else{
						s[j+l]='-';
					}
				}
			}
		}
		for(;s[j]!='\0';j++){
			if(s[j]!='+'){
				cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
				flag=1;
				break;
			}
		}
		if(flag==0){
			cout<<"Case #"<<i+1<<": "<<count<<endl;
		}
	}
	return 0;
}