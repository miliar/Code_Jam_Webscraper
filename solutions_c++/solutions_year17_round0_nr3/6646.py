#include<bits/stdc++.h>
#define MAX 100100
#define mod 1000000007
#define MS0(x) memset(x, 0, sizeof(x))
#define ll long long int
#define in(x) scanf("%I64d", &x)
#define ind(x) scanf("%d", &x)
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pid pair<int,double>
#define pii pair<int,int>
#define p_q priority_queue
#define gcd(a,b) __gcd(a,b)
using namespace std;
string to_string(int x)
{
    string s="";
    while(x!=0)
    {
        int d=x%10;
        s+=d+'0';
        x/=10;
    }
    reverse(s.begin(),s.end());
    return s;
}
int main()
{
        freopen("input.txt","r",stdin);
        freopen("out.txt","w",stdout);
 ios_base::sync_with_stdio(false);
 cin.tie(NULL);
 int t,tc;
 cin>>tc;
 for(t=0;t<tc;t++)
 {
    int n,k;
    cin>>n>>k;
    priority_queue< pair<int,pair<int,int> > > pq;
    pq.push(make_pair(n,make_pair(1,n+2)));
    int i;
    int ma,mi;
    for(i=1;i<=k;i++)
    {
        pair< int, pair <int,int> > p=pq.top();
        pq.pop();
        int z=p.first;
        int diff=(z+1)/2;
        int x=p.second.first;
        int y=p.second.second;
       // cout<<x<<" "<<y<<" "<<z<<"\n";
           int f=diff+p.second.first;
        if(i==k)
        {
           mi=min(f-x-1,y-f-1);
           ma=max(f-x-1,y-f-1);

        }
        pq.push(make_pair(f-x-1,make_pair(x,f)));
           pq.push(make_pair(y-f-1,make_pair(f,y)));

    }

     cout<<"Case #"<<(t+1)<<": "<<ma<<" "<<mi<<"\n"; 
 }
    return 0;
}
