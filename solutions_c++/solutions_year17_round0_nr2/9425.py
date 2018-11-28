#include <iostream>
#include <cstdio>
using namespace std;

bool isTidy(int n)
{
    bool tidy=true;
    int c=10;
    while(n)
    {
        if((n%10)>c) return false;
        c=n%10;
        n=n/10;
    }
    return true;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t;
    cin >> t;
    int cs=1;
    int n;

    while(t--)
    {
        cin >> n;
        for(int i=n;i>=1;i--)
        {
            if(isTidy(i))
            {
                printf("Case #%d: ",cs++);
                cout << i << endl;
                break;
            }
        }

    }

    return 0;
}
