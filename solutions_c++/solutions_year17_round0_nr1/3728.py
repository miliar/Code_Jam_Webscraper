#include <bits/stdc++.h>
using namespace std;
char a[1001];
int main(){
	ifstream fin("D:/C++/A-large.in");
	ofstream fout("D:/C++/A-large.out");
	int n,k;
	fin>>n;
	for ( int i = 0 ; i< n ; i++){
		string s;
		fin>>s;
		bool poss = true;
		int total=0;
		for ( int j = 0 ; unsigned(j)< s.length();j++){
			if (s[j]=='+'){
				a[j]='+';
			} else{
				a[j]='-';
			}
		}
		fin>>k;
		for ( int curr = 0 ; unsigned(curr) <= s.length()-k; curr++){
			if (a[curr]=='-'){
				total++;
				for ( int j = 0 ; j<k;j++){
					if (a[curr+j] =='+'){
						a[curr+j] ='-';
					} else{
						a[curr+j]='+';
					}
				}
			}
		}
		for ( int j = 0 ; unsigned(j)<s.length();j++){
			if (a[j]=='-'){
				poss= false;
			}
		}
		if (poss){
			fout<<"Case #"<<i+1<<": "<<total<<endl;
		} else{
			fout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
	
	}
			
		
