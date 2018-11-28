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

inline void RI(int& x)
{
    x=0;
    char c=getchar();
    while(!((c>='0'&&c<='9')||c=='-'))c=getchar();
    bool flag=1;
    if(c=='-')
    {
        flag=0;
    }
    while(c<='9'&&c>='0')
    {
        x=x*10+c-'0';
        c=getchar();
    }
    if(!flag)x=-x;
}

/*--------------------------------------------------*/

char dat[100];
int main(){	
	freopen("D:\\acm\\B-large.in","r",stdin);
	ofstream fout("D:\\acm\\out.txt");
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		fout<<"Case #"<<cas<<": ";
		scanf("%s",dat);
		int len=strlen(dat);
		for(int i=0;i<len-1;i++)
			if(dat[i]>dat[i+1]){
				dat[i]--;
				for(int j=i+1;j<len;j++)
					dat[j]='9';
				for(int j=i;j>0;j--)
					if(dat[j]<dat[j-1]){
						dat[j]='9';
						dat[j-1]--;
					}
				break;
			}
		if(dat[0]=='0')fout<<dat+1<<endl;
		else fout<<dat<<endl;
	}
	return 0;
}
