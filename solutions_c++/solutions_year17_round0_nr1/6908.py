/*************************************************************************
 > File Name: A.cpp
 > Author: makeecat
 > Created Time: 2017年04月08日 星期六 22时32分35秒
 ************************************************************************/

#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
int T,k;
char s[1010];
int main(){
	scanf("%d",&T);
	for (int kase =1 ; kase<=T;kase++){
		scanf("%s%d",s,&k);
		printf("Case #%d: ",kase);
		int l = strlen(s);
		int ans=0;
		bool flag= false;
		for (int i = 0 ; i<l;i++){
			if (s[i]=='-') {
				ans++;
				if (i+k>l){
					puts("IMPOSSIBLE");
					flag = true;
					break;
				}
				bool found = false;
				int p=0;
				for (int j=i;j<=i+k-1;j++){
					if (s[j]=='+' && !found){
						p=j;
						found = true;
					}
					if (s[j]=='+') s[j]='-';else s[j]='+';
				}
				if (!found) i = i+k-1;else i =p-1;
				//printf("%d\n",i);
				//for (int k=0;k<l;k++) printf("%c",s[k]); 
			}

		}
		if (!flag )printf("%d\n",ans);
	}
	return 0;
}
