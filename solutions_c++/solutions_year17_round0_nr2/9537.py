#include<iostream>
#include<bits/stdc++.h>
#define ull unsigned long long
using namespace std;
int ist(ull n, int len)
{
    int x[len];
    for(int i=len-1; i>=0; i--)
    {
        x[i]= n%10;
        n/=10;
    }

    for(int i=0; i<len-1; i++)
        if(x[i]>x[i+1])
            return i+1;
        return len;
}
ull pw(int t)
{
    ull x = 1;
    for(int i=0; i<t; i++)
        x*=10;
    return x;
}
int getsize(ull n)
{
    int ret=0;
    while(n)
    {
        ret++;
        n/=10;
    }
    return ret;
}
ull ezbot(ull n, int len, int it, int k)
{
    int co = len -it;
    for(int i = 0; i<co ;i++)
    {
        ull temp = (n%pw(k))*pw(i);
        n-=temp;
    }
    return n;
}
int main()
{
    int t;
    cin >> t;
    for(int j = 0; j<t; j++)
    {
        ull n;
        cin >> n;
        int len = getsize(n);
        cout << "Case #" << j+1 << ": ";
        if(ist(n, len)== len){
            cout << n << endl;
            continue;
        }
        int k = 0;
        while(ist(n-1, len)!= getsize(n))
        {
            int it = ist(n, len);
            n = ezbot(n, len, it, k++);
        }
        cout << n-1 << endl;
    }

    return 0;
}
