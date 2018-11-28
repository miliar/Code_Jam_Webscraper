#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;


int main()
{
    int T,N,K;
    cin >> T;
    for(int t = 1; t<=T; ++t)
    {
        cin>>N>>K;
        priority_queue<int>stalls;
        stalls.push(N);

        for(int i=0;i<K-1; ++i)
        {
            int tmp = stalls.top();
            stalls.pop();

            int l = (tmp-1)/2;
            int r = tmp - (l+1);

            if(l!=0)
                stalls.push(l);
            if(r!=0)
                stalls.push(r);
        }

        int tmp = stalls.top();

        int l = (tmp-1)/2;
        int r = tmp - (l+1);

        cout <<"Case #"<<t<<": "<<max(l,r)<<" "<<min(l,r)<<endl;
    }

    return 0;
}
