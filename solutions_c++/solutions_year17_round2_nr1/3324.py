#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define sf_d(var) scanf("%d",&var)
#define sf_2d(var1,var2) scanf("%d %d",&var1,&var2)
#define vi vector<int>
#define vvi vector< vector<int> >
#define pb push_back
#define v_iter vector<int>::iterator
#define v_riter vector<int>::reverse_iterator
#define fr_z(start,end) for(int z=start;z<end;z++)
#define fr_o(start,end) for(int o=start;o<end;o++)
#define w while
#define mod 1000000007
#define srt(cont) sort(cont.begin(),cont.end())
#define all(m) m.begin(),m.end()
#define mp make_pair
#define mprq(a,b) priority_queue< pair<a,b> ,vector< pair<a,b> >,greater< pair<a,b> > >
#define fa_io std::ios::sync_with_stdio(false)

int main()
{
    fa_io;
    cin.tie(NULL);
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int t;
    cout<<setprecision(6)<<fixed;
    cin>>t;
    fr_o(1,t+1)
    {
        cout<<"Case #"<<o<<": ";
        int d,n;
        cin>>d>>n;
        vector<double> v;
        double a,b;
        fr_z(0,n)
        {
            cin>>a>>b;
            a=d-a;
            v.pb(a/b);
        }
        sort(v.begin(),v.end());
        cout<<(double)d/(*(v.end()-1))<<'\n';
    }

    return 0;
}
