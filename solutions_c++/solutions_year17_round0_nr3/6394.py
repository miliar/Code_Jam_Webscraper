#include <bits/stdc++.h>
using namespace std;
int main()
{
    int col_test,top,n,k,r,res;
    cin>>col_test;
    for(r=1;r<=col_test;r++)
    {
        priority_queue<int> p;
        cin>>n>>k;
        p.push(n);
        for(int i=0;i<k-1;i++)
        {
            top=p.top();
            p.pop();
            if(top%2!=0)
            {
                p.push(top/2);
                p.push(top/2);
            }
            else
            {
                p.push(top/2);
                p.push(top/2-1);
            }
        }
        res=p.top();
        if(res%2!=0)
            printf("Case #%d: %d %d\n",r,res/2,res/2);
        else
            printf("Case #%d: %d %d\n",r,res/2,res/2 - 1);
    }
}