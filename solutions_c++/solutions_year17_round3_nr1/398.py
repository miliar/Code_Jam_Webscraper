#include <bits/stdc++.h>

using namespace std;
vector<pair<long double,long double> > SortedCakes;
int N,K;
long double DP[1001][1001];
long double solve(int idx,int Left)
{
    if(Left==0||idx==N)
        return 0;
    long double &ret=DP[idx][Left];
    if(ret>=0)
        return ret;
    ret=0;
    long double add=0;
    if(Left==K)
        add=(long double)acos(-1)*SortedCakes[idx].first*SortedCakes[idx].first;
    ret=max(ret,solve(idx+1,Left));
    ret=max(ret,solve(idx+1,Left-1)+add+2*acos(-1)*SortedCakes[idx].first*SortedCakes[idx].second);
    return ret;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    int cases=0;
    scanf("%d",&T);
    while(T--){
        SortedCakes.clear();
        cases++;
        scanf("%d%d",&N,&K);
        for(int i=0;i<=1000;i++)
            for(int j=0;j<=1000;j++)
            DP[i][j]=-1;
        for(int i=0;i<N;i++){
            int a,b;
            scanf("%d%d",&a,&b);
            SortedCakes.push_back(make_pair(a,b));
        }
        sort(SortedCakes.rbegin(),SortedCakes.rend());
        cout<<"Case #"<<cases<<": "<<fixed<<setprecision(6)<<solve(0,K)<<endl;
    }
    return 0;
}
