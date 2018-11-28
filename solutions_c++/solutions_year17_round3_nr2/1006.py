#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>

using namespace std;

bool comp(pair<long long,int> l, pair<long long ,int> r)
{
    if(l.first==r.first)
    {
        return l.second>r.second;
    }
    return l.first>r.first;
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int jj=1;
    while(t)
    {
        int ac,aj;
        cin>>ac>>aj;
        vector<pair<int,int> >c(ac);
        vector<pair<int,int> >j(aj);
        int res=0;
        for(int i=0;i<ac;i++)
        {
            cin>>c[i].first>>c[i].second;
        }
        for(int i=0;i<aj;i++)
        {
            cin>>j[i].first>>j[i].second;
        }
        if(ac<=1&&aj<=1)
        {
           res=2;
        }
        else
        {
            if(ac==2)
            {
                if(max(c[0].second,c[1].second)-min(c[0].first,c[1].first)>720)
                {
                    if(-min(c[0].second,c[1].second)+max(c[0].first,c[1].first)>720)res=2;
                    else res=4;
                    if(-min(c[0].second,c[1].second)+max(c[0].first,c[1].first)==720)res=2;
                }
                else
                {
                    res=2;
                }
            }
            else
            {
                if(max(j[0].second,j[1].second)-min(j[0].first,j[1].first)>720)
                {
                    if(-min(j[0].second,j[1].second)+max(j[0].first,j[1].first)>720)res=2;
                    else res=4;
                    if(-min(j[0].second,j[1].second)+max(j[0].first,j[1].first)==720)res=2;
                }
                else
                {
                    res=2;
                }
            }
        }
        printf("Case #%d: ",jj);
        cout<<res<<endl;
        jj++;
        t--;
    }
    return 0;
}
