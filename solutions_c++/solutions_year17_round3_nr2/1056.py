#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
pair<int,int> P1[1000],P2[1000];
int q,t,R1,R2,t1,t2,i,I1,I2,S1,S2;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for (q=1;q<=t;q++)
    {
        cout<<"Case #"<<q<<": ";
        cin>>t1>>t2;
        R1=R2=0;
        for (i=0;i<t1;i++)
        {
            cin>>I1>>S1;
            R1+=S1-I1;
            P1[i] = make_pair(I1,S1);
        }
        sort(P1,P1+t1);
        for (i=0;i<t2;i++)
        {
            cin>>I2>>S2;
            R2+=S2-I2;
            P2[i] = make_pair(I2,S2);
        }
        sort(P2,P2+t2);
        if (t1+t2<2)
            cout<<2;
        else if (t1==1&&t2==1)
             cout<<2;
        else if (t1==2)
        {
            if (P1[0].second==P1[1].first)
                cout<<2;
            else if (P1[1].second-P1[0].first<=720)
                cout<<2;
            else if (P1[1].second==1440&&P1[0].first==0)
                cout<<2;
            else if ((P1[0].second+1440)-P1[1].first<=720)
                cout<<2;
            else cout<<4;

        }
        else if (t2==2)
        {
            if (P2[0].second==P2[1].first)
                cout<<2;
            else if (P2[1].second-P2[0].first<=720)
                cout<<2;
            else if (P2[1].second==1440&&P2[0].first==0)
                cout<<2;
            else if ((P2[0].second+1440)-P2[1].first<=720)
                cout<<2;
            else cout<<4;
        }

        cout<<'\n';
    }
}
