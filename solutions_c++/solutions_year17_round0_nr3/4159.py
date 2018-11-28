#include<bits/stdc++.h>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("In.txt", "r", stdin);
    freopen("Out.txt", "w", stdout);

    int t;
    cin>>t;

    for(int i = 0; i < t; ++i)
    {
        long long int n,k;
        cin>>n>>k;

        priority_queue<long long int> q;
        q.push(n);

        long long int f,s;

        for(long long int j = 0; j < k; ++j)
        {
            n = q.top();
            q.pop();
            f = n/2;
            s = n-f-1;
            q.push(f);
            q.push(s);
            //cout<<f<<" "<<s<<endl;
        }

        cout<<"Case #"<<i+1<<": "<<f<<" "<<s<<endl;
    }
}
