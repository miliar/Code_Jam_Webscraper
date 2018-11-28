#include<iostream>
using namespace std;
int fun(int a[], int s)
{
    int f = 0;
    for(int i = 1; i <= s; i ++)
    {
        for(int j = i + 1; j <= s; j ++)
        {
            if(a[i] >= a[j])
            {
                f = 1;
            }
            else
            {  
                f = 0;   
                goto l;
            }
        }
    }
    l:
    if(f == 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int  num(int a[], int s)
{
    int i = 1;
    int m = 0;
    int t = 1;
    while(s)
    {
        m = m + (a[i] * t);
        t = t * 10;
        s--;
        i++;
    }
    return m;
}
int main()
{
    int T;
    int i = 1,x;
    cin>>T;
    int y;
    int re[10000],h = 0;
    while(T--)
    {
        cin>>x;
        while(x)
        {
            y = x;
            i = 1;
            int a[10000];
            while(y)
            {
                a[i++] = y % 10;
                y = y / 10;
            }
            if(i == 2)
            {
                re[h++] = x;
                break;
            }
            else if(fun(a,i-1) == 1)
            {
                re[h++] = num(a, i-1);
                break;
            }
            x--;
        }
    }
    for(int i = 0; i < h; i++)
    {
        cout<<"Case #"<<i+1<<": "<<re[i]<<endl;
    }
    return 0;
}
