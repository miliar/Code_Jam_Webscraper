#include <map>
#include <set>
#include <ctime>
#include <stack>
#include <cmath>
#include <queue>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <iostream>
#include <algorithm>
#pragma comment(linker, "/STACK:1024000000,1024000000")

using namespace std;
#define   maxn          1000+10
#define   maxm          400+10
#define   lson          l,m,rt<<1
#define   rson          m+1,r,rt<<1|1
#define   clr(x,y)      memset(x,y,sizeof(x))
#define   pii           pair<int,int>
#define   mp            make_pair
#define   FI            first
#define   SE            second
#define   IT            iterator
#define   PB            push_back
#define   Times         10

typedef   long long     ll;
typedef   unsigned long long ull;
typedef   long double   ld;

const double eps   = 1e-14;
const double  pi   = acos(-1.0);
const  ll    mod   = 1e9+7;
const  int   inf   = 0x3f3f3f3f;
const  ll    INF   = (ll)1e18+300;
const double delta = 0.98;

using namespace std;

int dat[55][55];
int num[55];
int vis[55];
bool check(int n,int p){
	for(int i=0;i<n;i++)
		if(vis[i]==p)
			return false;
	return true;
}
int main(){
    freopen("D:\\acm\\B-large.in","r",stdin);
	ofstream fout("D:\\acm\\out.txt");
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		int n,p,na,nb;
		scanf("%d %d",&n,&p);
		for(int i=0;i<n;i++)
			scanf("%d",&num[i]);
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++)
				scanf("%d",&dat[i][j]);
			sort(dat[i],dat[i]+p);
		}
		int ans=0;
		clr(vis,0);
		for(int i=1;check(n,p)&&i<=1000000;){
			bool flag=true;
			for(int j=0;j<n;j++){
				double l=0.9*num[j]*i;
				double r=1.1*num[j]*i;
				while(vis[j]<p&&dat[j][vis[j]]<l){
					vis[j]++;
				}
				if(vis[j]==p||dat[j][vis[j]]>r){
					flag=false;
					i++;
					break;
				}
			}
			if(flag){
				ans++;
				for(int j=0;j<n;j++)
					vis[j]++;
			}
		}
		fout<<"Case #"<<cas<<": "<<ans<<endl;
	}
    return 0;
}







