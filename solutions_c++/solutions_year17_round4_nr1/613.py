#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define PB push_back
#define MP make_pair

const int INF = 0x3f3f3f3f;
const int mod = 1e9 + 7;
const double eps = 1e-8;
const int maxn = 1e5+5;

int n,p;
int a[maxn];
int b[5];

int main(){
	int T;
	scanf("%d",&T);
	for(int q=1;q<=T;++q){
		scanf("%d%d",&n,&p);
		for(int i=1;i<=n;++i){
			scanf("%d",&a[i]);
		}
		for(int i=0;i<=4;++i)b[i]=0;
		for(int i=1;i<=n;++i){
			b[(a[i]%p)]++;
		}
		int ans=0;
		if(p==2){
			ans=b[0]+(b[1]+1)/2;
		}
		else if(p==3){
			ans=b[0];
			if(b[1]>b[2])swap(b[1],b[2]);
			ans+=b[1];
			b[2]-=b[1];
			ans+=b[2]/3;
			if(b[2]%3)ans++;
		}
		else if(p==4){
			ans=b[0];
			if(b[1]>b[3])swap(b[1],b[3]);
			ans+=b[1];
			b[3]-=b[1];
			int tmp=0;
			for(int i=0;i<=n;++i){
				if(i*4>b[3])break;
				int res=i;
				int t3=b[3]-i*4;
				int t2=b[2];
				if(t3/2>t2){
					res+=t2;
					t3-=2*t2;
					res+=t3/4;
					t3%=4;
					if(t3)res++;
				}
				else{
					res+=t3/2;
					t2-=t3/2;
					t3%=2;
					res+=t2/2;
					t2%=2;
					if(t2||t3)res++;
				}
				if(res>tmp)tmp=res;
			}
			ans+=tmp;
		}
		printf("Case #%d: %d\n",q,ans);

	}
	return 0;
}
