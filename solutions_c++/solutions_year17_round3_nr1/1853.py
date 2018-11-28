#include<bits/stdc++.h>
using namespace std;
#define PI 3.141592653589793238462643383279502884197169399
struct node{
    double r,h;
};
struct node1{
    double h1,ind,r1;
};
bool cmp(node1 i,node1 j)
{
    return(i.r1> j.r1);
}
bool cmp1(node1 i,node1 j)
{
    return(i.h1> j.h1);
}
bool cmp3(node1 i,node1 j)
{
    return(i.ind< j.ind);
}
int main()
{
    int T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        int N,K,j;
        cin>>N>>K;
        node ans[N];
        node1 b[N];
        for(j=0;j<N;j++)
        {
            double R,H;
            scanf("%lf%lf",&R,&H);
            H= 2*R*H;
            R= R*R;
            b[j].h1= H;
            b[j].r1= R;
        }
        sort(b,b+N,cmp);
        for(j=0;j<N;j++)
        {
            b[j].ind=j;
            ans[j].r=b[j].r1;
            ans[j].h=b[j].h1;
        }
        sort(b+1,b+N,cmp1);
        double sum=0;
        priority_queue< pair<double,double> , vector<pair<double,double > >,greater< pair<double,double > > > pq;
        for(j=1;j<K;j++)
        {
            sum+=b[j].h1;
            pq.push(make_pair(b[j].ind,b[j].h1));
        }
        int last=j;
        for(j=0;j<N-K+1;j++)
        {
            if(!pq.empty()){
            while(pq.top().first<=j)
            {
                sum-=pq.top().second;
                pq.pop();
                pq.push(make_pair(b[last].ind,b[last].h1));
                sum+= b[last].h1;
                last++;
            }
            }
            ans[j].h+=sum;
        }
        for(j=0;j<N-K+1;j++)
        {
            ans[j].r+=ans[j].h;
        }
        double mx1= ans[0].r;
        for(j=1;j<N-K+1;j++)
        {
            if(ans[j].r>mx1)
                mx1= ans[j].r;
        }
        mx1*=PI;
        cout<<"Case #"<<i<<": ";
        printf("%0.9f",mx1);
        cout<<endl;
    }
    return 0;
}
