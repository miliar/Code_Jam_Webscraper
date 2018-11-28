#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define ll long long
#define mp make_pair
#define MAX 100005
#define mod 1000000007
#define pb push_back
#define INF 1e18
#define pii pair<int,int>

int main()
{
    freopen ("B-small-attempt2.in","r",stdin);
    freopen ("outputC.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,z,n,r,o,y,g,b,v;
    int a1,a2,a3;
    char c1,c2,c3;
    cin>>t;
    //cout<<t<<endl;
    for(z=1;z<=t;z++)
    {
        cin>>n;
        cin>>r>>o>>y>>g>>b>>v;
        //cout<<n<<" "<<r<<" "<<o<<" "<<y<<" "<<g<<" "<<b<<" "<<v<<endl;
        cout<<"Case #"<<z<<": ";
        a1=max(r,max(y,b));
        a3=min(r,min(y,b));
        a2=r+y+b-a1-a3;
        if((a3+a2)>=a1)
        {
            if(a1==r)
            {
                c1='R';
                r=-1;
            }
            else if(a1==y)
            {
                c1='Y';
                y=-1;
            }
            else if(a1==b)
            {
                c1='B';
                b=-1;
            }
            if(a2==r)
            {
                c2='R';
                r=-1;
            }
            else if(a2==y)
            {
                c2='Y';
                y=-1;
            }
            else if(a2==b)
            {
                c2='B';
                b=-1;
            }
            if(a3==r)
                c3='R';
            else if(a3==y)
                c3='Y';
            else if(a3==b)
                c3='B';
            while(a3>=max((a1-a2+1),1))
            {
                cout<<c1<<c2<<c3;
                a1--;
                a2--;
                a3--;
            }
            while(a2>0)
            {
                cout<<c1<<c2;
                a2--;
                a1--;
            }
            while(a3>0)
            {
                cout<<c1<<c3;
                a3--;
                a1--;
            }
        }
        else
            cout<<"IMPOSSIBLE";
        cout<<endl;
    }
    return 0;
}
