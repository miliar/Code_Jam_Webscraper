#include<bits/stdc++.h>
using namespace std;



struct stall
{
    int left_occupied,right_occupied;
    bool operator < (const stall& b)const
    {
        if(right_occupied-left_occupied==b.right_occupied-b.left_occupied)
        {
            return left_occupied > b.left_occupied;
        }
        return right_occupied-left_occupied<b.right_occupied-b.left_occupied;
    }
};

int main()
{

    int T;
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    cin>>T;

    for(int t=1;t<=T;t++)
    {
        unsigned long long n,k;
        cin>>n>>k;
        priority_queue<stall>pq;
        stall st;
        st.left_occupied=0;
        st.right_occupied=n+1;
        pq.push(st);
        long long mx,mn;
        for(int i=1;i<=k;i++)
        {
            st = pq.top();
            pq.pop();
            stall st2;
            long long m=(st.left_occupied+st.right_occupied)/2;
            if(m-st.left_occupied>1)
            {
                st2.left_occupied = st.left_occupied;
                st2.right_occupied = m;
                pq.push(st2);
            }
            if(st.right_occupied-m>1)
            {
                st2.left_occupied = m;
                st2.right_occupied = st.right_occupied;
                pq.push(st2);
            }
            mx = max(m-st.left_occupied-1,st.right_occupied-m-1);
            mn = min(m-st.left_occupied-1,st.right_occupied-m-1);
        }
        cout<<"Case #"<<t<<": "<<mx<<" "<<mn<<endl;
    }
    return 0;
}
