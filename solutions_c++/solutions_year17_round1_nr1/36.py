#include<bits/stdc++.h>
int row,col;
char a[99][99];
int main(){
	int _,t;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%d%d",&row,&col);
		for(int i=0; i<row; i++)
			scanf("%s",a[i]);
		for(int i=0; i<row; i++){
			for(int j=1; j<col; j++)
				if(a[i][j] == '?' && a[i][j-1] != '?')
					a[i][j] = a[i][j-1];
		}
		for(int i=0; i<row; i++){
			for(int j=col-2; j>=0; j--)
				if(a[i][j] == '?' && a[i][j+1] != '?')
					a[i][j] = a[i][j+1];
		}
		for(int i=1; i<row; i++)
			for(int j=0; j<col; j++)
				if(a[i][j] == '?' && a[i-1][j] != '?')
					a[i][j] = a[i-1][j];
		for(int i=row-2; i>=0; i--)
			for(int j=0; j<col; j++)
				if(a[i][j] == '?' && a[i+1][j] != '?')
					a[i][j] = a[i+1][j];
		printf("Case #%d:\n",t);
		for(int i=0; i<row; i++)
			puts(a[i]);
	}
	return 0;
}
