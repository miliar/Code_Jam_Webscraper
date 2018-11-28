#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;

ull D;
int n;
typedef struct __sp{
    ull d;
    int s;
    double tm;
}hr;



void solve(int tc)
{
    ull a,b;
    cout << "Case #"<< tc<<": ";
    cin >> D >> n;
    hr v[n];

    hr mx;
    double ti= 0;
    for(int i=0;i<n;i++)
    {
        cin >> a >> b;
        hr x;
        v[i].d = a;
        v[i].s = b;
        v[i].tm = (D-a)/double(b);
        if(ti < v[i].tm)
        {
            mx = v[i];
            ti = v[i].tm;
        }
    }

    printf("%0.6f\n",(D/ti));



}



int main(void)
{
    int tc=1;
    int T;
    cin >> T;
    while(T--)
        solve(tc++);

    return 0;
}
