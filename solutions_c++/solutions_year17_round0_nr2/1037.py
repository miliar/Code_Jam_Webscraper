#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include <limits.h>
#include<cmath>
#include<map>
#include<queue>
#include<set>
using namespace std;

#define N 100005
#define M 100005
#define LL long long

//为自己加油O(∩_∩)O~

const long long  mod =1000000007;
bool ok(LL a)
{
    if (a<0) return false;
    vector<int> v;
    while (a){
        v.push_back(a%10);
        a/=10;
    }
    vector<int> v1=v;
    sort(v1.rbegin(),v1.rend());
    return v==v1;
}
LL gao(LL a)
{
    if (ok(a)) return a;
    for (LL j=1;j<=1e18;j*=10){
        LL g=a;
        g/=j;
        g*=j;
        g-=1;
        if (ok(g)) return g;
    }
    return 0;
}
int main()
{
    freopen("2.in","r",stdin);
    freopen("1.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int t=T;
    while (T--){
        LL a;
        cin>>a;
        printf("Case #%d: ",t-T);
        cout<<gao(a)<<endl;
    }
    return 0;
}








