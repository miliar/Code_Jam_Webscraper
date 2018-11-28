#include <stdio.h>
#include <cstring>

int r,c;
char str[30][30];

int main() {
	int test;
	scanf("%d", &test);
	for(int tc=1;tc<=test;tc++) {
		scanf("%d %d",&r,&c);
		for(int i=0;i<r;i++)
			scanf("%s",str[i]);


		//init first not '?' row
		int st=-1,le=0;
		for(int i=0;i<r;i++) {
			for(int j=0;j<c;j++) {
				if(str[i][j]!='?') {
					st=i; 
					break;
				}
			}
			if(st!=-1) break;
		}
		for(int j=0;j<c;j++) {
			if(str[st][j]!='?') {
				for(int k=le;k<j;k++)
					str[st][k]=str[st][j];
				le=j+1;
			}
		}
		for(int j=le;j<c;j++) {
			str[st][j]=str[st][le-1];
		}

		//fill prev cell
		for(int i=st-1;i>=0;i--) {
			for(int j=0;j<c;j++) {
				str[i][j]=str[i+1][j];
			}
		}

		//fill next cell
		for(int i=st+1;i<r;i++) {
			bool flag=false;
			for(int j=0;j<c;j++) {
				if(str[i][j]!='?') {
					flag=true;
					break;
				}
			}
			if(flag) {
				le=0;
				for(int j=0;j<c;j++) {
					if(str[i][j]!='?') {
						for(int k=le;k<j;k++)
							str[i][k]=str[i][j];
						le=j+1;
					}
				}
				for(int j=le;j<c;j++) {
					str[i][j]=str[i][le-1];
				}
			}
			else {
				for(int j=0;j<c;j++)
					str[i][j]=str[i-1][j];
			}
		}
		printf("Case #%d:\n",tc);
		for(int i=0;i<r;i++) {
			printf("%s\n",str[i]);
		}
	}
	return 0;
}