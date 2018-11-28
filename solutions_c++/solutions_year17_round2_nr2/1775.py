#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int ii=0; ii<t; ii++)
    {
        int n, r, o, y, g, b, v, fin=-1;
        cin>>n>>r>>o>>y>>g>>b>>v;
        string res(n,'#');

        int mx, mn, md;
        char mxc, mnc, mdc;
        if (r>=y && y>=b)
            mx=r, md=y, mn=b, mxc='R', mdc='Y', mnc='B';
        else if (r>=b && b>=y)
            mx=r, md=b, mn=y, mxc='R', mdc='B', mnc='Y';
        else if (y>=r && r>=b)
            mx=y, md=r, mn=b, mxc='Y', mdc='R', mnc='B';
        else if (y>=b && b>=r)
            mx=y, md=b, mn=r, mxc='Y', mdc='B', mnc='R';
        else if (b>=y && y>=r)
            mx=b, md=y, mn=r, mxc='B', mdc='Y', mnc='R';
        else
            mx=b, md=r, mn=y, mxc='B', mdc='R', mnc='Y';

        if (mx<=n/2)
        {
            string s=string(mx,mxc)+string(md,mdc)+string(mn,mnc);

            int i=0;
            for (int j=0; j<n; i++, j+=2)
                res[j]=s[i];

            for (int j=1;j<n; j+=2,i++)
                res[j]=s[i];

            cout<<"Case #"<<ii+1<<": "<<res<<endl;
        }
        else
            cout<<"Case #"<<ii+1<<": "<<"IMPOSSIBLE"<<endl;
    }
}
