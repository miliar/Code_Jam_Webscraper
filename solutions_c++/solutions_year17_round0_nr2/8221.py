#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;
int T;
int main(){
	cin>>T;
	for(int k=1;k<=T;k++){
		string S;
		cin>>S;
		if(S.length()==1){
			printf("Case #%d: %s\n",k,S.c_str());
			continue;
		}
		bool flag = 1;
		for(int i=0;i<S.length()-1;i++){
			if(S[i]>S[i+1]){
				flag=0;
			}
		}
		if(flag){
			printf("Case #%d: %s\n",k,S.c_str());
			continue;
		}
		else{
			int posi=-1;
			for(int i=S.length()-1;i>0;i--){
				if(S[i]<S[i-1])
					posi=i-1;
			}
			while(posi>=1 && S[posi-1]==S[posi])
				posi--;
			S[posi]--;
			for(int i=posi+1;i<S.length();i++)
				S[i]='9';
			if(S[0]=='0')
				printf("Case #%d: %s\n",k,S.substr(1,string::npos).c_str());	
			else
				printf("Case #%d: %s\n",k,S.c_str());

		}
	}
}
