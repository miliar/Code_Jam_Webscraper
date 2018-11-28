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
#define PI          3.14159265359d
#define sz(x)       (int)x.size()
#define INF         1e12
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int t,T,r,o,y,g,b,v,n,i;
    char A[1005];
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>n>>r>>o>>y>>g>>b>>v;
        cout<<"Case #"<<t<<": ";
        if(r>n/2||y>n/2||b>n/2)
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        if(r>=y&&r>=b)
            A[0]='R',r--;
        else if(y>=r&&y>=b)
            A[0]='Y',y--;
        else
            A[0]='B',b--;
        for(i=1;i<n;i++)
        {
            if(A[i-1]=='R')
            {
                if(y>b)
                    A[i]='Y',y--;
                else if(b>y)
                    A[i]='B',b--;
                else if(A[0]=='Y')
                    A[i]='Y',y--;
                else
                    A[i]='B',b--;
            }
            else if(A[i-1]=='Y')
            {
                if(r>b)
                    A[i]='R',r--;
                else if(b>r)
                    A[i]='B',b--;
                else if(A[0]=='R')
                    A[i]='R',r--;
                else
                    A[i]='B',b--;
            }
            else
            {
                if(r>y)
                    A[i]='R',r--;
                else if(y>r)
                    A[i]='Y',y--;
                else if(A[0]=='R')
                    A[i]='R',r--;
                else
                    A[i]='Y',y--;
            }
        }
        if(A[0]==A[n-1])
            cout<<"IMPOSSIBLE"<<endl;
        else
        {
            for(i=0;i<n;i++)
                cout<<A[i];
            cout<<endl;
        }
    }
    return 0;
}
