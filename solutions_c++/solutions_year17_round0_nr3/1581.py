#include <iostream>
#include <cstdio>
#include <queue>
#include <map>
using namespace std;
long long p2[64];
priority_queue<long long> q;
map<long long,long long> M;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int N;
    p2[0] = 1;
    cin >> N;
    for (int i = 1; i<=N; i++)
    {
        long long n,k;
        cin >>n >>k;
        M.clear();
        while (!q.empty())q.pop();
        printf("Case #%d: ",i);
        q.push(n);

        M[n] =1;
        while (!q.empty())
        {
            long long t = q.top();
            q.pop();
            if (k<=M[t])
            {
                cout <<(t)/2LL <<" "<<(t-1)/2LL<<endl;
                break;
            }
            k-=M[t];
            if (t>1LL&&M[t/2LL]==0)q.push(t/2LL);
            if (t>2LL&&M[(t-1LL)/2LL]==0)q.push((t-1LL)/2LL);
            M[t/2LL]+=M[t];
            M[(t-1LL)/2LL]+=M[t];
            M[t]=0;
        }
    }
}
