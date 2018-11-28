
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define mod 1000000007
#define vec vector<long long>
#define arl(n) array<long long,n>
#define ard(n) array<double,n>
#define sc(n) scanf("%lld",&n)
#define prn(n) printf("%lf\n",n)
#define prs(n) printf("%lld ",n)
#define pr() printf("\n")
#define pb push_back
#define mp make_pair
int main()
{
    ll t;
    sc(t);
    ll ii=1;
    while(t--)
    {
        ll n;
        sc(n);
        vector<arl(2)> v;
        bool b=0;
        for(ll i=0;i<6;i++)
        {
            ll a;
            sc(a);
            v.pb({n-a,i});
            if((i==1 || i==3 || i==5) && a)
            b=1;
        }
        sort(v.begin(),v.end());
        ll tp1,tp2,tp3;
        string st1,st2,st3;
        if(v[0][1]==0)
        st1 = "R";
        else if(v[0][1]==2)
        st1 = "Y";
        else if(v[0][1]==4)
        st1 = "B";
        if(v[1][1]==0)
        st2 = "R";
        else if(v[1][1]==2)
        st2 = "Y";
        else if(v[1][1]==4)
        st2 = "B";
        if(v[2][1]==0)
        st3 = "R";
        else if(v[2][1]==2)
        st3 = "Y";
        else if(v[2][1]==4)
        st3 = "B";
        tp1 = n-v[0][0],tp2 = n-v[1][0],tp3 = n-v[2][0];
        //cout<<tp1<<" "<<st1<<" "<<tp2<<" "<<st2<<" "<<tp3<<" "<<st3<<endl;
        string s = "";
        if(tp1>(tp2+tp3))
        cout<<"Case #"<<ii<<": IMPOSSIBLE\n";
        else if(tp1 == tp2 && tp2 == tp3)
        {
            for(ll i=0;i<tp1;i++)
            s = s+"RYB";
            cout<<"Case #"<<ii<<": "<<s<<"\n";
        }
        else
        {
            for(ll i=0;i<tp1;i++)
            {
                s = s+st1;
                if(tp2==0)
                {
                    s = s+st3;
                    tp3--;
                }
                else
                {
                    s=s+st2;
                    tp2--;
                }
            }
            ll i=1;
            while(tp3>0)
            {
                s.insert(i,st3);
                tp3--;
                i+=2;
            }
            cout<<"Case #"<<ii<<": "<<s<<"\n";
        }
        ii++;
    }
    return 0;
}