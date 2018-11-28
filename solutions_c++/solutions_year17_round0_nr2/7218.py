#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int n,i,j,k;
	char max;
	string s,ans;
	cin>>n;
	for(i=0;i<n;i++){
		cin>>s;
		ans="";
		if(s.size()&&s[0]=='0'){
			int flag=1;
			for(j=0;j<s.size();j++){
				if(flag&&s[j]!='0'){
					flag=0;
				}
				if(!flag){
					ans=ans+s[j];
				}
			}
			s=ans;
		}
		max='-';
		for(j=0;j<s.size();j++){
			if(max=='9'){
				s[j]='9';
			}
			else if(j!=s.size()-1&&s[j]>s[j+1]){
				k=j;
				char temp=s[j];
				while(k>=0&&temp==s[k]){
					s[k]='0'+s[k]-'0'-1;
					k--;
				}
				j=k+1;
				max='9';
			}
		}
		int ff=1;
		for(j=0;j<s.size();j++){
			if(ff&&s[j]!='0'){
				ff=0;
			}
			if(!ff){
				cout<<s[j];
			}
		}
		cout<<endl;
	}
	return 0;
}