#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <iomanip>

using namespace std;




int main()
{
    //ios::sync_with_stdio(false);
    //cin.tie(0);
    //freopen("small.out", "w", stdout);
//    freopen("small.in", "r", stdin);



    long long nbT;
    cin >> nbT;
    long double maxi;
    vector<pair<long double,pair<long double, long double>>> pans;


    for (long long t = 1; t <= nbT; t++)
    {
        pans.resize(0);
        int N, K;
        cin >> N >> K;
        maxi = 0;

        for (int i = 0; i < N; i++)
        {
            long double r,h;
            cin >> r >> h;
            pans.push_back({h*r,{h, r}});

        }

        long double best = 0;
        sort (pans.rbegin(), pans.rend());
        //for (int i = 0; i < N; i++)
        //    std::cout << pans[i].first << "lol" << pans[i].second << '\n';
        //return 0;

        long double prop1 = 0;
        long double base = 0;
        long double maxiBase = 0;
        for (int i = 0; i < K-1; i++)
        {
//            std::cout << "lol\n";
            base += pans[i].first*2*M_PI;
            maxiBase = max(maxiBase, pans[i].second.second*pans[i].second.second*M_PI);
        }
        for (int i = K-1; i < N; i++)
        {
            long double curSurf = pans[i].second.second*pans[i].second.second*M_PI;
            long double cur = 2*M_PI*pans[i].first;
            if (curSurf > maxiBase)
                cur += curSurf;
            else
                cur+= maxiBase;
            maxi = max(cur, maxi);
        }


        //cout << "rrrr" << taille << endl;
        std::cout << "Case #" << t << ": ";
        std::cout << std::fixed;
        std::cout << std::setprecision(7);
        std::cout << base+maxi << "\n";


    }

    return 0;
}



