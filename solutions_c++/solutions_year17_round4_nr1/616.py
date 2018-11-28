#include <bits/stdc++.h>
using namespace std;
#define ll          long long
#define MOD         1000000007
#define ll          long long
#define pb          push_back
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define endl        '\n'
#define PI          acos(-1)
#define sz(x)       (int)x.size()
int A[5];
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int t,T,i,n,p,x,res;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>n>>p;
        memset(A,0,sizeof A);
        for(i=0;i<n;i++)
        {
            cin>>x;
            A[x%p]++;
        }
        res=0;
        if(p==2)
        {
            res+=A[0];
            res+=A[1]/2;
            res+=A[1]%2;
        }
        else if(p==3)
        {
            res+=A[0];
            x=min(A[1],A[2]);
            res+=x;
            A[1]-=x;
            A[2]-=x;
            res+=A[1]/3;
            res+=A[2]/3;
            res+=(A[1]%3!=0);
            res+=(A[2]%3!=0);
        }
        else
        {
            res+=A[0];
            res+=A[2]/2;
            A[2]%=2;
            x=min(A[1],A[3]);
            res+=x;
            A[1]-=x;
            A[3]-=x;
            if(A[2])
            {
                if(A[1]>=2)
                {
                    res++;
                    A[2]=0;
                    A[1]-=2;
                }
                else if(A[3]>=2)
                {
                    res++;
                    A[2]=0;
                    A[3]-=2;
                }
                if(A[2])
                    res++;
            }
            if(!A[2])
            {
                res+=A[1]/4;
                A[1]%=4;
                res+=A[3]/4;
                A[3]%=4;
                res+=(A[1]!=0);
                res+=(A[3]!=0);
            }
        }
        cout<<"Case #"<<t<<": "<<res<<endl;
    }
    return 0;
}
