// Author : Muhammad Rifayat Samee
// Problem : A
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<complex>
#include<valarray>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;

int main(){

	freopen("A_L.in","r",stdin);
	//freopen("A_l.out","w",stdout);
    int cases,i,j,K,ct=1;
    char str[1005];
    scanf("%d",&cases);
    while(cases--){
        scanf("%s %d",str,&K);
        int len = strlen(str);
        int flag = 0;
        int res = 0;
        for(i=len-1;i>=0;i--){
            if(str[i] == '-'){
                if(i-K+1>=0){
                    for(j=i-K+1;j<=i;j++){
                        if(str[j] == '-')str[j] = '+';
                        else
                            str[j] = '-';
                    }
                    res++;
                }
                else{
                    flag = 1;
                    break;
                }
            }
        }
        printf("Case #%d: ",ct++);
        if(flag == 1){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("%d\n",res);
        }
    }

	return 0;
}
