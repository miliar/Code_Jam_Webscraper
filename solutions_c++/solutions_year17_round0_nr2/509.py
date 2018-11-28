#include <cstdio>
#include <sstream>
#include <algorithm>
#include <map>
#include <cmath>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;
#define forn(i,n) for(int i=0; i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(int)(s); i<(int)(n); i++)
#define fore(i,n) forn(i,n.size())
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(n) n.begin(),n.end()
#define dbg(x) cout<<#x<<"="<<x<<endl
typedef pair<int,int> pii;


char flip(char c){
	if(c=='-')return '+';
	return '-';	
}

int main(){	
	int t;
	cin>>t;
	forn(caso,t){
		string s;
		cin>>s;
		bool flag=false;
		int pos;
		forn(i,s.size()-1){
			if(s[i+1]<s[i]){
				pos=i;
				flag=true;
				break;
			}
		}
		if(flag){
			while(pos!=0 && s[pos]==s[pos-1])pos--;
			forsn(i,pos+1,s.size())s[i]='9';
			s[pos]=s[pos]-1;
		}
		cout<<"Case #"<<caso+1<<": ";
		if(s[0]!='0')cout<<s[0];
		forsn(i,1,s.size())cout<<s[i];
		cout<<endl;
	}

	return 0;
}
