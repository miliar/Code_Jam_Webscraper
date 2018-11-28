#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <queue>
using namespace std;

struct S
{
    int len;
    int start;

    S(int l, int s)
    {
        len=l;
        start=s;
    }

    bool operator<(const S &b) const
    {
        if(len!=b.len)
            return len<b.len;
        return start>b.start;
    }
};

struct Ans
{
    int M,m;
};

Ans solve(int K, int N)
{
    Ans a;
    priority_queue<S> q;
    q.push(S(K,0));

    for(int i=0; i<N-1; i++)
    {
        S r = q.top();
        q.pop();
        //printf("pop %d %d\n",r.len,r.start);
        int half = r.len/2;
        S s1(r.len-half, r.start);
        S s2(r.len-s1.len, r.start+s1.len);
        s1.len--;
        q.push(s1);
        q.push(s2);
    }
    S choose = q.top();
    //printf("pop %d %d\n",choose.len,choose.start);
    int half = (choose.len)/2;
    int rs = half;
    int ls = choose.len-rs-1;
    a.M=max(rs,ls);
    a.m=min(rs,ls);


    return a;
}


int main()
{
    int T=0;
    scanf("%d",&T);
    for(int i=0; i<T; i++)
    {
        int K=0, N=0;
        scanf("%d %d",&K,&N);
        Ans a=solve(K,N);
        printf("Case #%d: %d %d\n",i+1,a.M,a.m);
    }

    return 0;
}
