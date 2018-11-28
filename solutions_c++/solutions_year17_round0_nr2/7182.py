#include "bits/stdc++.h"
using namespace std;
string solve(string cad){
	for (int i = 0; i < cad.length()-1; ++i)
		{
			if(cad[i]>cad[i+1]){
				if(i==0 and cad[i]=='1'){
					string cad2="";
					for (int j = 0; j < cad.length()-1; ++j)
					{
						cad2=cad2+'9';
					}
					return cad2;
				}
				else {
					cad[i]-=1;
					for (int j = i+1; j < cad.length(); ++j)
					{
						cad[j]='9';
					}
				}
			}
		}
	return cad;
}
bool cond(string cad){
	for (int i = 0; i < cad.length()-1; ++i)
	{
		if(cad[i]>cad[i+1])return false;
	}
	return true;
}
int main(){
	int t;
	cin>>t;
	for (int ct = 1; ct <= t; ++ct)
	{
		string cad;
		cin>>cad;
		while(!cond(cad)){
			cad=solve(cad);
		}
		cout<<"Case #"<<ct<<": "<<cad<<endl;
	}
	return 0;
}