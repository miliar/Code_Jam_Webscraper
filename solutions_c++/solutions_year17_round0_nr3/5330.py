#include <iostream>
#include<queue>
using namespace std;

int main()
{
    int t,tc=0,n,k,i,low,mid,high,test,cl,cr,left,right;
    cin >> t;
    int arr[1010]={0};
    typedef struct prq
    {
        int l,h,dist;
        bool operator<(const prq &o) const
        {
        return dist < o.dist;
        }
    }prq;
    while(t--)
    {
        priority_queue<prq> pq;
        cout << "Case #" << ++tc << ": ";
        cin >> n >> k;
        for(i=0;i<n+2;i++)
            arr[i]=0;
        arr[0]=1;
        arr[n+1]=1;
        // low=0;
        // high=n+1;
        pq.push(prq{0,n+1,n+1});
      //  cout << n << k << endl;
        while(k--)
        {
        //     mid=(low+high)/2;
            left=pq.top().l;
            right=pq.top().h;
            mid=(left+right)/2;
            pq.pop();
            // if((high-mid)==(mid-left))
            // {
            //     pq.push(prq{left,mid,mid-left-1});
            //     pq.push(prq{mid,right,right-mid});
            
            // }
            // else
            //{
                pq.push(prq{left,mid,mid-left});
                pq.push(prq{mid,right,right-mid});
            //}
            arr[mid]=1;
         //   cout << " mid is " << mid << endl;
            // if((mid-low)>=(high-mid))
            // {
            //     high=mid;
            // }
            // else
            // {
            //     low=mid;
            // }
        }
        test=mid;
        cl=0;
        cr=0;
        while(test--)
        {
            if(arr[test]==1)
                break;
            cl++;
        }
        while(mid++)
        {
            if(arr[mid]==1)
                break;
            cr++;
        }
        //  for(int i=0;i<n+2;i++)
        //       cout << arr[i] << " ";
        //cout << endl;
        // cout << "cl is " << cl << " cr is " << cr << endl;
        
        cout << (cl>cr?cl:cr) << " " << (cl<cr?cl:cr) << endl;
        
    }
    
    return 0;
}
