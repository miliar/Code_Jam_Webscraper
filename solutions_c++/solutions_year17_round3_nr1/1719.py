#include<bits/stdc++.h>
#define LL long long
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
using namespace std;
const int INF=2000000009;
const int MX=100005;
const double PI=acos(-1);
const double EPS=1e-9;

int main()
{
    ifstream fin("input.in");
   // ofstream fout("output.txt");
    FILE *fp=fopen("output.txt","w");
    int tc;
    fin>>tc;
   // cout<<tc<<endl;
    int caseno=0;

    while (tc--)
    {
        int n,k;
        fin>>n>>k;
        pair<double,double> p[n];
        for (int i=0;i<n;i++)
            fin>>p[i].ff>>p[i].ss;
        double ar[n];
        double as[n];
        sort(p,p+n);
        double ans=0.0;
        for (int i=n-1;i>=0;i--)
        {
            ar[i]=PI*p[i].ff*p[i].ff;
            as[i]=2*PI*p[i].ff*p[i].ss;
        }
        set <double> st;
        for (int i=0;i<k;i++)
        {
            st.insert(as[i]);
            ans+=as[i];
        }
        double cur=ans;
        ans+=ar[k-1];
        for (int i=k;i<n;i++)
        {
            double temp=*st.begin();
            st.erase(st.begin());
            ans=max(ans,cur-temp+as[i]+ar[i]);
            cur-=temp;
            temp=max(temp,as[i]);
            st.insert(temp);
            cur+=temp;
        }
        //cout<<setprecision(9)<<ans<<endl;
        fprintf(fp,"Case #%d: %0.9lf\n",++caseno,ans);
    }
    fclose(fp);
    return 0;
}

