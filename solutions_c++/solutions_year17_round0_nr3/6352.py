#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

priority_queue <long long int> Q;

ifstream in("data.in");
ofstream out("data.out");

int main()
{
    long long int tests;
    in>>tests;
    for(long long int p=1; p<=tests; p++)
    {
        cout<<p<<" ";
        long long int n,k;
        in>>n>>k;
        Q.push(n);
        for(long long int i=1; i<k; i++)
        {
            long long int x;
            x=Q.top()-1;
            Q.pop();
            Q.push(x/2);
            if(x%2==1)
            {
                Q.push(x/2+1);
            }
            else
            {
                Q.push(x/2);
            }
        }
        long long int l,r;
        long long int x=Q.top()-1;
        r=x/2;
        if(x%2==1)
            l=x/2+1;
        else
            l=x/2;
        out<<"Case #"<<p<<": ";
        out<<max(l,r)<<" "<<min(l,r)<<'\n';
        while(Q.empty()==0)
        {
            Q.pop();
        }
    }
}
