#include<bits/stdc++.h>

using namespace std;

pair < int , int > St[1010];
pair < int , int > Ed[1010];

vector < int> workm,workf;

void solve(int t)
{
    int s1,s2,a,b;
    int m = 720,f = 720;
    scanf("%d%d",&s1,&s2);
    int co = 1;
    for ( int c=1 ; c<=s1 ; c++ )
    {
        scanf("%d%d",&a,&b);
        f -= b-a;
        St[co].first = a;
        St[co].second = 2;
        Ed[co].first = b;
        Ed[co].second = 2;
        co++;
    }
    for ( int c=1 ; c<=s2 ; c++ )
    {
        scanf("%d%d",&a,&b);
        m -= b-a;
        St[co].first = a;
        St[co].second = 1;
        Ed[co].first = b;
        Ed[co].second = 1;
        co++;
    }
    int ans = 0;
    int n = (co-1);
    sort(St+1,St+1+n);
    sort(Ed+1,Ed+1+n);
    workm.clear();
    workf.clear();
    for ( int c=1 ; c<n ; c++ )
    {
        if ( Ed[c].second != St[c+1].second ) ans++;
        else if ( Ed[c].second == 1 )
        {
            workm.push_back(St[c+1].first-Ed[c].first);
        }
        else
        {
            workf.push_back(St[c+1].first-Ed[c].first);
        }
    }
    if ( Ed[n].second != St[1].second ) ans++;
    else if ( Ed[n].second == 1 )
    {
        workm.push_back(1440+St[1].first-Ed[n].first);
    }
    else
    {
        workf.push_back(1440+St[1].first-Ed[n].first);
    }
    sort(workm.begin(),workm.end());
    sort(workf.begin(),workf.end());
    /*printf("%d %d\n",workm.size(),workf.size());
    printf ("m = %d f = %d\n",m,f);
    printf("%d\n",ans);*/
    for ( int c=0 ; c<workm.size() ; c++ )
    {
        if ( m < workm[c] )
        {
            ans += 2*(workm.size()-c);
            break;
        }
        else m -= workm[c];
    }
    for ( int c=0 ; c<workf.size() ; c++ )
    {
        //printf("FF%d %d\n",f,workf[c]);
        if ( f < workf[c] )
        {
            //printf("!!!%d\n",c);
            ans += 2*(workf.size()-c);
            break;
        }
        else f -= workf[c];
    }
    //printf("List\n");
    /*for ( int c=1 ; c<=n ; c++ )
    {
        printf("%d %d\n",S[c].first,S[c].second);
    }*/
    printf("Case #%d: %d\n",t,ans);
}
int main()  {
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for ( int c=1 ; c<=t ; c++ )    solve(c);
}
