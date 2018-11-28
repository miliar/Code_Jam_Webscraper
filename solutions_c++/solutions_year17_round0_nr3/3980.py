#include<iostream>
#include<string>
#include<queue>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        priority_queue<unsigned long> pq;
        unsigned long n,k;
        cin>>n>>k;
        pq.push(n);
        k--;
        while(k--)
        {
            unsigned long temp=pq.top();
            if(temp==1)break;
            pq.pop();
            pq.push(((temp>>1)-((temp&1)?0L:1L)));
            pq.push(temp>>1);
        }
        unsigned long space= pq.top(),left,right;
        if(space&1)
        {
            left=space>>1;
            right=space>>1;
        }
        else
        {
            left= (space>>1)-1;
            right= (space>>1);
        }
        cout<<"Case #"<<tc<<": "<<max(left,right)<<" "<<min(left,right)<<endl;
    }
    return 0;
}