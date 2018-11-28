#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long int t,n=0,k=0,x=0;
    long long int num;
    long long int  max, min;


    cin>>t;

    for(x=1; x<=t; x++)
    {
        cin>>n;
        cin>>k;

        priority_queue<long long int> q;
        q.push(n);
        for(int i=0; i<k; i++)
        {
            num = q.top();
            q.pop();
            max = num/2;
            min = num - num/2 - 1;

            q.push(min);
            q.push(max);
         }
        cout<<"Case #"<<x<<": "<<max<<" "<<min<<"\n";
    }


    return 0;
}

