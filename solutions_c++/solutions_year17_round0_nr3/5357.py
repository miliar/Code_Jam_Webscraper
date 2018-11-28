#include <bits/stdc++.h>
using namespace std;
int main()
{
    int tc,n,k;
    //freopen("C-small-2-attempt1.in","r",stdin);
    //freopen ("C-small-2-attempt1.out","w",stdout);
    cin>>tc;
    for(int i=1; i<=tc; i++)
    {

        priority_queue <int> datas;
        cin>>n>>k;
        datas.push(n);
        int mx=0,mn=1000000000,temp=0;
        for(int j=0; j<k; j++)
        {
            temp=datas.top();
            datas.pop();
            //cout<<temp<<endl;
            if(temp%2)
            {
                mx=temp/2;
                mn=temp/2;
                datas.push(mx);
                datas.push(mn);
            }
            else
            {
                mx=temp/2;
                if(mx>0)mn=temp/2-1;
                datas.push(mx);
                datas.push(mn);
            }
        }
        printf("Case #%d: %d %d\n",i,mx,mn);
    }


    return 0;
}
