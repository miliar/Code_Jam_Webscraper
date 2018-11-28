#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

int main()
{
    freopen("a","r",stdin);
    freopen("b","w",stdout);
    int t;
    cin >> t;
    int g=1;
    while(t--)
    {
        cout << "Case #" << g << ": ";
        g++;
        int d,n;
        cin >> d >> n;
        //list<pair<int,int> > hrs;
        double mxtime=0;
        for (int i=0;i<n;i++)
        {
            int ps;
            cin >> ps;
            int sp;
            cin >> sp;
            double tm=(double)(d-ps)/(double)(sp);
            mxtime=max(mxtime,tm);
        }
        printf("%.8f\n",(double)d/mxtime);
    }
    return 0;
}
