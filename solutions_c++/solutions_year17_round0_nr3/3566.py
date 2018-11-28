#include <iostream>
#include <stdio.h>
#include <queue>
using namespace std;

struct asd
{
    int length;
    int s, f;
    bool operator<(const asd& rhs) const
    {
        if(length==rhs.length) return s>rhs.s;
        return length < rhs.length;
    }
};


int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int N,I,i,j,n,k;
    cin>>N;
    for(I=1;I<=N;I++)
    {
        cin>>n>>k;
        priority_queue<asd> q;
        asd init;
        init.length=n;
        init.s=1;
        init.f=n;
        q.push(init);
        for(i=1;i<=k;i++)
        {
            init = q.top();
            //cout<<init.s<<" "<<init.f<<"\n";
            q.pop();
            j=(init.s+init.f)/2;
            asd aux;
            aux.s=init.s;
            aux.f=j-1;
            aux.length=aux.f-aux.s+1;
            q.push(aux);
            asd aux2;
            aux2.s=j+1;
            aux2.f=init.f;
            aux2.length=aux2.f-aux2.s+1;
            q.push(aux2);

        }
        cout<<"Case #"<<I<<": "<< max(j-init.s,init.f-j)<<" "<<min(j-init.s,init.f-j)<<"\n";

    }
    return 0;
}
