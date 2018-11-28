#include<bits/stdc++.h> //_Shaffi
using namespace std;
#define sc scanint
#define sl scanlong
#define gc getchar
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define in(a,arr) sc(a); arr.push_back(a);
#define mi 100000007
#define DO int t; scanf("%d",&t); while(t--)
#define st(arr); sort(arr.begin(),arr.end());
#define er(arr); arr.erase(unique(arr.begin(),arr.end()),arr.end());
#define INF INT_MAX
#define mx(arr) *max_element(arr.begin(),arr.end())
#define mn(arr) *max_element(arr.begin(),arr.end())
#define getst(s) getline(cin>>ws,s)
#define sci(a,b) sc(a),sc(b);
#define scl(a,b) sl(a),sl(b);
#define MAX 664579
typedef long long ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > pi;
void scanint(int &x);
void scanlong(ll &x);
void scanint(int &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
void scanlong(ll &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
int main()
{
    int t,tt; sc(t);
    tt=t;
    while(t--)
    {
        string a;
        int f=0,g=0,k,c=0,j=0;
        cin>>a>>k;
        for(int i=0;i<a.size();i++)
        {
            if(a[i]=='-')
            {
                f=1;
                break;
            }
        }

        if(f==0)
            cout<<"Case #"<<tt-t<<": "<<0<<endl;
        else
        {
            for(int i=0;i<a.size();i++)
            {
                if(a[i]=='-')
                {
                    c++;
                    for(int j=i;j<=(i+k-1) && (i+k-1)<a.size() ;j++)
                    {
                        if(a[j]=='+')
                            a[j]='-';
                        else
                            a[j]='+';
                    }
                }
            }
            for(int i=0;i<a.size();i++)
            {
                if(a[i]=='-')
                {
                    g=1;
                    break;
                }
            }
            if(g!=1)
                cout<<"Case #"<<tt-t<<": "<<c<<endl;
            else
                cout<<"Case #"<<tt-t<<": "<<"IMPOSSIBLE"<<endl;
        }
    }
}
