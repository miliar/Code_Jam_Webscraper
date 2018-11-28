#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int z=1;z<=t;z++){
		string s;
		int n;
		cin>>s;
		scanf("%d", &n);
		int count=0;
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'&&s.size()-i>=n){
				for(int j=i;j<i+n;j++){
					if(s[j]=='-')s[j]='+';
					else s[j]='-';
				}
				count++;
				i=-1;
			}
		}
		printf("Case #%d: ",z);
		bool flag=true;
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'){
				flag=false;
				break;
			}
		}
		if(flag)printf("%d\n",count);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
