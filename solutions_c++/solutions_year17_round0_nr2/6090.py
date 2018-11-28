#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<algorithm>
#include<map>
#include<string>
using namespace std;

typedef long long ll;

int main() {
	int t;
	cin>>t;
	int cas = 0;
	while(t--){
		string s;
		cin>>s;
		int i=1;
		while(i<s.size() and s[i]>=s[i-1])
		       i++;
		if(i != s.size()){
			for(int j=i;j<s.size();++j)
				s[j] = '9';
			i--;
			while(i>0 and s[i]==s[i-1])
			{
				s[i] = '9';
				i--;
			}
			s[i] = s[i]-1;
		}
		string tt;
		for(int i=0;i<s.size();++i){
			if(i==0 and s[i]=='0')
				continue;
			tt.push_back(s[i]);
		}
		cout<<"Case #"<<++cas<<": "<<tt<<endl;
	}
	return 0;
}
