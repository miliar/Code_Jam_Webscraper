#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int main(){
	int noc;cin>>noc;
	for(int cs=1;cs<=noc;cs++){
		string s;int k;cin>>s>>k;
		int ans=0;
		for(int j=0;j<s.length()-k+1;j++){
			if(s[j]=='-'){
				ans++;
				for(int t=0;t<k;t++){
					if (s[j+t]=='-')	s[j+t]='+';
					else 	s[j+t]='-';
				}
			}
		}
		for(int j=0;j<s.length();j++){
			if (s[j]=='-')	ans=-1;
		}
		if (ans==-1)	printf("Case #%d: IMPOSSIBLE\n",cs);
		else printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}