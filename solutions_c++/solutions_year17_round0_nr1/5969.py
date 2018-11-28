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


int t,k;
string s;

int fun(){
	int cnt = 0;
	int n = s.length();
	for(int i = 0 ; i< n;i++){
		if(s[i] == '-'){
			if(i + k - 1 <= n-1){
				++cnt;
				for(int j = 0 ; j <k; j++){
					if(s[i+j] == '+')
						s[i+j] = '-';
					else
						s[i+j] = '+';
				}
			}
			else return -1;
		}
	}
	return cnt;
}

int main(){
	cin>>t;
	for(int i =1; i <=t;i++){
		cin>>s;
		cin>>k;
		int ans = fun();
		printf("Case #%d: ",i);
		if(ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}


	
	//debug();
	return 0;
}