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
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    ll t;
    cin>>t;
    fr_z(1,t+1)
    {
        string s;
        cin>>s;
        string::iterator iter=s.begin(),iter1;
        bool k=true;
        for(;iter!=s.end()-1;iter++)
            if(*iter>*(iter+1))
            {
                k=false;
                break;
            }
        cout<<"Case #"<<z<<": ";
        if(k)
            cout<<s;
        else
        {
            if(*iter=='1')
                fr_o(1,s.length())
                    cout<<9;
            else
            {
                iter1=iter-1;
                while(iter1!=s.begin()-1 && *iter1==*iter)
                {
                    iter=iter1;
                    iter1--;
                }
                *iter-=1;
                for(iter++;iter!=s.end();iter++)
                    *iter='9';
                cout<<s;
            }
        }
        cout<<'\n';
    }
    return 0;
}
