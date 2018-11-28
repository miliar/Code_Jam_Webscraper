#include<bits/stdc++.h>
using namespace std;
int isTidy(int n)
{
    int d1,d2,tmp;
    tmp=n;
    d1=n%10;
    n/=10;
    while(n>0)
    {
        d2=n%10;
        //cout << d1 <<" "<<d2<<endl;
        if(d2 <= d1)
        {
                n/=10;
                d1=d2;
        }
        else
        {
                break;
        }
    }
    //cout << n;
    if(n==0)
        return tmp;
    else
        return 0;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,n,cas=1;
    cin >> t;
    while(t--)
    {
        cin >> n;
        for(int i=n;i>=1;i--)
        {
            int tmp=isTidy(i);
            if(tmp!=0)
                {
                    cout <<"Case #"<<cas++<<": "<< tmp << endl;
                    break;
                }
        }
    }
    return 0;
}
