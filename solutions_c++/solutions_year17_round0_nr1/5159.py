#include <bits/stdc++.h>
using namespace std;

int cek(string kata,int n)
{
    int tanda=0,temp=0;
    for(int i=0; i<kata.length(); i++)
    {
        if(kata[i]=='-')
        {
            tanda=1;
            break;
        }
    }
    if(tanda==1)
    {
        for(int i=0; i<kata.length(); i++)
        {
            if(kata[i]=='-')
            {
                if(n>kata.length()-i) break;
                for(int j=0;j<n;j++)
                {
                    if(kata[i+j]=='-')kata[i+j]='+';
                    else kata[i+j]='-';
                }
                temp++;
            }
        }
    }
    else return temp;

    for(int i=0; i<kata.length(); i++)
    {
        if(kata[i]=='-')
        {
            return -1;
        }
    }
    return temp;
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen ("A-large.out","w",stdout);
    int tc,n;
    string kata;
    cin>>tc;
    for(int i=1; i<=tc; i++)
    {
        cin>>kata;
        cin>>n;
        if(cek(kata,n)==-1) printf("Case #%d: IMPOSSIBLE",i);
        else printf("Case #%d: %d",i,cek(kata,n));
        cout<<endl;
    }

    return 0;
}
