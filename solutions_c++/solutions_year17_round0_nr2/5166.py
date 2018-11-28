#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#define ll long long
using namespace std;
int T,a[25],l;
char s[25];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("21.out","w",stdout);
	scanf("%d",&T);
	for(int k=1;k<=T;k++){
		scanf("%s",s+1);
		l=strlen(s+1);
		for(int i=1;i<=l;i++) a[i]=s[i]-'0';
		printf("Case #%d: ", k);
		if(l==1) printf("%d\n", a[1]);
		else{
			int tg=l+1;
			for(int i=l-1;i>0;i--){
				if(a[i]>a[i+1]){
					tg=i+1;
					a[i]=(a[i]+9)%10;
					}
				}
			int i=1;
			while(a[i]<=0&&i<tg) i++;
			while(i<tg) {printf("%d",a[i]); i++;}
			while(i<=l) {printf("9"); i++;}
			puts("");
			}
		}
	return 0;
	}
