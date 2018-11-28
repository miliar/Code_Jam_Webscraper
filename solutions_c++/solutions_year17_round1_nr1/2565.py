#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include<cmath>
#include <cstring>
#include <map>
#define fi first
#define se second
#define INF 0x3f3f3f3f
using namespace std;
const int MOD = 1e9+7;
const int MAX_P = 2e4+10;
const int maxn =5e5+10;
const int MAX_V = 5e5+10;
const int maxv = 1e6+10;
typedef long long LL;
typedef pair<int,int> Pair;

int prime[maxn],mu[maxn],cnt;
LL sum_mu[maxn][20];
LL num[maxn];//分解质因数个数
int n,m,p;

char a[30][30];
    int r,c;
void tianchong(int x,int y,int flag){
    int ok = -1;
    for(int i = x ; i<r ; ++i){
        if(a[i][y] !='?'){
            ok = i ; break;
        }
    }
    if(ok == -1){
        if(x>0 &&a[x-1][y] !='?'){
            for(int i =x ; i<r ; ++i)
                a[i][y] = a[x-1][y];
        }else{
            if(flag == -1){
                if(y>0){
                    for(int i = x ; i<r ; ++i){
                        a[i][y] =a[i][y-1];
                    }
                }
            }else{
                if(y<c-1){
                    for(int i = x ; i<r ; ++i)
                        a[i][y] = a[i][y+1];
                }
            }
        }
    }else{
        for(int i=  x ; i<ok ; ++i)
            a[i][y] = a[ok][y];
    }
}

int main(int argc, char const *argv[]) {
    int T;
    int kase = 0;
    cin>>T;
    while (T--) {

        scanf("%d%d", &r,&c);
        for(int i=0 ; i<r ; ++i)
            scanf("%s", a[i]);
        // for(int i=0 ; i<r ; ++i)
        //     printf("%s\n",a[i] );
        for(int i= 0 ; i<c ; ++i)
            for(int j = 0 ; j<r;  ++j)
                if(a[j][i] =='?'){
                    tianchong(j,i,-1);
                }
        for(int i = c-1 ; i>=0 ; --i)
            for(int j = 0 ; j<r ; ++j)
                if(a[j][i]=='?'){
                    tianchong(j,i,1);
                }

        printf("Case #%d:\n", ++kase);
        for(int i=0 ; i<r ; ++i){
            for(int j=0 ; j<c ; ++j)
                printf("%c",a[i][j]);
            putchar('\n');
        }
    }
  return 0;
}
