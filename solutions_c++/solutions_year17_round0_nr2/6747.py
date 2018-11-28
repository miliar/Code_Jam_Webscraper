#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
LL getAns(char s[]) {
	int n = strlen(s);
	bool flag = true;
	int now = 0,nowidx = -1;
	for (int i=0;i<n;i++) {
		if (s[i] == now) continue;
		else if (s[i] > now) {
			now = s[i];
			nowidx = i;
		}
		else {
			s[nowidx]--;
			for (int j=nowidx + 1;j < n;j++) s[j] = '0' + 9;
			break;
		}
	}
	long long ret = 0;
	for (int i=0;i<n;i++) ret = ret * 10 + s[i] - '0';
	return ret;
}
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d\n",&T);
	for (int test = 1;test <= T;test++) {
		printf("Case #%d: ",test);
		char s[30];
		scanf("%s",s);
		cout<<getAns(s)<<endl;
	}
}
