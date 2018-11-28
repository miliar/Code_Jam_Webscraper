#include<tuple>
#include<queue>
#include<iostream>
#define ENCENDER(n,i) (n|1<<i)
#define APAGAR(n,i) (n&~(1<<i))
using namespace std;
int k;
int f(string s)
{
    int n=0,y=s.size(),x;
    for(x=0;x<y;x++)
        if(s[x]=='+')
            n|=1<<x;
    return n;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string s;
    int t,c,x,y,o,n,i,p,m;
    cin>>t;
    for(c=1;c<=t;c++)
        {
        cin>>s>>k;
        y=s.size();
        o=(1<<y)-1;
        n=f(s);
        queue<tuple<int,int,int> > q;
        q.push(make_tuple(n,0,0));
        while(q.empty()==0)
            {
            n=get<0>(q.front());
            i=get<1>(q.front());
            p=get<2>(q.front());
            //cout<<n<<" "<<i<<" "<<p<<endl;
            q.pop();
            if(n==o)
                break;
            if(i+k>y)
                continue;
            m=n;
            for(x=i;x<i+k;x++)
                {
                if(m&1<<x)
                    m=APAGAR(m,x);
                else
                    m=ENCENDER(m,x);
                }
            q.push(make_tuple(m,i+1,p+1));
            for(;x<y;x++)
                {
                if(m&1<<x)
                    m=APAGAR(m,x);
                else
                    m=ENCENDER(m,x);
                if(m&1<<i)
                    m=APAGAR(m,i);
                else
                    m=ENCENDER(m,i);
                q.push(make_tuple(m,i+2,p+1));
                i++;
                }
            }
        cout<<"Case #"<<c<<": ";
        if(n==o)
            cout<<p<<endl;
        else
            cout<<"IMPOSSIBLE\n";
        }
    return 0;
}
