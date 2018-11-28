#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
//#include <bits/stdc++.h>
using namespace std;
bool check(string s,int b){
	bool flag=true;
	for(int i=0;i<b;i++){
		if(s[i]!='?'){
			flag = false;
			break;
		}
	} 
	return flag;
}
int index(string s,int x,int b){
	int i;
	for(i=x;i<b;i++){
		if(s[b-1]=='?' && i==b-1){
			return x-1;
		}
		if(s[i]!='?'){
			return i;
		}
		
	}
}
int main(){
	int test,k;
	cin >> test;
	
	for(k=1;k<=test;k++){
		cout << "Case #"<< k << ": " << endl;
		//Code
string s,s1;
		int nn=0,i,j,a,b,z,l;
	//	queue<string> q;
		cin >> a >> b;
		for(;;){
	//			cout << "fdgd";
				cin>> s;
				bool g = check(s,b);
				if(g==false)		break;
				else 	nn=nn+1;
			}
//		cout<< nn;
		for (i=nn;i<a;i++){
//			cout << i;
//cout << "fghgdf";
			bool y=true,ll=0;
				
//			cout << s;
			
			
			
			
			bool g = check(s,b);
			//cout << "bhjsjd";
			if(g==false){
				
				y=false;
			//	cout << "dfgghfd";
				int m;
				m = 0;
				for(j=0;j<b;j++){
					if(s[j]=='?'){
						z = index(s,j,b);
//cout << "z" << z<< endl;
						if(z==j-1){
							for(l=j;l<b;l++){
								s[l] = s[z];
							}
						}
						else{
						for(l=j;l<z;l++){
							s[l] = s[z];
						}}
						j=z;
						m=z;
					}
				}
				for(l=m;l<b;l++){
					s[j] = s[z];
				}
			}
			else{
	
				s=s1;
				//strcpy(s,s1);	
			}
	//		cout << "abhi";
			if(i==nn){
	//cout << "ab";
				for(j=0;j<nn;j++){
			cout <<s << endl;
		}			
			}
			cout << s << endl;
			s1 = s;
			//strcpy(s1,s);
			if(i!=a-1)
			cin >> s;
		}
	}
}
