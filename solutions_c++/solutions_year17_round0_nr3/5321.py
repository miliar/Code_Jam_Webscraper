#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

int main()
{
    freopen("C-small-2-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int t;
    cin>>t;
    int jj=1;
    while(t)
    {
        long long n,k;
        cin>>n>>k;
        long long res=0;
        long long ans1,ans2,pos=0,last=0;
        /*vector<bool>a(n+1,0);
        vector<int>l(n+1,n+1);
        vector<int>r(n+1,n+1);
        vector<int>m1(n+1,0);
        vector<int>m2(n+1,0);
        if(k<1000){
        for(int i=0;i<k;i++)
        {
            last=0;
            for(int j=1;j<=n;j++)
            {
                if(a[j]==1)
                {
                    last=j;
                }
                else
                {
                    l[j]=j-last-1;
                    m1[j]=l[j];
                    m2[j]=l[j];
                    //printf("%d ",l[j]);
                }

            }
            last=n+1;
            vector<int>p;
            //cout<<endl;
            for(int j=n;j>=1;j--)
            {
                if(a[j]==1)
                {
                    last=j;
                }
                else
                {
                    r[j]=last-j-1;
                    m1[j]=min(r[j],l[j]);
                    m2[j]=max(r[j],l[j]);
                    //printf("%d ",r[j]);
                }
            }
            //cout<<endl;
            int m;
            for(int j=1;j<=n;j++)
            {
                if(!a[j])m=m1[j];
            }
            for(int j=2;j<=n;j++)
            {
                if(a[j])continue;
                if(m<m1[j])m=m1[j];
            }
            //cout<<m<<"  ";
            ans1=m;
            for(int j=1;j<=n;j++)
            {
                if(a[j])continue;
                if(m==m1[j]){p.push_back(j);}// cout<<j<<' ';}
            }
            m=m2[p[0]];
            pos=p[0];
            for(int j=0;j<p.size();j++)
            {
                if(m2[p[j]]>m)
                {
                    m=m2[p[j]];
                    pos=p[j];
                }
            }
            ans2=m;
            a[pos]=1;

        }
        printf("j== %d, ans2==%I64d, ans1==%I64d\n",jj,ans2,ans1);}
        int h=0;*/
        //vector<long long>q(k+100,0);
        //q[h]=n;
        priority_queue<long long>q;
        int ta=1;
        q.push(n);
        while(ta<k)
        {
            ta++;
           /* int temp=q[h];
            //cout<<temp<<' ';
            h++;
            temp--;
            q[ta++]=temp/2+(temp)%2;
            q[ta++]=temp/2;*/
            int temp=q.top()-1;
            q.pop();
            q.push(temp/2+(temp)%2);
            q.push(temp/2);
            //ta+=2;
        }// 9 4 4 2 1 2 1
        printf("Case #%d: %I64d %I64d\n",jj,(q.top()-1)/2+(q.top()+1)%2,(q.top()-1)/2);
        t--;
        jj++;
    }
    return 0;
}
