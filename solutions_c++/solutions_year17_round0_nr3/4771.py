#include <functional>
#include <queue>
#include <vector>
#include <iostream>
#include <math.h>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("CJ17_3.out","w",stdout);
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
        long long n,k,mx=0,mn=0;
        cin>>n>>k;
        std::priority_queue<long long int> q;
        q.push(n);
        long long i=0;
        while(i<k)
        {
            long long temp=q.top();
            q.pop();
            if(temp%2==0)
            {
                if(i==k-1)
                {
                    mn=temp/2-1;
                    mx=temp/2;
                }
                else
                {
                    q.push(temp/2-1);
                    q.push(temp/2);
                }
            }
            else
            {
                if(i==k-1)
                {
                    mx=temp/2;
                    mn=temp/2;
                }
                else{
                    q.push(temp/2);
                    q.push(temp/2);
                }
            }

            i++;
        }

        cout<<"Case #"<<x<<": "<<mx<<" "<<mn<<endl;


    }
    return 0;
}
