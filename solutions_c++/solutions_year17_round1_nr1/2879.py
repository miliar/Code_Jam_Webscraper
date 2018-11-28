#include<bits/stdc++.h>
using namespace std;

struct box
{
    int xl,yl,xh,yh;
};

void update_box(box& b,pair<int,int>&p)
{
    b.xl = min(b.xl,p.first);
    b.yl = min(b.yl,p.second);
    b.xh = max(b.xh,p.first);
    b.yh = max(b.yh,p.second);
}
bool intersects(box b1,box b2)
{
    if(b1.xl>b2.xl)
        swap(b2,b1);
    if(b2.xl>b1.xh)
        return false;
    if(b2.yl>b1.yh)
        return false;
    if(b2.yh<b1.yl)
        return false;
    return true;


}

int main()
{
    int T;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);

    cin>>T;
    for(int t=1;t<=T;t++)
    {

        int r,c;
        cin>>r>>c;
        vector<string>v;
        for(int i=0;i<r;i++)
        {
            string s;
            cin>>s;
            v.push_back(s);
        }
        vector<box>dq;
        bool visited[30][30];
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(v[i][j]!='?')
                {
                    box b;
                    b.xl = i;
                    b.yl = j;
                    b.xh = i;
                    b.yh = j;
                    memset(visited,false,sizeof(visited));
                    queue<pair<int,int> >q;
                    q.push(make_pair(i,j));
                    pair<int,int>p,p2;
                    while(!q.empty())
                    {
                        p = q.front();
                        q.pop();
                        visited[p.first][p.second] = true;
                        if(p.first-1>=0)
                        {
                            p2.first = p.first-1;
                            p2.second = p.second;
                            if(visited[p2.first][p2.second]==false&&v[p2.first][p2.second]==v[i][j])
                            {
                                update_box(b,p2);
                                q.push(p2);
                            }
                        }

                        if(p.first+1<r)
                        {
                            p2.first = p.first+1;
                            p2.second = p.second;
                            if(visited[p2.first][p2.second]==false&&v[p2.first][p2.second]==v[i][j])
                            {
                                update_box(b,p2);
                                q.push(p2);
                            }
                        }

                        if(p.second-1>=0)
                        {
                            p2.first = p.first;
                            p2.second = p.second-1;
                            if(visited[p2.first][p2.second]==false&&v[p2.first][p2.second]==v[i][j])
                            {
                                update_box(b,p2);
                                q.push(p2);
                            }
                        }

                        if(p.second+1<c)
                        {
                            p2.first = p.first;
                            p2.second = p.second+1;
                            if(visited[p2.first][p2.second]==false&&v[p2.first][p2.second]==v[i][j])
                            {
                                update_box(b,p2);
                                q.push(p2);
                            }
                        }

                    }
                    dq.push_back(b);
                }
            }
        }

        for(int i = 0;i<dq.size();i++)
        {
            box b = dq[i];
            for(int m=b.xl;m<=b.xh;m++)
            {
                for(int n=b.yl;n<=b.yh;n++)
                {
                    v[m][n] = v[b.xh][b.yh];
                }
            }
        }

        for(int i=0;i<r;i++)
        {
            for(int j = 0;j<c;j++)
            {
                if(v[i][j]=='?')
                {
                    for(int m = 0;m<dq.size();m++)
                    {
                        box b1 = dq[m];
                        char c = v[b1.xh][b1.yh];
                        pair<int,int>p;
                        p.first = i;p.second = j;
                        update_box(b1,p);
                        int n;
                        for(n=m+1;n<dq.size();n++)
                        {
                            box b2 = dq[n];
                            if(intersects(b1,b2))
                                break;
                        }
                        if(n==dq.size())
                        {
                            dq.erase(dq.begin()+m);
                            dq.push_back(b1);
                            for(int a=b1.xl;a<=b1.xh;a++)
                            {
                                for(int b=b1.yl;b<=b1.yh;b++)
                                {
                                    v[a][b]=c;
                                }
                            }
                            break;
                        }
                    }

                }
            }
        }
        cout<<"Case #"<<t<<":"<<endl;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
                cout<<v[i][j];
            cout<<endl;
        }
    }
}
