//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

pair<int,int>ar[1000009];
int S[1000009];
int P[1000009];
int N,M,C;

int check(int curr)
{
    int i,j,k,l,temp;

    for(i=1;i<=N;i++) S[i]=curr;

    temp=1;
    for(i=1;i<=M;i++)
    {
        while(!S[temp]) temp++;
        if(temp>ar[i].first) return 0;
        S[temp]--;
    }

    return 1;
}

int BS(int l,int r)
{
    if(l==r) return l;
    if(l==r-1)
    {
        if(check(l)) return l;
        return r;
    }

    int m=l+r;
    m/=2;
    if(check(m)) return BS(l,m);
    return BS(m,r);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int i,j,k,l,n,cas,test,flag,temp,now,m,c,ans1,ans;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n>>c>>m;
        N=n;
        C=c;
        M=m;

        memset(P,0,sizeof(P));

        l=0;
        for(i=1;i<=m;i++)
        {
            scanf("%d%d",&ar[i].first,&ar[i].second);
            P[ar[i].second]++;
            l=max(l,P[ar[i].second]);
        }

        l=max(l,(m+n-1)/n);

        sort(ar+1,ar+1+m);

        ans=BS(l,m);

        for(i=1;i<=n;i++) S[i]=ans;

        ans1=0;
        for(i=1;i<=m;i++)
        {
            for(j=ar[i].first;j>=1;j--)
            {
                if(S[j])
                {
                    S[j]--;
                    if(j!=ar[i].first) ans1++;
                    break;
                }
            }
        }

        printf("Case #%d: %d %d\n",cas,ans,ans1);


    }



}
