#include<bits/stdc++.h>

using namespace std;

pair < int , int > ti[1010];

set < int > S[1010];

set < pair<int,int> > H;
set<pair<int,int>>::iterator it;

int co[1010];
void solve(int t)
{
    H.clear();
    int n,k,m;
    scanf("%d%d%d",&n,&k,&m);
    for ( int c=1 ; c<=n ; c++ )    co[c] = 0;
    for ( int c=1 ; c<=m ; c++ )
    {
        scanf("%d%d",&ti[c].first,&ti[c].second);
        co[ti[c].first]++;
    }
    sort(ti+1,ti+1+m);
    int nt = 1;
    S[1].clear();
    S[1].insert(ti[1].second);
    H.insert({1,1});
    for ( int c=2 ; c<=m ; c++ )
    {
        bool sai = false;
        for ( it = H.begin() ; it != H.end() ; it++ )
        {
            pair<int,int> temp = *it;
            int d = temp.second;
            if ( S[d].size() < ti[c].first )
            {
                if ( S[d].find(ti[c].second) == S[d].end() )
                {
                    sai = true;
                    S[d].insert(ti[c].second);
                    H.erase(it);
                    H.insert({temp.first+1,d});
                    break;
                }
            }
        }
        if ( !sai )
        {
            nt++;
            S[nt].clear();
            S[nt].insert(ti[c].second);
            H.insert({1,nt});
        }
    }
    //printf("%d\n",nt);
    int ans = 0;
    for ( int c=1 ; c<=n ; c++ )
    {
        if ( co[c] > nt )   ans += co[c]-nt;
    }
    printf("Case #%d: %d %d\n",t,nt,ans);
}
int main()  {
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for ( int c=1 ; c<=t ; c++ )    solve(c);
}
