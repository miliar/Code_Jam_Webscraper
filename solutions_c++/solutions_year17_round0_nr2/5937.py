#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <bits/stdc++.h>

#define ll long long

using namespace std;


void debug(){
	fflush(stdin);
	printf("press any key to continue");
	getc(stdin);
	fflush(stdin);
}



int cases;
string s;

bool check(){
	for(int i = 1 ; i< s.length() ; i++){
		if(s[i] < s[i-1])
			return false;
	}
	return true;
}

void fun(int cas){
	for(int i = s.length()-1 ; i>=0;i--){
		char tmp = s[i];
		for(char j = tmp ; j>='0' ; j--){
			s[i] = j;
			//cout<<"s = " <<s <<endl;
			//debug();
			if(check()){
				printf("Case #%d: ",cas);
				int k = 0 ;
				while(s[k] == '0') k++;
				while(k<s.length()){
					cout<<s[k];
					k++;
				}
				cout<<endl;
				return;
			}
			if(j == '0'){
				int p = i;
				while(s[p] == '0'){
					s[p] = '9';
					p--;
				}
				s[p]--;
			}
		}
	}
}


int main(){
	cin>>cases;
	for(int cas = 1 ; cas <= cases ; cas++){
		cin>>s;
		fun(cas);
	}

//	debug();
	return 0;
}