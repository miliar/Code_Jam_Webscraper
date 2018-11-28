#include<bits/stdc++.h>
#define pii pair<int,int>
#define ft first
#define sd second
#define mp make_pair
#define pb push_back
using namespace std;
int main()
{
    ifstream inp;
    ofstream out;
    inp.open("input.txt");
    out.open("output.txt");
    int T,n;
    inp>>T;
    for(int t=1;t<=T;t++)
    {
        inp>>n;
        vector<int> v(6);
        for(int i=0;i<6;i++)
            inp>>v[i];
        out<<"Case #"<<t<<": ";
        bool flag = 0;
        for(int i=0;i<6;i++)
        {
            if(v[i]>n/2)
            {
                out<<"IMPOSSIBLE"<<endl;
                flag = 1;
                break;
            }
        }
        if(flag)
            continue;
        vector<pii > a;
        for(int i=0;i<6;i++)
        {
            if(v[i])
            {
                a.pb(mp(v[i],i));
            }
        }
        sort(a.begin(),a.end());
        reverse(a.begin(),a.end());
        string ans;
        int i=0,j=1;
        unordered_map<int,char> ch;
        ch[0]='R';
        ch[2]='Y';
        ch[4]='B';
        while(i<a.size() || j<a.size())
        {
            if(i<a.size() && a[i].ft!=0)
            {
                ans.pb(ch[a[i].sd]);
                a[i].ft--;
            }
            if(j<a.size() && a[j].ft!=0)
            {
                ans.pb(ch[a[j].sd]);
                a[j].ft--;
            }
            if(j<a.size() && a[j].ft==0)
                j++;
            if(i<a.size() && a[i].ft==0)
                i+=2;
        }
        int cnt=1;
        j=ans.size()-1;
        while(j>0 && ans[j]==ans[j-1])
        {
            cnt++;
            j--;
        }
        cout<<cnt<<endl;
        if(cnt>1 && cnt&1)
        {
            int i=0,j=ans.size()-2;
            for(int k=0;k<cnt/2;k++)
            {
                swap(ans[i],ans[j]);
                i+=2;
                j-=2;
            }
            swap(ans[0],ans[i]);
        }
        else
        {
            int i=0,j=ans.size()-1;
            for(int k=0;k<cnt/2;k++)
            {
                swap(ans[i],ans[j]);
                i+=2;
                j-=2;
            }
        }
        out<<ans<<endl;
        //cout<<ans<<endl;
    }
    return 0;
}
