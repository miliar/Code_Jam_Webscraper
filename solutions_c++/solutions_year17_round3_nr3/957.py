#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
using namespace std;

struct Node
{
    double p;
    int ct;
    bool operator<(const Node& b) const
    {
        return p>b.p;
    }
};

double eps=1e-8;
int n,k;
double u;

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        cout<<"Case #"<<++tci<<": ";
        cin>>n>>k;
        cin>>u;
        int i;
        priority_queue<Node> pq;
        double prob=1;
        for(i=0;i<n;i++)
        {
            double t;
            cin>>t;
            Node node;
            node.p=t;
            node.ct=1;
            //cout<<"?"<<node.p<<endl;
            pq.push(node);
        }
        while(fabs(u-0)>eps)
        {
            //cout<<u<<endl;
            Node out1=pq.top();
            pq.pop();
            if(pq.empty())
            {
                out1.p=min(1.0,out1.p+u/out1.ct);
                pq.push(out1);
                u=0;
                break;
            }
            Node out2=pq.top();
            pq.pop();
            if(fabs(out2.p-out1.p)<eps)
            {
                out1.ct+=out2.ct;
                pq.push(out1);
                continue;
            }
            //cout<<out1.p<<" "<<out2.p<<endl;
            double ad=min((out2.p-out1.p)/out1.ct,u/out1.ct);
            out1.p+=ad;
            u-=ad*out1.ct;
            pq.push(out1);
            pq.push(out2);
        }
        while(!pq.empty())
        {
            Node node=pq.top();pq.pop();
            int i;
            for(i=0;i<node.ct;i++)prob*=node.p;
        }

        printf("%.8lf\n",prob);
    }
    return 0;
}
