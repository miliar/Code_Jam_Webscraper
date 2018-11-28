#include <bits/stdc++.h>
using namespace std;
int a[1001];
int main(){
	ifstream fin("D:/C++/B-large.in");
	ofstream fout("D:/C++/B-large.out");
	int n;
	fin>>n;
	for ( int i = 0 ; i< n; i++){
		string s;
		bool change = false;
		int curr=0;
		fin>>s;
		for ( int j = 0 ; unsigned(j)<s.length();j++){
			a[j] = s[j]-'0';
		}
		for ( int j = 0 ; unsigned(j)<s.length()-1;j++){
			if (a[j] <a[j+1]){
				curr=j+1;
			} else if (a[j]>a[j+1]){
				change = true;
				break;
			}
		}
		if (s.length()==1){
			fout<<"Case #"<<i+1<<": "<<s<<endl;
		} else if (change){
			if (a[curr]==1){
				fout<<"Case #"<<i+1<<": ";
				for (int k = 0 ; unsigned(k)<s.length()-1;k++){
					fout<<9;
				}
				fout<<endl;
			} else{
				fout<<"Case #"<<i+1<<": ";
				for ( int k = 0 ; k<curr;k++){
					fout<<a[k];
				}
				fout<<a[curr]-1;
				for( int k = curr+1; unsigned(k)<s.length();k++){
					fout<<9;
				}
				fout<<endl;
			}
		} else{
			fout<<"Case #"<<i+1<<": "<<s<<endl;
		}
			
	}
}
				
		
		
