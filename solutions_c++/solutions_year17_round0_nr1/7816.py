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
int t, k, ans;
string anz="";
string n;
ifstream infile("input.in");
ofstream outfile("output.txt");
bool allright(){
	for(int i=0; i<n.length(); i++){
		if(n[i] == '-') return false;
	}
	return true;
}
void makeplus(){
	ans=0;
	for(int i=0; i<n.length(); i++){
		if(i+k > n.length()) break;
		if(n[i] == '-'){
			ans++;
			for(int j=i; j<i+k; j++){
				if(n[j] == '-'){
					n[j] = '+';
				}else{
					n[j] = '-';
				}
			}
		}
	}
}
bool check(){
	for(int i=0; i<n.length(); i++){
		if(n[i] == '-') return false;
	}
	return true;
}
void calculate(){
	if(allright()){
		anz="0";
		return;
	}
	makeplus();
	if(!check()){
		anz="IMPOSSIBLE";
		return ;
	}
	
}
void input(){
	infile>>n;
	infile>>k;
}
void output(int s){
	if(anz=="IMPOSSIBLE" || anz=="0"){
		outfile<<"Case #"<<s<<": "<<anz<<"\n";
	}else{
		outfile<<"Case #"<<s<<": "<<ans<<"\n";
	}
	anz="";
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
























