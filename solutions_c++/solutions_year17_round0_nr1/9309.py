#include <algorithm>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <stdio.h>


using namespace std;


int check(string s){
	
	//printf("check: %s \n",s.c_str());
	
	for (int i=0;i<s.length();i++){
	
		if(s[i]=='-'){
		return -1;
		}	
	}

	return 1;
	
	
}

string flip(string s,int i,int k){

	if ( (i+k) <= s.length()){
		for (int j=0;j<k;j++){
		
			if (s[i+j]=='-') s[i+j]='+';
			else {
			s[i+j]='-';		
			}
		}
	
	}
	return s;
}


int main(){

	
	int t;
	
	scanf("%d",&t);
	
	for(int test=0;test<t;test++){		
		int k;
		char str [1001];
			
		scanf("%s %d",str,&k);
		
		string s(str);
		int count=0;
		
		for(int i=0;i<s.length();i++){
			if (s[i]=='-'){
				s= flip(s,i,k);
				count++;
			}
		}
		
		int result = check(s);
		
		printf("Case #%d: ",test+1);
		if (result==-1) printf("IMPOSSIBLE\n");
		else {
			printf(" %d\n",count);
		}
	}
		
	return 0;

}
