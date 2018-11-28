#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int main()
{
    int T;
    freopen("C-small-1-attempt1.in","r",stdin);
    freopen("cout.txt","w",stdout);
    cin>>T;
    for (int j=1;j<=T;j++)
    {
        int n,k;
        cin>>n>>k;
        vector<bool> ar(n+2,0);
        ar[0] = 1;
        ar[n+1] = 1;
        int in=1, len=0, sflag=0, maxl=0, maxin=0, cri=0, ls=0, rs=0;
        while(k!=0)
        {
            for (int i=1;i<=n+1;i++)
            {
                if(ar[i]==0)
                {
                    if (sflag==0)
                    {
                        in = i;
                        len=1;
                        sflag=1;
                    }
                    else
                    {
                        len++;
                    }
                }
                else
                {
                    sflag=0;
                    if(len>maxl)
                    {
                        maxl=len;
                        maxin=in;
                    }
                }
            }
            if(maxl%2)
            {
                cri = maxin + (maxl/2);
            }
            else
            {
                cri = maxin + (maxl/2) - 1;
            }
            ar[cri] = !ar[cri];
            k -= 1;
            if(k)
            {
                maxin=0;
                maxl=0;
                len=0;
            }
        }
        ls = cri-maxin;
        rs = maxin + maxl - cri - 1;
        if(ls>rs)
            cout<<"Case #"<<j<<": "<<ls<<" "<<rs<<endl;
        else
            cout<<"Case #"<<j<<": "<<rs<<" "<<ls<<endl;
    }
    return 0;
}
