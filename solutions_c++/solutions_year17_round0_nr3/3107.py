#include <bits/stdc++.h>

using namespace std;

typedef long long lo;

int main()
{
    lo i, t, n, k, j, c, p;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n>>k;
        c = 1;
        p = 2;
        while(c<k)
        {
            c+=p;
            p*=2;
        }
        lo minimo, maximo;
        minimo = maximo = (n-c)/p;
        lo dif = n-c-maximo*p;
        p/=2;
        c-=p;
        //cout<<"c: "<<c<<endl<<"p: "<<p<<endl;
        if(k-c<=dif)
            maximo++;
        if(k-c+p<=dif)
            minimo++;
        //cout<<dif<<endl;
        //cout<<(n-c)/p<<endl;
        //cout<<c<<" "<<p<<endl;
        cout<<"Case #"<<i<<": "<<maximo<<" "<<minimo<<endl;
    }
    return 0;
}
