/*
	Copyright: razouq (c)
	Author: Anass BENDARSI
	Date: 08/04/2017 14:15:16
	flamers will **** you
*/
#include<bits/stdc++.h>
//#include<flamers.h>
#define ull unsigned long long
using namespace std;

int main(){
	freopen ("B-large.in","r",stdin);
	freopen ("B0large.txt","w",stdout);
	string tt;
	int t;
	getline(cin,tt);
	t = stoi(tt);

	for(int m = 1; m <= t; m++){
		
		string str;
		cin>>str;
		int n = str.size();
		for(int i = n-1; i > 0; i--){
			if(str[i] == '0') {
				str[i] = '9';
				for(int j = i+1; j < n; j++) str[j] = '9';
				if(str[i-1] != 0) str[i-1] --;
			}
			else {
				if(str[i] < str[i-1]){
					str[i] = '9';
					for(int j = i+1; j < n; j++) str[j] = '9';
					if(str[i-1] != 0) str[i-1] --;
				}
			}
		}
		
		cout<<"Case #"<<m<<": "<<stoll(str)<<endl;
	}
	return 0;
}

