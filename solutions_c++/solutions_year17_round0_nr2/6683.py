#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <set>
#include <algorithm>
#include <queue>
#include <math.h>
#include <iomanip>
#include <map>
#include <stdlib.h>
#include <sstream>
using namespace std;

string delzero(string s){
	int len=s.length();
	for(int i = 0; i < len; i++){
		if(s[i]!='0'){
			break;
		}
		else{
			s = s.substr(1,len);
		}
	}
	return s;
}

int main(){
	int t;
	cin>>t;
	int count=1;
	while(t--){
		
		long long n;
		cin>>n;
		stringstream ss;
		ss << n;
		string num = ss.str();
		int len = num.length();
		char curr = num[0];
		int ch = 0;
		for(int i=1; i<len; i++){
			if(num[i]>curr){
				curr = num[i];
				ch = i;
			}
			else if(num[i]<curr){
				num[ch]=num[ch]-1;
				for(int j = ch+1; j < len; j++){
					num[j] = '9';
				}
				break;
			}
		}
		num = delzero(num);
		cout<<"Case #"<<count<<": "<<num;
		count++;
		cout<<endl;

	}
		
	
	return 0;
}
