#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        priority_queue <int> pq;
        pq.push(n);
        k--;
        while (k--)
        {
            int top=pq.top();
            pq.pop();
            pq.push(top/2);
            pq.push((top-1)/2);
        }
        int ml=pq.top();
        printf("Case #%d: %d %d\n",itr,ml/2,(ml-1)/2);
    }

}
