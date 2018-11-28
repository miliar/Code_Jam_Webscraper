// Lavina Jain
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define INF 1e20
#define MAX 1000000007
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL);
#define cases int t; cin>>t; while(t--)

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

int main()
{
    int i,j,t,z,r,c,ind,index;
    bool flag;
    char ch,ar[27][27];
    cin>>t;
    for(z=1;z<=t;z++)
    {
        cin>>r>>c;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                cin>>ch;
                ar[i][j]=ch;
            }
        }


        for(i=0;i<r;i++)
        {
            flag=0;
            for(j=0;j<c;j++)
            {
                if(ar[i][j]!='?')
                {
                    if(!flag)
                    {
                        index=j;
                        ch=ar[i][j];
                        flag=1;
                    }
                    else
                    {
                        for(int k=index+1;k<j;k++)
                        {   
                            ar[i][k]=ch;
                        }
                        index=j;
                        ch=ar[i][j];
                    }
                }
            }
            if(flag && ar[i][c-1]=='?')
            {
                for(int k=index+1;k<c;k++)
                {
                    ar[i][k]=ch;
                }
            }
        }


        for(i=0;i<r;i++)
        {
            flag=0;
            for(j=c-1;j>=0;j--)
            {
                if(ar[i][j]!='?')
                {
                    if(!flag)
                    {
                        index=j;
                        ch=ar[i][j];
                        flag=1;
                    }
                    else
                    {
                        for(int k=index-1;k>j;k--)
                        {   
                            ar[i][k]=ch;
                        }
                        index=j;
                        ch=ar[i][j];
                    }
                }
            }
            if(flag && ar[i][0]=='?')
            {
                for(int k=index-1;k>=0;k--)
                {
                    ar[i][k]=ch;
                }
            }
        }


        for(i=0;i<c;i++)
        {
            flag=0;
            for(j=0;j<r;j++)
            {
                if(ar[j][i]!='?')
                {
                    if(!flag)
                    {
                        index=j;
                        ch=ar[j][i];
                        flag=1;
                    }
                    else
                    {
                        for(int k=index+1;k<j;k++)
                        {
                            ar[k][i]=ch;
                        }
                        index=j;
                        ch=ar[j][i];
                    }
                }
            }
            if(flag && ar[r-1][i]=='?')
            {
                for(int k=index+1;k<r;k++)
                {
                    ar[k][i]=ch;
                }
            }
        }

        
        
        for(i=0;i<c;i++)
        {
            flag=0;
            for(j=r-1;j>=0;j--)
            {
                if(ar[j][i]!='?')
                {
                    if(!flag)
                    {
                        index=j;
                        ch=ar[j][i];
                        flag=1;
                    }
                    else
                    {
                        for(int k=index-1;k>j;k--)
                        {
                            ar[k][i]=ch;
                        }
                        index=j;
                        ch=ar[j][i];
                    }
                }
            }
            if(flag && ar[0][i]=='?')
            {
                for(int k=index-1;k>=0;k--)
                {
                    ar[k][i]=ch;
                }
            }
        }
        
        cout<<"Case #"<<z<<":\n";
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                cout<<ar[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}
