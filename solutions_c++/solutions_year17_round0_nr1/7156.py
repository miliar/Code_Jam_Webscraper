#include<cstdio>
char str[10003];
char no(char a) {
	if(a=='+') return '-'; return '+';
}
int inv(int a,int b) {
	for(int i=a;i<a+b;i++) 
		str[i]=no(str[i]);
	return 0;
}
int check() {
	for(int i=0;str[i];i++)
		if(str[i]=='-') return 0;
	return 1;
}
int main () {
	int T;scanf("%d",&T);
	for(int t=0;t<T;t++) {
		int k,ans=0;
		scanf("%s%d",str,&k);
		int l=0;for(;str[l];l++);
		for(int i=0;i<=l-k;i++) {
			if(str[i]=='-') {
				ans++;
				inv(i,k);
			}
			//printf("%s\n",str);
		}
		printf("Case #%d: ",t+1);
		if(check()) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
