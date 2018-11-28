#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,d,n;
    int x,v;
    double maxtime;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        cin >> d >> n;
        maxtime=0;
        for (int j=0;j<n;j++)
        {
            cin >> x >> v;
            maxtime=max(double(d-x)/double(v),maxtime);
        }
        cout.precision(6);
        cout << fixed << "Case #" << i+1 << ": " << double(d)/maxtime << "\n";
    }
}
