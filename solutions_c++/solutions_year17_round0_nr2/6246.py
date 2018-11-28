#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;
typedef long long ll;

int main()
{
    //freopen("#input.in","r",stdin);
    //freopen("#output.in","w",stdout);

    ll t,i,j,k,n;
    vector<int> v;
    cin>>t;

    for(i=1; i<=t; i++)
    {
        cin>>n;
        v.clear();
        while(n)
        {
            v.push_back(n%10);
            n/=10;
        }
        reverse(v.begin(), v.end());

        for(j=0; j<v.size()-1; j++)
        {
            if(v[j]>v[j+1])
            {
                v[j]--;
                for(k=j+1; k<v.size(); k++)
                    v[k]=9;
                j=-1;
            }
        }
        j=0;
        while(v[j]==0)
            j++;
        cout<<"Case #"<<i<<": ";
        while(j<v.size())
        {
            cout<<v[j];
            j++;
        }
        cout<<endl;
    }
    return 0;
}

