#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll t,cases=1;
ll func1(int size,int y)
{
    ll ans=0;
    for(int i=0;i<size;i++)
    {
        ans+=pow(10,i)*y;
    }
    return ans;
}
ll func2(int a,int y[],int size)
{
    ll an=0;
    int beg=size-a;
    int j=a-1;
    for(int i=beg;i<size;i++)
    {
        an+=pow(10,j)*y[i];
        j--;
    }
    return an;
}
int main() {
    
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("outB.txt","w",stdout);
    cin>>t;

    while(t--)
    {
        ll n;
        cin>>n;
        ll i=0;
        ll a[19]={-1};
        while(n)
        {
            a[i]=n%10;
            n=n/10;
            i++;
        }
        int size=i;
        int org[size];
        for(i=size-1;i>=0;i--)
        {
            org[size-i-1]=a[i];
        }

        vector<int> out;
        ll j=0;
        ll str=0;
        for(i=size;i>=1;i--)
        {
            if(func2(i,org,size)>=func1(i,org[j]))
            {
                out.push_back(org[j]);
                j++;
            }
            else
            {
                if(org[j]!=1)
                out.push_back(org[j]-1);
                str=i-1;
                break;
            }
        }
        for(i=0;i<str;i++)
        out.push_back(9);
        ll answer=0;
        for(i=0;i<out.size();i++)
        {
            answer+=pow(10,out.size()-i-1)*out[i];
        }
	cout<<"Case #"<<cases<<": "<<answer<<endl;
        cases++;
    }
	return 0;
}


