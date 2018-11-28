#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
long long n, ke, kebab, dzie, x, y;
int a;
int main()
{
     freopen("tat.txt", "r", stdin);
    freopen("tatodp.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for(int i = 1; i<=n; i++)
    {
        cin >> ke;
        while(ke > 0)
        {
            kebab = ke;
            y = kebab%10;
            kebab/=10;
            dzie=10;
            a = 1;
            while(kebab>0)
            {
                x = kebab%10;
                if(x<=y)
                {
                    dzie*=10;
                    y = x;
                    kebab/=10;
                    continue;
                }
                else
                {
                    ke-=ke%dzie+1;
                    a = 0;
                    break;
                }
            }
            if(a == 1)
            {
                cout << "Case #" << i << ": " << ke << "\n";
                break;
            }
        }
    }
    return 0;
}
