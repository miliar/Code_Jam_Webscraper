#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
using namespace std;

typedef vector<int> vi;
typedef long long int lli;
typedef vector<lli> vli;
typedef pair<int, int> pii;

void foo()
{

    int r, c;
    cin>>r>>c;
    cout<<endl;
    vector<string > a(r);
    int i, j, k;

    for(i=0;i<r;i++)
    {
        cin>>a[i];
    }

    char curr=0;

    //rowwise first
    for(i=0;i<r;i++)
    {
        j=c;
        for(k=0;k<c;k++)
        {
            if(a[i][k]!='?')
            {
                curr = a[i][k];
                for(j=0;j<=k;j++)
                {
                    a[i][j]=curr;
                }

                break;
            }
        }


        for(;j<c;j++)
        {
            if(a[i][j]=='?')
                a[i][j]=curr;

            else if(a[i][j]!=curr)
                curr=a[i][j];
        }
    }

    curr=0;
    //col wise
    for(j=0;j<c;j++)
    {
        i=r;
        for(k=0;k<r;k++)
        {
            if(a[k][j]!='?')
            {
                curr=a[k][j];
                for(i=0;i<=k;i++)
                {
                    a[i][j]=curr;
                }
                break;
            }
        }


        for(;i<r;i++)
        {
            if(a[i][j]=='?')
                a[i][j]=curr;

            else if(a[i][j]!=curr)
                curr=a[i][j];
        }
    }

    for(i=0;i<r;i++)
    {
        cout<<a[i]<<endl;
    }
    return;


}


int main()
{
    int t;
    cin>>t;
    int i;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        foo();
    }

}
