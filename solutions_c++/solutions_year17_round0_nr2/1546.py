#include<bits/stdc++.h>

using namespace std;

bool check(long long n)
{
    int c=9;
    while(n>0)
    {
        if(n%10>c)
            return false;
        c=n%10;
        n/=10;
    }
    return true;
}

long long getprev(long long n)
{
    int c=9,i=0;;
    while(n%10<=c)
    {
        c=n%10;
        n/=10;
        i++;
    }
    n--;
    while(i--)
        n=n*10+9;

    return n;
}

int main()
{
    freopen("000.in","r",stdin);
    freopen("0002.txt","w",stdout);

    long long t,n,l;

    cin>>t;

    for(l=1;l<=t;l++)
    {
        cin>>n;

        while(!check(n))
            n=getprev(n);

        cout<<"Case #"<<l<<": "<<n<<endl;

    }

    return 0;
}
