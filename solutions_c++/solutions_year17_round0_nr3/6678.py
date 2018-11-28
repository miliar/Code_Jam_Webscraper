#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll  long long int
#define X first
#define Y second
using namespace std;
struct comp
{
    bool operator()(const pair<int,int>& l,const pair<int,int>& r)
    {
        int lval,rval,lmax,lmin,rmax,rmin;
        if(l.X%2==0) lval=l.X/2;
        else         lval=(l.X+1)/2;

        if(r.X%2==0) rval=r.X/2;
        else         rval=(r.X+1)/2;

        lmax=max(l.X-lval,lval-1);
        lmin=min(l.X-lval,lval-1);

        rmax=max(r.X-rval,rval-1);
        rmin=min(r.X-rval,rval-1);

        if(lmin!=rmin) return lmin<rmin;
        if(lmax!=rmax) return lmax<rmax;
        return l.Y+lval>r.Y+rval;
    }
};
int main()
{
    int t,k,i,j,c,n,m;
    ofstream out;int pp=1;
    out.open("output.txt");
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        cout<<"Case #"<<pp<<": ";
        out<<"Case #"<<pp<<": ";pp++;
        priority_queue<pair<int,int>,vector<pair<int,int> >,comp> q;
        q.push(mp(n,0));
        k--;
        while(k--)
        {
            i=q.top().X;
            j=q.top().Y;
            q.pop();
            int val;
            if(i%2==0) val=i/2;
            else       val=(i+1)/2;

            q.push(mp(val-1,j));
            q.push(mp(i-val,j+val));
        }
            i=q.top().X;
            j=q.top().Y;
            q.pop();
            int lval,rval;
            if(i%2==0) lval=i/2;
            else       lval=(i+1)/2;
            rval=i-lval;
            lval--;
            cout<<max(lval,rval)<<" "<<min(lval,rval)<<endl;
            out<<max(lval,rval)<<" "<<min(lval,rval)<<endl;
    }
    return 0;
}
