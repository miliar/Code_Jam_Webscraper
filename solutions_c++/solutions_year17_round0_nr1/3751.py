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
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int t,k;
    cin>>t;
    fr_z(1,t+1)
    {
        string s;
        cin>>s;
        int cnt=0;
        string::iterator iter,iter1;
        cin>>k;
        for(iter=s.begin();iter!=s.end();iter++)
            if(*iter=='-')
                break;
        for(;iter+(k-1)<s.end();)
        {
            iter1=iter;
            fr_z(1,k+1)
            {
                if(*iter1=='+')
                    *iter1='-';
                else if(*iter1=='-')
                    *iter1='+';
                iter1++;
            }
            cnt++;
            //cout<<s<<'\n';
            iter++;
            for(;iter!=s.end();iter++)
                if(*iter=='-')
                    break;
        }
        cout<<"Case #"<<z<<": ";
        if(iter!=s.end())
            cout<<"IMPOSSIBLE";
        else
            cout<<cnt;
        cout<<'\n';
    }
    return 0;
}
