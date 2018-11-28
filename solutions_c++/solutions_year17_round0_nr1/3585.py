#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cmath>
#include<string>
#include<map>
#include<list>
#include<queue>
#include<utility>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<math.h>
#include<set>
#include<stack>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<iterator>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int test,casio=1,i,j,k,l,m,cnt;
    scanf("%d",&test);
    while(test--){
    char str[1200];
    cnt=0;
    int ck=1;
    scanf("%s%d",str,&k);
    l=strlen(str);
    for(i=0;str[i];i++){
        if(str[i]=='+')continue;
        if((i+k-1)>=l)break;
        cnt++;
        m=k;
        for(int j=i;str[j]&&m;j++){
                m--;
            if(str[j]=='+')str[j]='-';
            else str[j]='+';
        }
    }
    for(i=0;str[i];i++){
        if(str[i]=='-')ck=-1;
    }
    if(ck==-1)printf("Case #%d: IMPOSSIBLE\n",casio++);
    else printf("Case #%d: %d\n",casio++,cnt);
}
}
