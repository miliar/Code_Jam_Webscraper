#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int k,test,i,j,t;
	string s;
	bool flag;
	int count;
	t++;
	cin>>test;
	while(test--){
		cin>>s>>k;
		count = 0;
		flag = true;
		for(i = s.size()-1; i>=k-1 ; i--){
			if(s[i] == '-'){
				for(j = i;j > i-k ; j--){
					if(s[j]=='+')s[j]='-';
					else s[j]='+';
				}
				count++;
			}
		}
		for(i=0;i<=k-2;i++){
			if(s[i] == '-')flag=false;
		}
		cout<<"Case #"<<t++<<": ";
		if(flag)cout<<count<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}
