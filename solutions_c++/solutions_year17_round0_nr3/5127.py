#include <bits/stdc++.h>

#define MAX 100000
#define INF 2000000000

typedef long long ll;
typedef unsigned long long llu;

using namespace std;

void IO()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small.txt","w",stdout);
}

vector < int > v;

void Fun(int n)
{
    if(n==1)return;
    if(n%2==0){
        Fun(n/2);
        v.push_back(n/2);
        if(((n/2)-1)!=0){
            Fun((n/2)-1);
            v.push_back((n/2)-1);
        }
    }
    else{
        Fun(n/2);
        v.push_back(n/2);
        Fun(n/2);
        v.push_back(n/2);
    }
}

int main()
{
    //IO();
    int t,n,k;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d %d",&n,&k);
        printf("Case #%d: ",i);
        v.clear();
        v.push_back(n);
        Fun(n);
        sort(v.rbegin(),v.rend());
        int m=v[k-1];
        if(m%2==0)printf("%d %d\n",m/2,(m/2)-1);
        else printf("%d %d\n",m/2,m/2);
    }
    return 0;
}
