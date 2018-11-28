#include <algorithm>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>

using namespace std;


string createnumber(string s, int pos){
	
	s[pos]=s[pos]-1;
	
	for(int i=pos+1;i<s.length();i++){
		s[i]='9';			
	}
	
	
	return s;				
}




int check(vector<int> myvector){
	int pos= -1;

	bool negative=false;
	
	for(int i=0;i<myvector.size();i++){
		
		if (myvector.at(i)<0){
			negative=true;
			break;
		}
	}
	
	if (negative==false) {return pos;}
	else{
		for(int i=0;i<myvector.size();i++){		
			if (myvector.at(i)<=0){
			return i;
			}			
		}
	}	
	return pos;		
}


int main(){
	
	int t;
	
	scanf("%d",&t);
	
	for(int test=0;test<t;test++){		
		long long int k;
			
		scanf("%lld",&k);
				
		stringstream ss;
		ss << k;
	    string s= ss.str();	
		
		string result;
		if(s.length()==1){
			result = s;
		}
		else{
			vector<int> myvector;
			
			for(int i=0;i<s.length()-1;i++){
			
				myvector.push_back( (s[i+1]-'0')- (s[i]-'0') );
				
			}
			
			//only positives in myvector returns -1
			//else returns position where first 0 or negative appears
			if (check(myvector)==-1){
				result = s;
			}
			else {
				s= createnumber(s,check(myvector));
			}
							
		}

		long long int resultado;
		stringstream convert(s);
		convert >> resultado;

				
		printf("Case #%d: ",test+1);
		
		printf("%lld\n",resultado);	

	}
		
	return 0;
}
