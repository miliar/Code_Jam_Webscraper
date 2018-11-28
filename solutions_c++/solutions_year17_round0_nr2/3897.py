#include <iostream>
#include <stdio.h>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int check(string s){
	for(int i=1;i<(int)s.length();i++){
		if(s[i]<s[i-1]) return i;
	}
	return -1;
}

int main(){
	int T;
	ios_base::sync_with_stdio(0);
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-practice2-.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for(int t=1;t<=T;t++){
		long long n;
		cin>>n;
		stringstream ss;
		string s;
		ss<<n;
		ss>>s;
		int idx=check(s);
		if(idx==-1) cout<<"Case #"<<t<<": "<<n<<endl;
		else{
			if(s[idx-1]>'1'){
				while(idx!=-1){
					s[idx-1]=char(s[idx-1]-1);
					for(int i=idx;i<(int)s.length();i++) s[i]='9';
					idx=check(s);
				}
				cout<<"Case #"<<t<<": "<<s<<endl;
			}
			else{
				string s1="";
				for(int i=0;i<(int)s.length()-1;i++){
					s1+='9';
				}
				cout<<"Case #"<<t<<": "<<s1<<endl;
				idx=-1;
			}
			
		}
	}
	
}
