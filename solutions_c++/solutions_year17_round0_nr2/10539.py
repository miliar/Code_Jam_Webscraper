#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    long long int t,n;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long int countDig = 0,m,c;
        cin>>n;
        m = n;
        c = n;
        for(int j=0;m!=0;j++)
        {
            m /=10;
            countDig++;
        }
        if(n/10==0)
        {
            cout<<"\nCase #"<<i<<": "<<n;
            continue;
        }
        else
        {
            while(true)
            {
                int store1=0,store2=9;
                bool flag = true;
                for (int k=1;n!=0;k++)
                {
                    store1 = n%10;
                    if(store1<=store2)
                    {
                        store2 = store1;
                        flag = true;
                    }
                    else
                    {
                        flag = false;
                        break;
                    }
                    n /=10;
                }
                if(flag)
                {
                    cout<<"\nCase #"<<i<<": "<<c;
                    break;
                }
                else
                {
                    c--;
                    n = c;
                    continue;
                }
            }
        }
    }
    return 0;
}
