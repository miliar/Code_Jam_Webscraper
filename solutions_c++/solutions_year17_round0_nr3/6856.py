#include <bits/stdc++.h>
#define f(i,a,b,s) for (int i = a; i <= b; i = i + s)

using namespace std;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w+", stdout);
    int tc;
    cin >> tc;
    f(m,1,tc,1)
    {
        int N,K,i,j,piv;
        vector<int> q;
        cin >> N >> K;
        q.push_back(0);
        q.push_back(N+1);
        i = 0;
        j = N+1;
        while (K != 0 )
        {
            piv = i + ((j-i)/2);
            //cout << piv << "\n";
            q.push_back(piv);
            sort(q.begin(),q.end());
            int mx =0;
            for (vector<int>::iterator it = q.begin(); it != q.end()- 1; it++)
            {
                 if (*(it+1) - *it > mx)
                 {
                     mx = *(it+1) - *it;
                     //cout << "mx =" << mx << "\n";
                     i = *it;
                     j = *(it+1);
                     //cout << "i =" << i << "\n";
                    // cout << "j =" << j << "\n";
                 }

            }
            K--;
        }
        int ls, rs;
        for (vector<int>::iterator it = q.begin(); it != q.end(); it++)
            {
                 if (*it == piv)
                 {
                     ls = piv - *(it-1) -1;
                     rs = *(it+1) - piv -1;
                 }

            }
        cout << "Case #"  << m <<": " << max(ls,rs) << " " << min(ls,rs) << "\n";
    }
    return 0;
}
