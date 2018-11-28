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

char s[30][30];
int main(){
    freopen("D:\\acm\\A-large.in","r",stdin);
	ofstream fout("D:\\acm\\out.txt");
	int t;
    cin>>t;
    int kase=0;
    while(t--){
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++) scanf("%s",s[i]);
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(s[i][j]!='?'){
                    for(int k=j+1;k<c;k++){
                        if(s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                    }
                    for(int k=j-1;k>=0;k--){
                        if(s[i][k]=='?') s[i][k]=s[i][j];
                        else break;
                    }
                }
            }
        }
        for(int i=0;i<r;i++){
            if(s[i][0]!='?'){
                for(int k=i-1;k>=0;k--){
                    if(s[k][0]=='?'){
                        for(int j=0;j<c;j++) s[k][j]=s[i][j];
                    }
                    else break;
                }
                for(int k=i+1;k<r;k++){
                     if(s[k][0]=='?'){
                        for(int j=0;j<c;j++) s[k][j]=s[i][j];
                    }
                    else break;
                }
            }
        }
        kase++;
		fout<<"Case #"<<kase<<":"<<endl;
        for(int i=0;i<r;i++)
			fout<<s[i]<<endl;
    }
    return 0;
}







