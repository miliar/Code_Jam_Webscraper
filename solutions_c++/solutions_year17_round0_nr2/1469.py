#include <cstdio>
#include <string>
#include <iostream>
#include <sstream>
using namespace std;
int testcase;
string make(int cc,string x)
{
    for (int i=x.size()-1;i>=1;i--)
    {
        int before=i-1;
        for (;before>=0 && x[before]<=x[before+1];before--);
        if (before>=0)
        {
            x[i]='9';
            x[i-1]--;
        }
        else break;
    }
    while (x[0]=='0')
        x.erase(0,1);
    cout<<"Case #"<<cc<<": "<<x;
    if (cc<testcase) cout<<endl;
    return x;
}
bool descend(string y)
{
    for (int i=y.size()-1;i>=1;i--)
        if (y[i-1]>y[i]) return false;
    return true;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&testcase);
    for (int i=1;i<=testcase;i++)
    {
        string x,y,z;
        cin>>x;
        y=x;
        z=x;
        string myans=make(i,x);
        /*while (!descend(y))
        {
            y[y.size()-1]--;
            for (int j=y.size()-1;y[j]<'0';j--)
            {
                y[j]+=10;
                y[j-1]--;
            }
            while (y[0]=='0')
                y.erase(0,1);
        }
        if (y!=myans)
        {
            cout<<endl<<"err at input "<<z<<" my="<<myans<<" corr="<<y<<endl;
        }*/
    }
    return 0;
}
