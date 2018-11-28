/*************************************************************************
 > File Name: A.cpp
 > Author: makeecat
 > Created Time: 2017年04月15日 星期六 09时13分26秒
 ************************************************************************/

#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
using namespace std;

int n,m,T;
char s[26][26];
bool b[26];
int main()
{
	scanf("%d",&T);
	for (int kase=1;kase<=T;kase++){
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			scanf("%s",s[i]);
		memset(b,0,sizeof(b));
		for (int j=0;j<m;j++){
			int i=0;
			char ch=s[0][j];
			while (i<n && ch=='?') {i++; ch=s[i][j];}
			if (i==n) b[j]=true;else{
				for (int k=0;k<i;k++) s[k][j]=ch;
			}
			while (i<n){
				if (s[i][j]!='?') ch=s[i][j];
				else s[i][j]=ch;
				i++;
			}
		}
		//for (int i=0;i<m;i++)if (b[i]) printf("%d ",i);puts("");
		int p=0;
		while (p<m){
			if (!b[p]) {p++;break;};
			p++;
		}
		
		p--;
		for (int j=0;j<p;j++){
			for (int i=0;i<n;i++) s[i][j] = s[i][p];
		}
		for (int j=p;j<m;j++){
			if (!b[j])  p=j;
			else{
				for (int i=0;i<n;i++) s[i][j] = s[i][p];
			}
		}
		printf("Case #%d:\n",kase);
		for (int i=0;i<n;i++)
			printf("%s\n",s[i]);
	}
	return 0;
}
