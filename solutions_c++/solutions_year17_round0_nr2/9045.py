#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
using namespace std;


bool isSorted(string s){

	if(s.length() ==  1)
		return true;
	for(int i= 1 ; i < s.length(); i++)
		if( s[i] + '0' < s[i-1] + '0')
			return false;

	return true;
}

string last(string s){

	if(s.length() ==  1)
		return s;
        for(int i = s.length() - 1; i > - 1; i--){

		if(s[i] - '0' < s[i-1] - '0'){
			for(int j = i ; j < s.length(); j++){
				s[j] = '9';
			}
				if( s[i-1] - '0' != 0){
					s[i-1] =  ((s[i-1] - '0') - 1)+ '0';
	}

			}}

	while(s[0] == '0')
		s.erase(0,1);
		return s;
}

int main(){

	int t;
	cin>>t;

	for(int i = 1 ; i <= t; i++){
		string k;
		cin >> k;

		while(!isSorted(k)){
		       
			k = last(k);
		}

		

		cout<<"Case #"<<i<<": "<<k<<endl;

	}

	return 0;
}


