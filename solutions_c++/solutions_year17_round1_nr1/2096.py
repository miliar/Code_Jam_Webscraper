#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cstdio>

int r,c;


using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int n;
    cin >> n;
    for (int z=0;z<n;z++)
    {
    vector<string > a,b;

    cin >> r >> c;
    for (int i=0;i<r;i++){

        string s;
        cin >> s;
        a.push_back(s);
        b.push_back(s);
    }
    for (int i=0;i<r;i++)
    {
       // cout << i << endl;
        for (int j=0;j<c;j++)
        {
            //cout << j << endl;
            if (b[i][j]!='?')
            {
                char ch=a[i][j];
                int lft=j-1;
                while (lft>=0)
                {
                    if (a[i][lft]!='?')break;
                    //cout << 1;
                    a[i][lft]=ch;
                    lft--;
                }
                lft++;
                int rt=j+1;
                while (rt<c)
                {
                    //cout << rt  << " " << c << endl;
                    if (a[i][rt]!='?')break;

                    a[i][rt]=ch;
                    rt++;

                }
                rt--;
                int v=0,mt=r+1, up=i-1,x=0,md=r+1,dn=i+1;
                for (int p=lft;p<=rt;p++)
                {
                    v=0,x=0,up=i-1,dn=i+1;
                    while (up>=0)
                    {
                       // cout << up << endl;
                        if (a[up][p]!='?')break;
                        v++;
                        up--;
                    }
                    mt=min(v,mt);
                    while (dn<r)
                    {
                        if (a[dn][p]!='?')break;
                        x++;
                        dn++;
                    }
                    md=min(x,md);

                }
                //cout << ch << " " << md << endl;
                for (int p=lft;p<=rt;p++)
                {
                    for (int q=i-1;q>=i-mt;q--)
                    {
                        a[q][p]=ch;
                    }
                    for (int q=i+1;q<=i+md;q++)
                    {
                        a[q][p]=ch;
                    }

                }



            }
        }

    }
    cout << "Case #" << z+1 << ":\n";
    for (int i=0;i<r;i++)
    {
         cout << a[i] << endl;
    }
    }


}
