#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<map>
#include<cmath>
#include<string>
#define ll long long
using namespace std;
int t,n,m;
int f;
int s[11000];
char a[11000];
int b[500];
char c[100];
bool cmp(char x,char y){
	return b[x]>b[y];
}
int fail(char x,char y){
	int a=0;
	if (x=='R' || x=='O' || x=='V') a+=1;
	if (x=='Y' || x=='O' || x=='G') a+=2;
	if (x=='B' || x=='V' || x=='G') a+=4;
	int b=0;
	if (y=='R' || y=='O' || y=='V') b+=1;
	if (y=='Y' || y=='O' || y=='G') b+=2;
	if (y=='B' || y=='V' || y=='G') b+=4;
	return (a&b);
}
int main(){
	scanf("%d",&t);
	for (int I=1;I<=t;I++){
		scanf("%d%d%d%d%d%d%d",&n,&b['R'],&b['O'],&b['Y'],&b['G'],&b['B'],&b['V']);
		if (b['R']==b['G'] && !b['O'] && !b['Y'] && !b['B'] && !b['V']){
			printf("Case #%d: ",I);
			for (int i=1;i<=b['R'];i++) printf("RG");
			printf("\n");
		}else if (b['O']==b['B'] && !b['R'] && !b['Y'] && !b['G'] && !b['V']){
			printf("Case #%d: ",I);
			for (int i=1;i<=b['O'];i++) printf("OB");
			printf("\n");
		}else if (b['V']==b['Y'] && !b['O'] && !b['R'] && !b['B'] && !b['G']){
			printf("Case #%d: ",I);
			for (int i=1;i<=b['V'];i++) printf("VY");
			printf("\n");
		}else{
			memset(a,0,sizeof(a));
			c[1]='R';c[2]='B';c[3]='Y';
			
			m=0;
			
			b['R']-=b['G'];
			b['B']-=b['O'];
			b['Y']-=b['V'];
			n-=(b['G']+b['O']+b['V'])*2;
			sort(c+1,c+1+3,cmp);
			f=0;
			for (int i=0;i<n;i+=2) s[++f]=i;
			for (int i=1;i<n;i+=2) s[++f]=i;
			for (int i=1;i<=3;i++){
				for (int j=1;j<=b[c[i]];j++)
					a[s[++m]]=c[i];
			}
			f=0;
			if (b['G'] && b['R']<=0) f=1;
			if (b['O'] && b['B']<=0) f=1;
			if (b['V'] && b['Y']<=0) f=1;
			for (int i=0;i<n-1;i++)
				if (a[i]==a[i+1]) f=1;
			if (a[0]==a[n-1]) f=1;
			a[n+1]=0;
			if (f) printf("Case #%d: IMPOSSIBLE\n",I);
			else{
				printf("Case #%d: ",I);
				for (int i=0;i<n;i++){
					printf("%c",a[i]);
					if (a[i]=='R' && b['G']){
						for (int j=0;j<b['G'];j++) printf("GR");
						b['G']=0;
					}else if (a[i]=='B' && b['O']){
						for (int j=0;j<b['O'];j++) printf("OB");
						b['O']=0;
					}else if (a[i]=='Y' && b['V']){
						for (int j=0;j<b['V'];j++) printf("VY");
						b['V']=0;
					}
				}
				printf("\n");
			}	
		}
	}
    return 0;
}

