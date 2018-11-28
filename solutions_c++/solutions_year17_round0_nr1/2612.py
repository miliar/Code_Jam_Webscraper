#include "bits/stdc++.h"
#define MAXN 100009
#define INF 1000000007
#define mp(x,y) make_pair(x,y)
#define all(v) v.begin(),v.end()
#define pb(x) push_back(x)
#define wr cout<<"----------------"<<endl;
#define ppb() pop_back()
#define tr(ii,c) for(typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define ff first
#define ss second
#define my_little_dodge 46
using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
template<class T>bool umin(T& a,T b){if(a>b){a=b;return 1;}return 0;}
template<class T>bool umax(T& a,T b){if(a<b){a=b;return 1;}return 0;}
const int N=1e3+9;
char s[N];
int main(){
    freopen("file.in", "r", stdin);
    freopen("file.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
		scanf("%s",s);
		int n=strlen(s),k,ans=0,flag=0;
		scanf("%d",&k);
		for(int i=0;i<n;i++){
			if(s[i]=='+')
				continue;
			for(int j=i;j<i+k;j++){
				if(j>=n){
					flag=true;
					break;
				}
				if(s[j]=='+')
					s[j]='-';
				else
					s[j]='+';
			}		
			ans++;
		}
		if(flag)
			printf("Case #%d: IMPOSSIBLE\n",test);
		else
			printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
