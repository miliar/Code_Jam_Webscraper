#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define x first
#define y second
FILE *fin = freopen("in.txt","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);
int main()
{
    int t;
    cin>>t;
    for(int b=1;b<=t;b++)
    {   vector<pair<long long int,long long int> > v;
        long long int n,k;
        cin>>n>>k;
        v.pb(mp(n,1));
       long long  int l=0;
        while(k>0)
        {
            k-=v[l].y;
             long long int one=(v[l].x-1)/2;
            long long int two=ceil((float)(v[l].x-1)/2.0);
            if(k<=0)
            {
                cout<<"Case #"<<b<<": "<<max(one,two)<<" "<<min(one,two)<<endl;
                continue;
            }
            if(v[v.size()-1].x==two)
            {
                v[v.size()-1].y+=v[l].y;
            }
            else v.pb(mp(two,v[l].y));
            if(v[v.size()-1].x==one)
                v[v.size()-1].y+=v[l].y;
            else v.pb(mp(one,v[l].y));
            l++;


        }
        for(int i=0;i<v.size();i++)
        {
           // cout<<v[i].x<<" "<<v[i].y<<endl;
        }
    }
}
