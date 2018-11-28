#include <bits/stdc++.h>

#define ll long long

using namespace std;

ll arr[100];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);

    ll t=1,T;
    cin >> T;
    while(T--)
    {
        ll i,j,k,l,m,n;
        string a;
        cin >> a;
        l=a.length();
        for(i=0;i<l;i++)
        {
            arr[i]= a[i]-'0';

        }
        for(ll x=0;x<21;x++)
        {
            for(i=1;i<l;i++)
            {
                if(arr[i]<arr[i-1])
                {
                    arr[i-1]--;
                    for(j=i;j<l;j++)
                        arr[j]=9;
                }
            }
        }
        cout << "Case #" << t++ << ": ";
        i=0;
        while(arr[i]==0)
            i++;
        for(;i<l;i++)
            cout << arr[i];
        cout << endl;






    }
}













