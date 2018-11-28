#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test, n, m;
    cin >> test;
    for (int i = 1; i <= test; ++i)
    {
        long long int n,z,c=0,p=0,gino,count=0,jawab,har;
        cin>>n;
yha:
        c=0;
        z=n;
        p=0;
        count=0;
        while(z!=0)
        {
            har=z%10;
            z=z/10;

            if(c&&gino<har)
            {
                p=1;
                break;
            }
            gino=har;
            c=1;
            count++;
        }
        if(p)
        {
            jawab=z;
            jawab=jawab*10+har-1;
            while(count--)
                jawab=jawab*10+9;
            n=jawab;

            goto yha;
        }
        else
            cout << "Case #" << i << ": " << n<< endl;
    }
}
