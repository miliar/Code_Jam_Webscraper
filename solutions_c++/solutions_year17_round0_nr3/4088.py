#include <bits/stdc++.h>

using namespace std;

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
        long long n,k;
        cin>>n>>k;
        multiset<long long> num;
        num.insert(-n);
        for (int i=1;i<k && !num.empty();i++)
        {
            long long s = *num.begin();
            num.erase(num.begin());
            s=-s;
            if (s/2) num.insert(-(s/2));
            if ((s-1)/2) num.insert(-((s-1)/2));
        }
        if (num.empty()) cout<<"0 0"; else
        {
            long long s = *num.begin();
            s=-s;
            cout<<s/2<<' ';
            cout<<((s-1)/2);
        }
        cout<<endl;
    }
    return 0;
}
