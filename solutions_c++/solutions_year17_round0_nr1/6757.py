#include<bits/stdc++.h>
#define IN freopen("in.txt","r",stdin);
#define OUT freopen("out.txt","w",stdout);
using namespace std;
const int N = 1010;
int k;
char s[N];
bitset<N> t,t2;
int main(){
	IN
	OUT
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++){
		scanf("%s %d",s,&k);
		t2.reset();
		for(int  i = 0;i<k;i++) t2.set(i);
		int len = strlen(s);	
		//cout<<len<<endl;
		t.reset();
		for(int i =0;i<len;i++) if(s[i]=='-') t.set(i);
		bool flag = true;
		int ans = 0;
		for(int i =0;i<len;i++){
			if(t[i]==1){
				if(i+k<=len){
					ans++;
					t^=t2<<i;
				} else flag = false;
			}
		}
		printf("Case #%d: ",test);
		if(flag) printf("%d\n",ans); else puts("IMPOSSIBLE");
	}
	return 0;
}
