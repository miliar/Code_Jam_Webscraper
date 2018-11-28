//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;

priority_queue<long long>pq;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream cin("input.in");
    ofstream cout("output.out");

    long long n,k,m,r,l;
    int T;
    cin>>T;

    for(int t1=1;t1<=T;t1++)
    {
        cout<<"Case #"<<t1<<": ";

        cin>>n>>m;
        //cout<<n<<" "<<m<<"  -  ";

        while(!pq.empty())pq.pop();
        pq.push(n);

        for(int i=1;i<=m;i++)
        {
            k=pq.top();
            pq.pop();


            k=k-1;
            l=(k/2)+k%2;
            r=(k/2);
            pq.push(r);
            pq.push(l);
        }
        cout<<l<<" "<<r<<"\n";

    }

    return 0;
}



