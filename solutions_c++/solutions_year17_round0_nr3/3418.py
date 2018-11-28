#include <bits/stdc++.h>
using namespace std;

vector<pair<int,int> >A;
void dfs(int n)
{
    if(n==0) return;
    int l=(n-1)/2;
    int r=n/2;
    A.push_back(make_pair(l,r));
    dfs(l);
    dfs(r);
}
int n,k;
void bfs(int n)
{
    queue<int>q;
    q.push(n);
    while(!q.empty())
    {
        int k=q.front();q.pop();
        if(k==0) continue;
        int l=(k-1)/2;
        int r=(k)/2;

        A.push_back(make_pair(l,r));
        q.push(r);
        q.push(l);
        if(A.size()>n) break;
    }
}
bool cmp(const pair<int,int>& a,const pair<int,int>& b)
{
    if(a.first==b.first) return a.second>b.second;
    return a.first>b.first;
}
int main()
{
    int T;
    int n,k;
    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        cin>>n>>k;
        A.clear();
        bfs(n);
        sort(A.begin(),A.end(),cmp);
        cout<<"Case #"<<cas<<": "<<A[k-1].second<<" "<<A[k-1].first<<endl;
    }
    return 0;
}
