#include <bits/stdc++.h>
using namespace std;
int main(){
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int y=0;y<t;y++){
		string str;cin>>str;
		long long int num=0;
		int mark=-1;
		for(int i=0;i<str.length();i++){
			if(i+1<str.length()){
				if((int)str[i]>str[i+1]){
					mark=i;
					break;
				}
			}
		}
		if(mark==-1){
			cout<<"Case #"<<y+1<<": "<<str<<endl;
		}
		else{
			int j=mark;
			while(str[j]==str[mark]){
				j--;
				if(j<0 || str[j]!=str[mark]){
					j++;break;
				}
			}
			str[j]=(char)((int)str[j]-1);
			for(int i=j+1;i<str.length();i++)
				str[i]='9';
			for(int i=0;i<str.length();i++){
				num=(num*10)+(((int)str[i])-48);
			}
			cout<<"Case #"<<y+1<<": "<<num<<endl;
		}
	}
	return 0;
}