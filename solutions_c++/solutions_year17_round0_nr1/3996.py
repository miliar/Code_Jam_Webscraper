#include <bits/stdc++.h>

using namespace std;

vector<long long> a(2000),h(2000);
long long l;

long long res(string st, long long k)
{
    if (st.size() < k)
    {
        if (st.find('-') == -1) return 0;
        else return -1;
    }
    if (st.size() == k)
    {
        int cnt = 0;
        for (int i=0;i<st.size();i++) if (st[i]=='+') cnt++;
        cnt=st.size()-cnt;
        if (!cnt) return 0;
        else if (cnt - st.size() == 0) return 1;
        else return -1;
    }
    long long s = 0;
    long long ans = 0;
    for (int i = 0; i <= l - k; i++)
    {
        if (h[i]) s--;
        if (s%2) a[i] = 1 - a[i];
        if (!a[i])s++,ans++,h[i + k]=1,a[i] = 1;
    }
    for (int i = l - k + 1; i < l; ++i)
    {
        if (h[i]) s--;
        if (s%2)
            a[i] = 1 - a[i];
    }

    for (int i = 0; i < l; ++i)
        if (!a[i]) return -1;
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    //freopen("in.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int q=1;q<=t;q++)
    {
        cout<<"Case #"<<q<<": ";
        string cake;
        long long k;
        cin >> cake;
        l = cake.size();
        for (int i = 0; i < l; ++i) a[i] = (cake[i] == '+')?1:0,h[i] = 0;
        cin >> k;
        long long ans = res(cake,k);
        if (ans==-1) cout<<"IMPOSSIBLE"; else cout<<ans;
        cout<<endl;
    }
    return 0;
}
