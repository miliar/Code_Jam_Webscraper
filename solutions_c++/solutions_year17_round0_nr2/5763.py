//B
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<ctime>
#include<cassert>
#include<algorithm>
#include<cmath>

#include<cstring>
#include<string>
#include<cctype>
#include<utility>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<list>

typedef long long ll;
typedef std::pair<int,int> pii;
typedef std::pair<ll,ll> pll;
typedef std::vector<int> vi;

const int OO=(int)2e9;
const ll INF=(ll)4e18;
const double EPS=(double)1e-12;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front

#define INL(i,a,b) ((a<=i)&&(i<=b))
#define EXL(i,a,b) ((a< i)&&(i< b))
#define REPP(i,a,b,c) for(int i=a;i<=b;i+=c)
#define REP(i,a,b) REPP(i,a,b,1)
#define REVV(i,a,b,c) for(int i=a;i>=b;i-=c)
#define REV(i,a,b) REVV(i,a,b,1)
using namespace std;

int t,l,temp;
char s[25];

int main(){
	scanf("%d",&t);
	REP(tc,1,t){
		scanf("%s",s);
		l=strlen(s);
		if(l>1){
			temp=1;
			REP(i,1,l-1){
				if(s[i-1]>s[i]){
					s[temp-1]--;
					REP(j,temp,l-1)s[j]='9';
					break;
				}
				if(s[i-1]<s[i])temp=i+1;
			}
			if(s[0]=='0') REP(i,1,l)s[i-1]=s[i];
		}
		printf("Case #%d: %s\n",tc,s);
	}
	return 0;
}
