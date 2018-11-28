#include<bits/stdc++.h>
using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	string s;
	int n,k;
	char ch;
	scanf("%d",&n);
	for (int i=1; i<=n; i++){
		cin>>s;
		if (s[0]=='0') {
			printf("Case #%d: 0\n",i);
			continue;
		}
		for (int j=0; j<s.length(); j++){
			if (j>0 and s[j]<s[j-1]){
				ch=s[j-1];
				k=j-1;
				while (k>=0 and s[k]==ch){
					--k;
				}
				++k;
				--s[k];
				for (int l=k+1; l<s.length(); l++) s[l]='9';
			}
		}
		printf("Case #%d: ",i);
		for (int j=0; j<s.length(); j++) if (s[j]!='0') printf("%c",s[j]);
		printf("\n");
	}
}
