#include<stdio.h>
#include<iostream>
#include<string>
#include<sstream>
using namespace std;
void print(string s,int n){
	int i;
	for (i=0;i<n;i++){
		cout<<s[i];
	}
	cout<<"\n";
}
int point(string s){
	int i;
	for(i=0;i<=s.length();i++){
		if(s[i]=='-'){
			return i;
		}
	}
}
int check(string s){
	int flag = true,j;
	for(j=0;j<s.length();j++){
		if(s[j]=='-'){
			flag = false;
			break;
		}
	}
	return flag;
}
int main(){
	int test,k;
	cin >> test;
	for(k=1;k<=test;k++){
		cout << "Case #"<< k << ": ";
		int i,j,count=0,p,n,flag;		
		string s;
		cin >> s;
		cin >> n;
		if(check(s)==true){
			cout << 0 << endl;
		}
		else{
			for (i=1;i<=s.length();i++){
//				print(s,s.length());
				p = point(s);
				if(p<=s.length()-n){
					for (j=p;j<=p+n-1;j++){
						if(s[j]=='+'){
								s[j]='-';
						}
						else{
							s[j]='+';			
						}
					}
				}
				count = count + 1;
			
				if(check(s) == true){
				//	cout << count << endl;
					break;
				}
			}
			if(count<s.length()){
				cout << count << endl;			
			}
			else{
				cout << "IMPOSSIBLE" << endl;
			}
		}
	}
}
