#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream myfile;
myfile. open ("3output.txt");
    int t;
    cin>>t;
    int x=t;
    while(t--)
    {
        int n,k,count=0;
        cin>>n>>k;
        queue <int> q;
        q.push(n);
        while(!q.empty())
        {
            n=q.front();
            count++;
            if(count==k)
                break;
            int mid=n/2;
            if(mid!=0)
                q.push(mid);
            if(n%2)
            {
                if(mid)
                    q.push(mid);
            }
            else
            {
                if(mid-1)
                    q.push(mid-1);
            }
            q.pop();
            int i,a[1009];
            for(i=0;!q.empty();i++)
            {
                a[i]=q.front();
                q.pop();
            }
            sort(a,a+i-1,std::greater<int>());
            for(int j=0;j<i;j++)
                q.push(a[j]);
        }

        if(n%2)
            myfile<<"Case #"<<x-t<<": "<<n/2<<" "<<n/2<<endl;
        else
            myfile<<"Case #"<<x-t<<": "<<n/2<<" "<<n/2-1<<endl;
    }
    return 0;
}
