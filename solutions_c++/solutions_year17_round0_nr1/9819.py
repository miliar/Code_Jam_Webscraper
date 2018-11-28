#include<bits/stdc++.h>
using namespace std;
string s;
int K;
int ans=0;
map<string,int>visit;
struct node{
    string p;
    int step;
};
bool check(string a)
{
    for(int i=0;i<a.length();i++)
        if(a[i]=='-')return false;
    return true;
}
void bfs(string t)
{
    queue<node>Q;
    node New;
    New.p=t;
    New.step=0;
    Q.push(New);
    visit[t]=1;
    if(check(t))
    {
        ans=0;return ;
    }
    while(!Q.empty())
    {
        New=Q.front();
        Q.pop();
        for(int i=0;i<t.length()-K+1;i++)
        {
            string tmp=New.p;
            for(int j=i;j<=i+K-1;j++)
            {
                if(tmp[j]=='+')tmp[j]='-';
                else tmp[j]='+';
            }
            if(visit[tmp])continue;
            visit[tmp]=1;
            node next;
            next.p=tmp;next.step=New.step+1;
            Q.push(next);
            if(check(tmp))
            {
                ans=New.step+1;
                return ;
            }
        }
    }
}
int main()
{
    int T;
    int CASE=0;
    cin>>T;
    while(T--)
    {
        visit.clear();
        cin>>s>>K;
        ans=123456789;
        bfs(s);
        if(ans==123456789)
            printf("Case #%d: IMPOSSIBLE\n",++CASE);
        else
            printf("Case #%d: %d\n",++CASE,ans);
    }
    return 0;
}
