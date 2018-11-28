#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

string largest_num(string ar){
	string br;
	char s[ar.length()+1];
	strcpy(s, ar.c_str());
	for(int i=0; i+1<ar.length() ;i++){
		if(s[i] > s[i+1]){
			s[i]--;
			for(int j=i+1; j<ar.length() ;j++){
				s[j] = '9';
			}
			break;
		}
	}
	br = string(s);
	if(ar == br){
		return ar;
	}else{
		return largest_num(br);
	}
}
int main(){
	int t, start_idx;
	string ar;
	scanf("%d",&t);
	for(int t1=1; t1<=t; t1++){
		cin>>ar;
		ar = largest_num(ar);
		start_idx = -1;
		for(int i=0;i<ar.size();i++){
			if(ar[i]!='0'){
				start_idx = i;
				break;
			}
		}
		if(start_idx == -1){
			start_idx = ar.length()-1;
		}
		printf("Case #%d: ",t1);
		for(int i=start_idx; i<ar.length(); i++){
			printf("%c",ar[i]);
		}
		printf("\n");
	}
	return 0;
}