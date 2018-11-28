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
char s[22];
int n;
bool ok(){
	for(int i=1;i<n;i++)
		if(s[i]<s[i-1])
			return 0;
	return 1;		
}
int main(){
    freopen("file.in", "r", stdin);
    freopen("file.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
		scanf("%s",s);
		n=strlen(s);
		if(n==1){
			printf("Case #%d: %c\n",test,s[0]);
			continue;
		}
		if(ok()){
			printf("Case #%d: ",test);
			for(int i=0;i<n;i++)
				printf("%c",s[i]);
			puts("");
			continue;	
		}
		int last=s[0]-'0',ok=-1;
		for(int i=1;i<n;i++){
			if(s[i]!='0' and s[i]-'0'-1>=last)
				ok=i-1;
			if(s[i]-'0'<last)
				break;
			last=s[i]-'0';	
		}
		if(~ok){
			printf("Case #%d: ",test);
			for(int i=0;i<=ok;i++)
				printf("%c",s[i]);
			printf("%d",s[ok+1]-'0'-1);
			for(int i=ok+2;i<n;i++)
				printf("9");
			puts("");	
		}
		else{
			printf("Case #%d: ",test);
			if(s[0]!='1')
				printf("%d",s[0]-'0'-1);
			for(int i=0;i<n-1;i++)
				printf("9");
			puts("");	
		}
	}
	return 0;
}
