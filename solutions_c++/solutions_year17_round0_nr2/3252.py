#include <bits/stdc++.h>
using namespace std;
int t,n;
char a[20];
int num[20],ans[20];
int no;
int len;
long long save[2][20][10];
int mark[2][20][10];
long long re(int m,int pos, int put) {
	if(mark[m][pos][put]==no) return save[m][pos][put];
	mark[m][pos][put] = no;
	save[m][pos][put]=0;
	if(pos==len) save[m][pos][put]=1;
	else {
		if(!m) {
			save[m][pos][put]+=re(0,pos+1,put);
			if(put!=9) save[m][pos][put]+=re(0,pos,put+1);
		}
		else {
			if(put>num[pos]) return 0;
			if(put<num[pos]) {
				save[m][pos][put]+=re(0,pos+1,put);
				if(put!=9) save[m][pos][put]+=re(1,pos,put+1);
			}
			else {
				save[m][pos][put]+=re(1,pos+1,put);
			}
		}
	}
	//printf("%d %d %d := %lld\n",m,pos,put,save[m][pos][put]);
	return save[m][pos][put];
}
int main() {
	cin >> t;
	while(t--) {		
		no++;
		scanf("%s",a);
		len = strlen(a);
		for(int i=0;i<len;i++) num[i]=a[i]-'0';
		int m = 1;
		int m2 = 0;
		printf("Case #%d: ",no);
		for(int i=0;i<len;i++) {
			for(int j=9;j>=0;j--) {
				if(re(m,i,j)>0) {
					ans[i]=j;
					break;
				}
			}
			if(m==1 && ans[i]!=num[i]) m=0;
			if(m2==0 && ans[i]!=0) m2=1;
			if(m2==1) printf("%d",ans[i]);
		}
		printf("\n");
	}
}