//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

vector<int>adj[100009],revadj[100009],vec;
int vis[100009],dis[100009],FLAG[100009];
int ar[200][200];
vector<pair<int,int> >vec1,vec2;
int N,M;

int GO(int i,int j)
{
    return (i-1)*M+j;
}

void dfs1(int curr)
{
    int i,siz=adj[curr].size();
    vis[curr]=1;
    for(i=0;i<siz;i++) if(vis[adj[curr][i]]==0) dfs1(adj[curr][i]);
    vec.push_back(curr);
}

void dfs2(int curr,int no)
{
    int i,siz=revadj[curr].size();
    vis[curr]=0;
    dis[curr]=no;
    for(i=0;i<siz;i++) if(vis[revadj[curr][i]]) dfs2(revadj[curr][i],no);
}

int neg(int i,int n)
{
    if(i<=n) return i+n;
    return i-n;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int i,j,k,l,n,m,cas,test,temp,temp1,flag,t,ans;
    char ch;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        cin>>n>>m;
        N=n;
        M=m;

        vec.clear();
        memset(vis,0,sizeof(vis));
        memset(dis,0,sizeof(dis));
        memset(FLAG,0,sizeof(FLAG));
        for(i=0;i<=m*n*2+5;i++)
        {
            adj[i].clear();
            revadj[i].clear();
        }

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                cin>>ch;
                ar[i][j]=ch;
            }
        }

        //cout<<n<<" "<<m<<endl;

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if(ar[i][j]=='-' || ar[i][j]=='|')
                {
                    flag=1;
                    for(k=j+1;k<=m;k++)
                    {
                        if(ar[i][k]=='#') break;
                        if(ar[i][k]=='-' || ar[i][k]=='|')
                        {
                            flag=0;
                            break;
                        }
                    }
                    for(k=j-1;k>=1;k--)
                    {
                        if(ar[i][k]=='#') break;
                        if(ar[i][k]=='-' || ar[i][k]=='|')
                        {
                            flag=0;
                            break;
                        }
                    }

                    if(flag==0)
                    {
                        temp=GO(i,j);
                        if(temp<0) temp=n*m+abs(temp);
                        temp1=temp;

                        //cout<<i<<" a "<<j<<" "<<temp<<" "<<temp1<<endl;

                        adj[neg(temp,n*m)].push_back(temp1);
                        adj[neg(temp1,n*m)].push_back(temp);

                        revadj[temp1].push_back(neg(temp,n*m));
                        revadj[temp].push_back(neg(temp1,n*m));
                    }

                    flag=1;
                    for(k=i+1;k<=n;k++)
                    {
                        if(ar[k][j]=='#') break;
                        if(ar[k][j]=='-' || ar[k][j]=='|')
                        {
                            flag=0;
                            break;
                        }
                    }
                    for(k=i-1;k>=1;k--)
                    {
                        if(ar[k][j]=='#') break;
                        if(ar[k][j]=='-' || ar[k][j]=='|')
                        {
                            flag=0;
                            break;
                        }
                    }

                    if(flag==0)
                    {
                        temp=-GO(i,j);
                        if(temp<0) temp=n*m+abs(temp);
                        temp1=temp;

                        //cout<<i<<" b "<<j<<" "<<temp<<" "<<temp1<<endl;

                        adj[neg(temp,n*m)].push_back(temp1);
                        adj[neg(temp1,n*m)].push_back(temp);

                        revadj[temp1].push_back(neg(temp,n*m));
                        revadj[temp].push_back(neg(temp1,n*m));
                    }
                }
            }
        }

        ans=1;
        for(i=1;i<=n && ans;i++)
        {
            for(j=1;j<=m && ans;j++)
            {
                if(ar[i][j]=='.')
                {
                    vec1.clear();
                    vec2.clear();
                    flag=1;
                    for(k=j+1;k<=m;k++)
                    {
                        if(ar[i][k]=='#') break;
                        if(ar[i][k]=='-' || ar[i][k]=='|')
                        {
                            vec1.push_back(make_pair(i,k));
                            if(vec1.size()>1)
                            {
                                flag=0;
                                break;
                            }
                        }
                    }

                    for(k=j-1;k>=1;k--)
                    {
                        if(ar[i][k]=='#') break;
                        if(ar[i][k]=='-' || ar[i][k]=='|')
                        {
                            vec1.push_back(make_pair(i,k));
                            if(vec1.size()>1)
                            {
                                flag=0;
                                break;
                            }
                        }
                    }

                    for(k=i+1;k<=n;k++)
                    {
                        if(ar[k][j]=='#') break;
                        if(ar[k][j]=='-' || ar[k][j]=='|')
                        {
                            vec2.push_back(make_pair(k,j));
                            if(vec2.size()>1)
                            {
                                flag=0;
                                break;
                            }
                        }
                    }

                    for(k=i-1;k>=1;k--)
                    {
                        if(ar[k][j]=='#') break;
                        if(ar[k][j]=='-' || ar[k][j]=='|')
                        {
                            vec2.push_back(make_pair(k,j));
                            if(vec2.size()>1)
                            {
                                flag=0;
                                break;
                            }
                        }
                    }

                    if(vec1.size()==1 && vec2.size()==1)
                    {
                        temp=-GO(vec1[0].first,vec1[0].second);
                        temp1=GO(vec2[0].first,vec2[0].second);

                        if(temp<0) temp=n*m+abs(temp);
                        if(temp1<0) temp1=n*m+abs(temp1);

                        //cout<<i<<" c "<<j<<" "<<temp<<" "<<temp1<<endl;

                        adj[neg(temp,n*m)].push_back(temp1);
                        adj[neg(temp1,n*m)].push_back(temp);

                        revadj[temp1].push_back(neg(temp,n*m));
                        revadj[temp].push_back(neg(temp1,n*m));
                    }
                    else if(vec1.size()==1)
                    {
                        temp=-GO(vec1[0].first,vec1[0].second);
                        temp1=-GO(vec1[0].first,vec1[0].second);

                        if(temp<0) temp=n*m+abs(temp);
                        if(temp1<0) temp1=n*m+abs(temp1);

                        //cout<<i<<" c "<<j<<" "<<temp<<" "<<temp1<<endl;

                        adj[neg(temp,n*m)].push_back(temp1);
                        adj[neg(temp1,n*m)].push_back(temp);

                        revadj[temp1].push_back(neg(temp,n*m));
                        revadj[temp].push_back(neg(temp1,n*m));
                    }
                    else if(vec2.size()==1)
                    {
                        temp=GO(vec2[0].first,vec2[0].second);
                        temp1=GO(vec2[0].first,vec2[0].second);

                        if(temp<0) temp=n*m+abs(temp);
                        if(temp1<0) temp1=n*m+abs(temp1);

                        //cout<<i<<" c "<<j<<" "<<temp<<" "<<temp1<<endl;

                        adj[neg(temp,n*m)].push_back(temp1);
                        adj[neg(temp1,n*m)].push_back(temp);

                        revadj[temp1].push_back(neg(temp,n*m));
                        revadj[temp].push_back(neg(temp1,n*m));
                    }
                    else ans=0;
                }
            }
        }

        if(ans)
        {
            for(i=1;i<=2*n*m;i++) if(vis[i]==0) dfs1(i);
            t=0;
            for(i=n*m*2-1;i>=0;i--) if(vis[vec[i]]) dfs2(vec[i],++t);

            flag=1;
            for(i=1;i<=n*m;i++)
            {
                if(dis[i]==dis[i+n*m])
                {
                    flag=0;
                    break;
                }
            }

            if(flag==0) printf("Case #%d: IMPOSSIBLE\n",cas);
            else
            {
                printf("Case #%d: POSSIBLE\n",cas);

                for(i=1;i<=n*m;i++)
                {
                    if(dis[i]>dis[i+n*m]) FLAG[i]=1;
                }

                for(i=1;i<=n;i++)
                {
                    for(j=1;j<=m;j++)
                    {
                        if(ar[i][j]!='|' && ar[i][j]!='-') printf("%c",ar[i][j]);
                        else
                        {
                            if(FLAG[GO(i,j)]) printf("|");
                            else printf("-");
                        }
                    }

                    cout<<endl;
                }
            }
        }
        else printf("Case #%d: IMPOSSIBLE\n",cas);

    }



}
