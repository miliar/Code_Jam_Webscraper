#include <bits/stdc++.h>

using namespace std;
int onecust[1001];
int arr[1001];
int adjmat[1001][1001];
int N,C,M;
pair<bool,int> Check(int Mid)
{
    int Left=0;
    int HadToPromote=0;
    for(int i=1;i<=1000;i++){
        int cur=0;
        for(int j=1;j<=C;j++)
            cur+=adjmat[j][i];
        Left+=(Mid-cur);
        HadToPromote+=max(0,cur-Mid);
        if(Left<0)
            return make_pair(0,0);
    }
    return make_pair(1,HadToPromote);
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    int cases=0;
    scanf("%d",&T);
    while(T--){
        cases++;
        int ans1=1e9,ans2=1e9;
        memset(adjmat,0,sizeof adjmat);
        memset(arr,0,sizeof arr);
        memset(onecust,0,sizeof onecust);
        scanf("%d%d%d",&N,&C,&M);
        for(int i=0;i<M;i++){
            int a,b;
            scanf("%d%d",&a,&b);
            onecust[b]++;
            adjmat[b][a]++;
            arr[a]++;
        }
        int Min=0;
        for(int i=1;i<=1000;i++)
            Min=max(Min,onecust[i]);
        int Max=1000000;
        while(Min<=Max){
            int Mid=(Min+Max)>>1;
            pair<bool,int> cur=Check(Mid);
            if(cur.first&&(Mid<ans1||(Mid<=ans1&&cur.second<=ans2))){
                ans1=Mid;
                ans2=cur.second;
            }
            if(cur.first)
                Max=Mid-1;
            else
                Min=Mid+1;
        }
        cout<<"Case #"<<cases<<": "<<ans1<<" "<<ans2<<endl;
    }
}
