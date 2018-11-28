//cot2.cpp
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
#define fa_io std::ios::sync_with_stdio(false)

int main()
{
    fa_io;
    cin.tie(NULL);
    freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-small-2-attempt0.out","w",stdout);
    ll t,k,two=2,a;
    cin>>a;
    for(ll o=1;o<=a;o++)
    {
        cin>>t;
        cin>>k;
        priority_queue<ll> pq;
        pq.push(t);
        cout<<"Case #"<<o<<": ";
        for(ll z=1;z<=k;z++)
        {
            ll temp=pq.top();
            //cout<<temp<<'\n';
            pq.pop();
            if(temp%two)
            {
                if(temp==1 && z==k)
                    cout<<"0 0\n";
                else
                {
                    pq.push(temp/two);
                    pq.push(temp/two);
                    if(z==k)
                        cout<<temp/two<<' '<<temp/two<<'\n';
                }
            }
            else
            {
                if(temp==two)
                {
                    if(z==k)
                        cout<<"1 0\n";
                    pq.push(1);
                }
                else
                {
                    pq.push(temp/two);
                    pq.push((temp/two)-1);
                    if(z==k)
                        cout<<temp/two<<' '<<(temp/two)-1<<'\n';
                }
            }
        }
    }

    return 0;
}
