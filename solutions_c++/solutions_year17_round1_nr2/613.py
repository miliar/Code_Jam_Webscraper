#include <fstream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

int main()
{
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int t;
    in >> t;
    for (int qq; qq<t; qq++)
    {
        out << "Case #" << qq+1 << ": ";
        int n, p;
        in >> n >> p;
        vector<long> ing;
        for (int i = 0; i<n; i++)
        {
            long a;
            in >> a;
            ing.push_back(a);
        }
        priority_queue<pair<long, long> > * q = new priority_queue<pair<long, long> >[n];
        for (int i = 0; i<n; i++)
        {
            for (int j = 0; j<p; j++)
            {
                long a;
                in >> a;
                long b = round(a*1.0/ing[i]);
                if (abs(b*ing[i]-a)<=b*ing[i]/10)
                {
                    long l = b, u = b;
                    while (abs((l-1)*ing[i]-a)<=(l-1)*ing[i]/10)
                    {
                        l--;
                    }
                    while (abs((u+1)*ing[i]-a)<=(u+1)*ing[i]/10)
                    {
                        u++;
                    }
                    q[i].push(make_pair(l,u));
                    //out << a << ' ' << b << ' ' << l << ' ' << u << '\n';
                }
            }
        }
        long ** top = new long*[2];
        top[0] = new long[n];
        top[1] = new long[n];

        bool done = false;
        for (int i = 0; i<n; i++)
        {
            if (q[i].empty())
            {
                //out << "0\n";
                done = true;
                break;
            }
            top[0][i] = q[i].top().first;
            top[1][i] = q[i].top().second;
            //out << top[0][i] << ' ' << top[1][i] << ' ';
        }
        //out << '\n';
        int sum = 0;
        while (!done)
        {
            int mxl = top[0][0], mnu = top[1][0];
            vector<int> mxI;
            bool eq = true;
            for (int i = 0; i < n; i++)
            {
                if (top[1][i] >= mxl && top[0][i] <=mnu)
                {
                    if (top[1][i]<mnu)
                        mnu = top[1][i];
                    if (top[0][i]>mxl)
                        mxl = top[0][i];
                    mxI.push_back(i);
                }
                else
                {
                   eq = false;
                   if (top[0][i]>mnu)
                   {
                       mxl = top[0][i];
                       mnu = top[1][i];
                       mxI.clear();
                       mxI.push_back(i);
                   }
                }
            }
            /*for (int k = 0; k<n; k++)
            {
                out << top[0][k] << ' '<< top[1][k] << " / ";
            }*/
            //out << '\n';
            if (eq)
            {
                sum++;
                for (int i=0; i<n; i++)
                {
                    q[i].pop();
                    if (q[i].empty())
                        done = true;
                    else
                    {
                        top[0][i] = q[i].top().first;
                        top[1][i] = q[i].top().second;
                    }
                }
                mxI.clear();
            }
            else
            {
                for (int i : mxI)
                {
                    q[i].pop();
                    if (q[i].empty())
                        done = true;
                    else
                    {
                        top[0][i] = q[i].top().first;
                        top[1][i] = q[i].top().second;
                    }
                }
                mxI.clear();
            }
        }
        out << sum <<'\n';
    }
    in.close();
    out.close();
    return 0;
}
