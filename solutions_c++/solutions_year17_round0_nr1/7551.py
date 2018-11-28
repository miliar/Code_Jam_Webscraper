#include<iostream>
#include <stdio.h>
#include<string.h>
#include<vector>
using namespace std;
int main(){

	freopen("2.in","r",stdin);
	freopen("op2.txt","w",stdout);
	int T;
	cin>>T;
	for(int t = 1; t <= T; t++){
	
		char S[1200];
		int k;
		cin>>S>>k;
		int count = 0;
		int flag = 0;
		int n = strlen(S);				//sizeof(S)/sizeof(char);
		//cout<<n<<endl;
		for(int i = 0; S[i] != '\0'; i++){
		
			if(S[i] == '-'){
																								//+---+++ 2
				if(i + k - 1 <= n - 1){
				
					for(int j = 0; j < k; j++){
				
						if(S[i + j] == '-')
							S[i + j] = '+';
						else
							S[i + j] = '-';
					}
					count++;
					//cout<<count<<"  ";
				}
				else{
				
					flag = 1;
					break;
				}
			}
		}
		if(flag == 1)
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<t<<": "<<count<<endl;
	}
	return 0;
}
