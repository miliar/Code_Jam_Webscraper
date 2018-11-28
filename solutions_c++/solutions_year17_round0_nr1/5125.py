#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int t;
    cin>>t;
    int jj=1;
    string s;
    int k;
    while(t)
    {
        cin>>s>>k;
        //cout<<s<<endl;
        int n=s.length();
        vector<int>ss(n,0);
        for(int i=0;i<n;i++)
        {
            if(s[i]=='-')ss[i]=1;else ss[i]=0;
        }
        vector<int>a(k,0);
        bool ok=true;
        for(int i=0;i<k;i++)
        {
            int j=0;
            while(j+i<n)
            {
                a[i]+=ss[i+j];
                j+=k;
            }
            if(i>0&&a[i]%2!=a[i-1]%2)ok=false;
        }
        if(!ok)
        {
            printf("Case #%d: IMPOSSIBLE\n",jj);
        }
        else
        {
            int res=0;
            for(int i=0;i+k-1<n;i++)
            {
                if(ss[i]==1)
                {
                    res++;
                    for(int j=0;j<k;j++)
                    {
                        ss[i+j]=1-ss[i+j];
                    }
                }
            }
            printf("Case #%d: %d\n",jj,res);
        }
        t--;
        jj++;
    }
    return 0;
}
