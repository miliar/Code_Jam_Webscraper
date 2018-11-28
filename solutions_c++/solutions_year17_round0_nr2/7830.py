#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <bits/stdc++.h>
#include <list>
#include <cmath>
#include <sstream>
#include <math.h>
#include <iomanip>
#include <set>
#include <map>
using namespace std;
int t, lastChangeIndex;
string anz="";
string n;
ifstream infile("input.in");
ofstream outfile("output.txt");
bool allright(){
	if(n.length()==1) return true;
	for(int i=0; i<=n.length()-2; i++){
		if(n[i]-'0' > n[i+1]-'0') return false;
	}
	return true;
}
void intToChard(int a, char &c, bool b){
	ostringstream convert;
	if(b) a--;
	convert << a;
	string res;
	res = convert.str();
	c=res[0];
}
int determineLastChangeIndex(){
	int changeIndex;
	for(int i=n.length()-1; i>0; i--){
		if(n[i]-'0' < n[i-1]-'0'){
			char c;
			intToChard(9, c, false);
			n[i] = c;
			intToChard(n[i-1]-'0', c, true);
			n[i-1] = c;
			changeIndex=i-1;
		}
	}
	return changeIndex;
}
void copyBeforeChange(string &ans){
	for(int i=0; i<lastChangeIndex; i++){
		ans+=n[i];
	}
}
void copyChanged(string &ans){
	int temp=n[lastChangeIndex]-'0';
	//-temp--;
	ostringstream convert;
	convert << temp;
	string res;
	res = convert.str(); 
	ans+=res;
}
void copyAfterChange(string &ans){
	for(int i=lastChangeIndex+1; i<n.length(); i++){
		ans+='9';
	}
}
bool containszero(){
	for(int i=0; i<n.length(); i++){
		if(n[i] == '0') return true;
	}
	return false;
}
void changeN(){
	while(containszero()){
		for(int i=1; i<n.length(); i++){
			bool stop=false;
			if(n[i] == '0'){
				char c;
				intToChard(n[i-1]-'0', c, true);
				n[i-1]=c;
				for(int j=i; j<n.length(); j++){
					n[j] = '9';
					stop=true;
				}
				if(stop) break;
			}
		}
		if(n[0] == '0'){
			int e=n.length()-1;
			n="";
			for(int i=0; i<e; i++){
				n+='9';
			}
		}
	}
}
void calculate(){
	string ans="";
	if(allright()){
		anz=n;
		return;
	}
	if(containszero()) changeN();
	lastChangeIndex=determineLastChangeIndex();
	copyBeforeChange(ans);
	copyChanged(ans);
	copyAfterChange(ans);
	anz=ans;
}
void input(){
	infile>>n;
}
void output(int s){
	outfile<<"Case #"<<s<<": ";
	outfile<<anz<<"\n";
}
int main(){
	infile>>t;
	for(int i=0; i<t; i++){
		input();
		calculate();
		output(i+1);
	}
	return 0;
}
























