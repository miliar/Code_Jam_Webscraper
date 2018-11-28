/* ***************************************
Author        :Scau.ion
Created Time  :2017/04/23 00:23:02 UTC+8
File Name     :ion.cpp
*************************************** */

#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define ULL unsigned long long
#define PB push_back
#define MP make_pair
#define PII pair<int,int>
#define VI vector<int>
#define VPII vector<PII>
#define X first
#define Y second
#define IOS ios::sync_with_stdio(0);cin.tie(0);
#define IN freopen("B-large.in", "r", stdin);
#define OUT freopen("B-large.out", "w", stdout);

char co[6]={'R','O','Y','G','B','V'};

int main()
{
    IN;
    OUT;
    IOS;
    int t;
    cin>>t;
    for (int i=1;i<=t;++i)
    {
        int n;
        cin>>n;
        int b[6];
        int type=0;
        for (int j=0;j<6;++j)
        {
            cin>>b[j];
            if (b[j]) ++type;
        }
        cout<<"Case #"<<i<<": ";
        if (n==1)
        {
            for (int j=0;j<6;++j)
                if (b[j]) cout<<co[j]<<endl;
            continue;
        }
        bool flag=1;
        for (int j=1;j<6;j+=2)
        {
            if (b[j]&&b[(j+3)%6]<=b[j]) flag=0;
        }
        if (!flag)
        {
            if (type==2)
            {
                for (int j=0;j<6;j+=2)
                {
                    if (b[j]&&b[(j+3)%6]&&b[j]==b[(j+3)%6])
                    {
                        flag=1;
                        int oth=(j+3)%6;
                        for (int k=1;k<=b[j];++k)
                            cout<<co[j]<<co[oth];
                        cout<<endl;
                    }
                }
            }
            if (!flag) cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        for (int j=1;j<6;j+=2)
        {
            b[(j+3)%6]-=b[j];
        }
        pair<int,int> a[3];
        a[0].X=b[0];
        a[1].X=b[2];
        a[2].X=b[4];
        a[0].Y=0;
        a[1].Y=2;
        a[2].Y=4;
        sort(a,a+3);
        if (a[2].X>a[0].X+a[1].X) cout<<"IMPOSSIBLE"<<endl;
        else
        {
            vector<int> ans;
            for (int j=1;j<=a[2].X;++j)
                ans.PB(a[2].Y);
            int st=0;
            for (int j=1;j<=a[1].X;++j)
            {
                ans.insert(ans.begin()+st,a[1].Y);
                st+=2;
            }
            int j;
            for (j=1;j<=a[0].X;++j)
            {
                if (st==ans.size()) break;
                ans.insert(ans.begin()+st,a[0].Y);
                st+=2;
            }
            st=0;
            for (;j<=a[0].X;++j)
            {
                ans.insert(ans.begin()+st,a[0].Y);
                st+=2;
            }
            for (int j=0;j<ans.size();++j)
            {
                int coo=ans[j];
                cout<<co[coo];
                int oth=(coo+3)%6;
                for (int k=1;k<=b[oth];++k)
                {
                    cout<<co[oth]<<co[coo];
                }
                b[oth]=0;
            }
            cout<<endl;
        }
    }
    return 0;
}
