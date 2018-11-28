#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int b[t];
    for(int i=0;i<t;i++)
    {
        b[i]=0;
        string s;
        int k;
        cin>>s>>k;
        int u=s.size();
        char o[u];
        strcpy(o,s.c_str());
        int rt[u];
        int sum=0;
        for(int y=0;y<u;y++)
        {
            if(o[y]=='+')
            {
                rt[y]=0;
            }
            else
                rt[y]=1;
        sum=sum+rt[y];
        }
        if(sum==0)
        {
            b[i]=0;
            continue;
        }
        sum=0;
        for(int y=0;y<u;y++)
        {
            if(rt[y]==1)
            {
                if(y+k<=u)
                {
                    for(int oop=y;oop<k+y;oop++)
                    {
                        if(rt[oop]==1)
                        {
                            rt[oop]--;
                        }
                        else
                            rt[oop]++;
                    }
                    b[i]=b[i]+1;
                }
                else
                {
                    b[i]=-1;
                    break;
                }
            }
        }
    }
    for(int i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        if(b[i]==-1)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
            cout<<b[i]<<"\n";
    }
    return 0;
}
