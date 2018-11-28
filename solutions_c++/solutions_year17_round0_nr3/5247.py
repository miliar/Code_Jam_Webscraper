#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define fillchar(a,x) memset(a,x,sizeof(a))
struct node
{
    int l;
    int r;
    int w;
};
struct cmp
{
    bool operator() (const node &a, const node &b)
    {
        if(a.w!=b.w)
        return a.w<b.w;

        else
        return a.l>b.l;
    }
};
int main()
{
    ofstream myfile;
    myfile.open("1.txt");

    int n,k,t;
    priority_queue<node,vector<node>,cmp> myq;

    scanf("%d",&t);

    for(int j=1;j<=t;j++)
    {
        scanf("%d %d",&n,&k);

        node a;

        a.l=0;
        a.r=n+1;
        a.w=a.r-a.l;

        //printf("pushed is %d %d %d\n",a.l,a.r,a.w);

        myq.push(a);

        int l,r,m;

        for(int i=0;i<k;i++)
        {
            a=myq.top();
            myq.pop();

            //printf("popped is %d %d %d\n",a.l,a.r,a.w);

            node b;

            l=a.l;
            r=a.r;

            m=l+(r-l)/2;

            b.l=a.l;
            b.r=m;
            b.w=b.r-b.l;

            if(b.w>1)
            myq.push(b);

            b.l=m;
            b.r=a.r;
            b.w=b.r-b.l;

            if(b.w>1)
            myq.push(b);
        }

        //printf("%d %d\n",max(m-l-1,r-m-1),min(m-l-1,r-m-1));
        myfile<<"Case #"<<j<<": "<<max(m-l-1,r-m-1)<<" "<<min(m-l-1,r-m-1)<<endl;

        while(!myq.empty())
        {
            myq.pop();
        }
    }
	return 0;
}
