#include<cstdio>
#include<iostream>
#include<fstream>
#include<string>
#include<climits>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;i++)


long pancake(string s,int k, int index){
	int n = s.length();
	if(index == -1)
		return 0;
	long num = 0;
	if(index <= n-k){
		FOR(i,index,index+k){
			if(s[i]=='-') s[i]='+';
			else s[i]='-';
		}
		index = -1;
		FOR(i,0,n){
			if(s[i]=='-'){
				index=i;
				break;
			}
		}
		num=pancake(s,k,index)+1;
		return num;
	}
	
	return LONG_MIN;
}

int main(){
	ifstream myfile("A-large.in");
	ofstream myf("p1.out");
	int t;
	myfile>>t;
	FOR(i,1,t+1){
		string s;
		int k;
		long num;
		myfile>>s>>k;
		int n = s.length();
		int index=-1;
		FOR(j,0,n){
			if(s[j]=='-'){
				index=j;
				break;
			}
		}
		if(index == -1)
			myf<<"Case #"<<i<<": "<<"0\n";
		else{
			num = pancake(s,k,index);
			if(num < 0 )
				myf<<"Case #"<<i<<": "<<"IMPOSSIBLE\n";
			else
				myf<<"Case #"<<i<<": "<<num<<endl;
		}
	}
	
	return 0;
}
