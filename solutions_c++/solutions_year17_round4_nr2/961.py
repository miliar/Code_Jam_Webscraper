#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

int n,m;
int t;
int a[1011],b[1011];
int na,nb;
int a1,b1;
int ans;
struct node{
       int num,next;
       };

node e[2000011];
int edge[100011];
int taile;

bool used[100011];
int match[100011];

bool dfs(int now)
{
    used[now]=true;
    //cout<<now<<"@@@"<<endl;
    int i,u,w;
    
    for(i=edge[now];i!=-1;i=e[i].next)
    {
        u=e[i].num;
        w=match[u];
        if(w<0 || !used[w] && dfs(w))
        {
            match[now]=u;
            match[u]=now;
            return true;
        }
    }
    return false;
}

void add(int xx,int yy)
{
    e[taile].num=yy;
    e[taile].next=edge[xx];
    edge[xx]=taile++;
}

int bi()
{
    int i,j;
    memset(edge,-1,sizeof(edge));
    taile=1;
    
    for(i=1;i<=na;i++)
    {
        for(j=1;j<=nb;j++)
        {
            if(a[i]!=b[j])
            {
                //cout<<i<<' '<<na+j<<endl;
                add(i,na+j);
                add(na+j,i);
            }
        }
    }
    
    //cout<<"!!!!"<<endl;
    /*
    for(i=edge[98];i!=-1;i=e[i].next)
    {
        cout<<e[i].num<<' ';
    }
    cout<<"   ^^^"<<endl;
    */
    int res=0;
    memset(match,-1,sizeof(match));
    for(i=1;i<=na+nb;i++)
    {
        //cout<<i<<"   @@@"<<endl;
        if(match[i]<0)
        {
             memset(used,0,sizeof(used));
             if(dfs(i))
             {
                 res++;
             }
        }
    }
    return res;
}
int c;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    int i,j,k,times;
    int xx,yy,zz;
    cin>>t;
    for(times=1;times<=t;times++)
    {
        cin>>n>>c>>m;
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        a1=b1=0;
        na=nb=0;
        for(i=1;i<=m;i++)
        {
            cin>>xx>>yy;
            if(yy==1)
            {
                if(xx==1)
                {
                    a1++;
                    continue;
                }
                na++;
                a[na]=xx;
            }
            else
            {
                if(xx==1)
                {
                    b1++;
                    continue;
                }
                nb++;
                b[nb]=xx;
            }
        }
        
        int ans1,ans2;
        ans1=max(a1+na,b1+nb);
        
        //cout<<a1<<' '<<na<<' '<<b1<<' '<<nb<<" !!!"<<endl;
        ans=bi();
        int a2,b2;
        a2=na-ans;
        b2=nb-ans;
        
        
        //cout<<a1<<' '<<b1<<' '<<a2<<' '<<b2<<"  !!!!"<<endl;
        
        int uu;
        uu=min(a1,b2);
        a1-=uu;b2-=uu;
        uu=min(a2,b1);
        a2-=uu;b1-=uu;
        
        
        uu=min(min(a1,b1),ans);
        a1-=uu;
        b1-=uu;
        
        ans1+=min(a1,b1);
        ans2=min(a2,b2);
        
        cout<<"Case #"<<times<<": "<<ans1<<" "<<ans2<<endl;
    }
    
    
    return 0;
} 
