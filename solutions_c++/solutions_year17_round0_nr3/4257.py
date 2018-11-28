#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
void solve(long long int n, long long int k, long long int* ans)
{       
        long long int seg = 0, tk=k+2, tn=n;
        while (tk >>= 1) seg++;// seg start wth 1
        long long int x = (1 << (seg)) - 2;
        if (seg == 1)  x = 0;
        x = k+1 - x;

        long long int l = 1, s = 1;
        long long int larger = n >> 1, smaller = n - larger-1;

        for (int i = 0; i < seg-1; ++i)
        {   
            if (larger & 1)
            {   
                if (smaller & 1)
                {
                    l = (l+s)*2;
                    s = 0;
                }
                else 
                    l = l*2+s;
                larger = (larger >> 1);
                smaller = larger-1;
            }
            else 
            {   
                if ((smaller & 1) == 0)
                {   s = l+s;
                    l = s;
                }
                else 
                {   s = l + s*2;
                    
                }
                larger = (larger >> 1);
                smaller = larger - 1;
            }

        }

        if ( x <= l )
        {
            ans[0] = (larger >> 1);
            ans[1] = larger-1-ans[0];
        }
        else 
        {
            ans[0] = (smaller >> 1);
            ans[1] = smaller - 1 - ans[0];
        }

}
int main()
{   
    int T;
    cin >> T;
    for (int kase = 1; kase <= T; kase++)
    {   long long int n, k;
        cin >> n >> k;
        long long int ans[2];
        if (k == 1) 
        {
            ans[0] = n >> 1;
            ans[1] = n - ans[0] - 1;
        }
        else solve(n, k-2, ans);
        if (ans[0] < ans[1] ) swap(ans[0], ans[1]);
        if (ans[1] < 0) ans[1] = 0;
        cout << "Case #" << kase <<": " << ans[0] << " " << ans[1] << endl;
    }
}
