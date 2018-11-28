#include <iostream>
#include <queue>
using namespace std;
typedef long long int lli;
int main()
{
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/BathroomStalls/C-small-2-attempt1.in","r",stdin);
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/BathroomStalls/output2.txt","w",stdout);
    int t,test=1;
    lli n,k,x;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        priority_queue<lli> q;
        q.push(n);
        while(k--)
        {
            x=q.top();
            q.pop();
            if(x&1)
                q.push(x/2),q.push(x/2);
            else
                q.push(x/2),q.push(x/2-1);
        }
        if(x&1)
            cout<<"Case #"<<test++<<": "<<x/2<<" "<<x/2<<endl;
        else
            cout<<"Case #"<<test++<<": "<<x/2<<" "<<x/2-1<<endl;
    }
    return 0;
}
