#include <bits/stdc++.h>

using namespace std;
int t,n,k;
string s;
int lev[(int)(1<<11)];
int goal(0);

void affich(int so)
{
    for(int i=0; i<(int)s.size(); i++)
    {
        cout<<(1&(so>>i));
    }
    cout<<endl;
}

int bfs(int so)
{
    queue<int> q;
    q.push(so);
    memset(lev,-1,sizeof lev);
    lev[so] = 0;
    while(!q.empty())
    {
        int u = q.front();
       // affich(u);
        q.pop();
        int aux(0);
        if(u == goal) return lev[u];
        for(int i=0; i<(int)s.size() - k + 1; i++)
        {
            aux = u;
            for(int j=i; j<i+k; ++j)
            {
                aux ^= (1<<j);
            }
            //affich(aux);
            if(lev[aux] == -1)
            {
                lev[aux] = 1 + lev[u];
                q.push(aux);
            }
        }
        //return 0;
    }
    return -1;

}

int main()
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("out");
    cin>>t;
    int tc(1);
    while(t--)
    {
        cin>>s>>k;
        n = 0;
        int l = (int)s.size();
        goal = (1<<l)- 1;
        for(int i=0; i<(int)s.size(); i++)
        {
            n*=2;
            if(s[i] == '+')
            {
                n += 1;
            }
        }
        int ans = bfs(n);
        cout<<"Case #"<<tc++<<": ";
        if(ans > -1)
        {
            cout<<ans<<endl;
        }
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
