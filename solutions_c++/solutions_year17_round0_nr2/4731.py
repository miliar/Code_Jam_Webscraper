// Author : Muhammad Rifayat Samee
// Problem : B
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

	freopen("B-l.in","r",stdin);
	//freopen("B_l.out","w",stdout);
    int cases,i,j,k,ct=1;
    char str[25];
    scanf("%d",&cases);
    while(cases--){
        scanf("%s",str);
        int len = strlen(str);
        k = -1;
        j = -1;
        for(i=1;i<len;i++){
            if(str[i]<str[i-1]){
                j = i-1;
                str[j] = str[j] - 1;
                break;
            }
        }
        //printf("%d\n",j);
        int k;
        k = j;

        for(i=j-1;i>=0;i--){
            if(str[i]>str[i+1]){
                k = i;
                str[i] = str[i] - 1;
            }
            else{
                break;

            }
        }
        if(k != -1){
            //str[k] = str[k] - 1;
            for(i=k+1;i<len;i++){
                str[i] = '9';
            }
        }
        if(str[0] == '0')
            printf("Case #%d: %s\n",ct++,str+1);
        else
        printf("Case #%d: %s\n",ct++,str);
    }

	return 0;
}
