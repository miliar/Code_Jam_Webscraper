#include <bits/stdc++.h>

#define ll long long

using namespace std;

ll arr[100];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outAl.txt","w",stdout);

    ll t=1,T;
    cin >> T;
    while(T--)
    {
        ll i,j,k,l,m,n;
        string a;
        cin >> a >> k;
        ll ans=0;
        l=a.length();
        for(i=0;i<l-k+1;i++)
        {
            if(a[i]=='-')
            {
                for(j=i;j<i+k;j++)
                {
                    if(a[j]=='+')
                        a[j]='-';
                    else
                        a[j]='+';
                }
                ans++;
            }

        }


        ll fl=0;
        //cout << a << " " << k <<  endl;
        for(i=0;i<l;i++)
        {
            if(a[i]=='-')
            {
                fl=1;
                break;
            }
        }
        cout << "Case #" <<t++ <<": ";
        if(fl)
        {
            cout << "IMPOSSIBLE";
        }
        else
            cout << ans;
        cout << endl;






    }
}













