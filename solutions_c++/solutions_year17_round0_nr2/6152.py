#include<cstdio>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;i++)

long long lastTidy(string s){
	int n = s.length();
	if(n==1)
		return stoll(s);
	int index1=-1;
	FOR(i,1,n){
		if(s[i]<s[i-1]){
			index1=i;
			break;
		}
	}
	
	if(index1==-1)
		return stoll(s);
	
	FOR(i,index1,n)
		s[i]='0';
	
	long long temp = stoll(s);
	temp--;
	
	return lastTidy(to_string(temp));
}

int main(){
	ifstream myfile("B-large.in");
	ofstream myf("p2.out");
	int t;
	myfile>>t;
	FOR(i,1,t+1){
		string s;
		myfile>>s;
		int n = s.length();
		if(s[n-1]=='0'){
			long long temp = stoll(s);
			temp--;
			s = to_string(temp);
		}
		myf<<"Case #"<<i<<": "<<lastTidy(s)<<endl;	
	}
	return 0;
}
