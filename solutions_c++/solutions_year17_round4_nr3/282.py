#include <bits/stdc++.h>
using namespace std;
int n,m;
char s[55][55];
int c[55][55];

void fuck()
{
	int i,j,k,last,num,x,y;
	memset(c,0,sizeof(c));
	scanf("%d%d",&n,&m);
	for(i=1;i<=n;i++){
		scanf("%s",&s[i][1]);
	}
	for(i=1;i<=n;i++) s[i][m+1]=s[i][0]='#';
	for(i=1;i<=n;i++){
		last=num=0;
		for(j=last+1;j<=m+1;j++){
			if(s[i][j]=='#'){
				if(num==1){
					for(k=last+1;k<j;k++)
						if(s[i][k]=='|') s[i][k]='-';
				}
				else if(num>1){
					for(k=last+1;k<j;k++)
						if(s[i][k]=='-') s[i][k]='|';
				}
				last=j;num=0;
			}
			else if(s[i][j]=='-'||s[i][j]=='|') num++;
		}
	}
	bool ok=1;
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++){
			if(s[i][j]=='|'){
				for(k=i-1;k>=1;k--){
					if(s[k][j]=='#') break;
					else if(s[k][j]=='-'||s[k][j]=='|'){
						ok=0;
						break;
					}
					else c[k][j]=(i-1)*m+j;
				}
				for(k=i+1;k<=n;k++){
					if(s[k][j]=='#') break;
					else if(s[k][j]=='-'||s[k][j]=='|'){
						ok=0;
						break;
					}
					else c[k][j]=(i-1)*m+j;
				}
			}
		}
	for(int t=1;t<=n*m;t++){
		for(x=1;x<=n;x++)
		for(y=1;y<=m;y++){
			if(s[x][y]!='-') continue;
			bool co=1;
			for(k=y-1;k>=1&&s[x][k]!='#';k--) if(c[x][k]==0){co=0;break;}
			for(k=y+1;k<=m&&s[x][k]!='#';k++) if(c[x][k]==0){co=0;break;}
			if(co==0) continue;
			bool okk=1;
			for(k=x-1;k>=1&&s[k][y]!='#';k--)
				if(s[k][y]=='-'||s[k][y]=='|'){okk=0;break;}
			for(k=x+1;k<=n&&s[k][y]!='#';k++)
				if(s[k][y]=='-'||s[k][y]=='|'){okk=0;break;}
			if(okk==0) continue;
			s[x][y]='|';
			for(k=x-1;k>=1&&s[k][y]!='#';k--) c[k][y]=(x-1)*m+y;
			for(k=x+1;k<=n&&s[k][y]!='#';k++) c[k][y]=(x-1)*m+y;
		}
	}
	for(x=1;x<=n;x++)
		for(y=1;y<=m;y++){
			if(s[x][y]!='-') continue;
			for(k=y-1;k>=1&&s[x][k]!='#';k--){
				if(s[x][k]=='|'||s[x][k]=='-'){ok=0;break;}
				c[x][k]=(x-1)*m+y;
			}
			for(k=y+1;k<=m&&s[x][k]!='#';k++){
				if(s[x][k]=='|'||s[x][k]=='-'){ok=0;break;}
				c[x][k]=(x-1)*m+y;
			}
		}
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
			if(s[i][j]=='.'&&c[i][j]==0){
				ok=0;
				//printf(" %d %d\n",i,j);
				break;
			}
	for(i=1;i<=n;i++) s[i][m+1]=0;
	//for(i=1;i<=n;i++) puts(s[i]+1);
	if(ok){
		printf("POSSIBLE\n");
		for(i=1;i<=n;i++) puts(s[i]+1);
	}
	else printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		fuck();
	}
 return 0;
}

