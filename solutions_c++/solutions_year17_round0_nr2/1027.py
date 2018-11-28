#include<bits/stdc++.h>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 
void RI(){}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
using namespace std;
typedef long long LL;
int t,len;
char in[30];
bool check(LL x)
{
	char tmp[30];
	sprintf(tmp, "%lld", x);
	int nn = strlen(tmp);
	REP(i,1,nn-1) if(tmp[i]<tmp[i-1]) return false;
	return true;
}
int main()
{
	RI(t);
	REP(tt,1,t)
	{
		scanf("%s",in+1); len=strlen(in+1);

		LL ans;
		FORD(pos,len,1)
		{
			char tmp = in[pos+1];
			in[pos+1]='\0';
			sscanf(in+1, "%lld", &ans);
			REP(i,1,len-pos) ans*=10;
			if(pos!=len) ans--;
			in[pos+1] = tmp;

			if(check(ans)) break;
		}

		printf("Case #%d: %lld\n",tt,ans);
	}
	return 0;
}

