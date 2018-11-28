#include <bits/stdc++.h>
#define PIE 3.141592653589793238462643383279502884197
using namespace std;
struct pc{
    long long int r,h;
    int id;
};
bool comp(pc p1, pc p2)
{
    return (p1.h*p1.r > p2.h*p2.r);
}
int main()
{
    freopen("put.in","r",stdin);
    freopen("utput.out","w",stdout);
    int t,k,n,cs=0;
    pc pan[1003];
    cin>>t;
    while(t--)
    {
        cs++;
        cin>>n>>k;
        for(int i=0;i<n;i++)
        {
            cin>>pan[i].r>>pan[i].h;
            pan[i].id=i;
        }
        sort(pan,pan+n,comp);
        long long int max_area = 0;
        for(int i=0;i<n;i++)
        {
            int cap=k-1;
            long long int area = pan[i].r*pan[i].r;
            area+=2*pan[i].r*pan[i].h;
            for(int j=0;j<n && cap>0;j++)
            {
                if(pan[j].id!=pan[i].id)
                {
                    if(pan[j].r<=pan[i].r)
                    {
                        area+=2*pan[j].r*pan[j].h;
                        cap--;
                    }
                }
            }
            if(cap==0)
            {
                max_area = max(max_area,area);
            }
        }
        long double tot = (max_area*PIE);
        printf("Case #%d: %.9Lf\n",cs,max_area*PIE);
        //cout<<"Case #"<<cs<<": "<<(max_area*PIE)<<"\n";
    }
    return 0;
}
