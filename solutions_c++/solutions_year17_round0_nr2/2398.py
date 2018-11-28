#include <bits/stdc++.h>
using namespace std;
typedef double ld;
#define y1 cgbngfgn
#define pb push_back
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define fir first
#define m_p make_pair
#define sec second
#define files(name) freopen(name".sol","r",stdin); freopen (name".dat","w",stdout);
int a[20000];
bool check(string st)
{
    if (st[0]=='0') return(0);
    for (int i=1;i<st.size();i++)
        if (st[i]<st[i-1]) return(0);
    return(1);
}
signed main()
{
    //files("graph");

    int t;
    cin>>t;
    for (int l=1;l<=t;l++)
    {
        string st;
        cin>>st;
        vector<string> vec;
        for (int i=0;i<st.size();i++)
        {
            string now=st;
            for (int j=i+1;j<now.size();j++)
                now[j]=now[j-1];
            if (check(now)) vec.pb(now);
        }
        for (int i=0;i<st.size();i++)
        {
            string now=st;
            if (now[i]!='0') now[i]--;
            for (int j=i+1;j<now.size();j++)
                now[j]='9';
            if (check(now)) vec.pb(now);
        }
        string maybe="";
        for (int i=1;i<st.size();i++)
            maybe+='9';
        bool ch=1;
        sort(vec.begin(),vec.end());
        reverse(vec.begin(),vec.end());
        for (int i=0;i<vec.size();i++)
            if (vec[i]<=st && ch)
            {
                cout<<"case #"<<l<<": "<<vec[i]<<'\n';
                ch=0;
            }
        if (ch)
            cout<<"case #"<<l<<": "<<maybe<<'\n';
    }
}
