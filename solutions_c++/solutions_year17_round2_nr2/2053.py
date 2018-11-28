#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define sz(x) ((int)x.size())
#define clr(a,b) memset(a,b,sizeof(a))
typedef long long ll;
const int maxn=1e3+7;
const int INF=1e9+7;
int n,m,t;
int num[6];
char cc[6]={'R','O','Y','G','B','V'};
struct node{
	int c;
	int cnt;
}a[3];
bool cmp(node n1,node n2){
	return n1.cnt<n2.cnt;
}
int ans[maxn];
int main(){
#ifdef AC
freopen("data.in","r",stdin);
freopen("data2.out","w",stdout);
#endif
	cin>>t;
	int tcase=1;
	while(t--){
		printf("Case #%d: ",tcase++);
		cin>>n;
		for(int i=0;i<6;i++)cin>>num[i];
		a[0].c=0;a[0].cnt=num[0];
		a[1].c=2;a[1].cnt=num[2];
		a[2].c=4;a[2].cnt=num[4];
		sort(a,a+3,cmp);
		if(a[2].cnt>a[1].cnt+a[0].cnt){
			puts("IMPOSSIBLE");
			continue;
		}
//		for(int i=0;i<3;i++){
//			cout<<a[i].c<<" "<<a[i].cnt<<endl;
//		}
		int cnt=a[1].cnt-a[0].cnt;
		a[2].cnt-=cnt;a[1].cnt-=cnt;
		int pos=0;
		for(int i=0;i<cnt;i++)ans[pos++]=a[2].c,ans[pos++]=a[1].c;
		cnt=min(a[2].cnt/2,a[0].cnt);
		a[2].cnt-=2*cnt;a[0].cnt-=cnt;
		for(int i=0;i<cnt;i++){
			ans[pos++]=a[2].c,ans[pos++]=a[1].c;
			ans[pos++]=a[2].c,ans[pos++]=a[0].c;
		}
		if(a[2].cnt)ans[pos++]=a[2].c;
		for(int i=0;i<a[0].cnt;i++)ans[pos++]=a[1].c,ans[pos++]=a[0].c;
		for(int i=0;i<n;i++)cout<<cc[ans[i]];
		cout<<endl;
	}		
	return 0;
}

