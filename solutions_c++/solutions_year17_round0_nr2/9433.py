#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<n;++i)
#define repp(i,a,b) for(int i=a;i<b;++i)
using namespace std;
typedef long long int ll;

ll counting_sort(ll temp)
{
    ll r = 0;
    for (ll i=0; i<10; i++)
        for(ll j=temp; j!=0; j/= 10)
            if (j % 10 == i)            
                r = 10 * r + i;
    return r;
}


int main()
{

freopen("input","r",stdin);
freopen("o","w",stdout);

int x;
cin>>x;

for(int no=1;no<=x;no++)
{
	cout<<"Case #"<<no<<": ";
    ll a;
    cin>>a;

    while(1)
    {
        if(a == counting_sort(a))
			break;
        a--;
    }
    
    cout<<a<<endl;
}
return 0;
}