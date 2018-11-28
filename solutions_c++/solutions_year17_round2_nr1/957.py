//
//  main.cpp
//  A
//
//  Created by Volodymyr Polosukhin on 22/04/2017.
//  Copyright © 2017 Volodymyr Polosukhin. All rights reserved.
//

#include <iostream>
#include <vector>
#include <tuple>
#include <list>

using namespace std;

const long double EPS = 1e-9;
const long double INF = 1e18;

long double solveSmall(long long d, vector < list < tuple < long double, long double, long double > > > ks)
{
    sort(ks.begin(), ks.end());
    
    long double totalTime;
    
    if (1 == ks.size())
    {
        totalTime = (d - get<0>(ks[0].back())) / get<2>(ks[0].back());
    }
    else
    {
        long double timeIntersection = 0;
    }
    
    return d / totalTime;
}

long double solveLarge(long long d, vector < list < tuple < long double, long double, long double > > > ks)
{
    sort(ks.begin(), ks.end());
    
    for (int i = (int)ks.size()-2; i >= 0; --i)
    {
        for (auto kilometerTimeSpeed : ks[i+1])
        {
            long double kilometer1, time1, speed1, kilometer2, time2, speed2;
            
            tie(kilometer1, time1, speed1) = ks[i].back();
            tie(kilometer2, time2, speed2) = kilometerTimeSpeed;
            
            long double time3 = (kilometer1 - speed1 * time1 - kilometer2 + speed2 * time2) / (speed2 - speed1);
            
            if (time3 + EPS > time1 && time3 + EPS > time2)
            {
                long double kilometer3 = speed1 * (time3 - time1) + kilometer1;
                
                if (kilometer3 < d + EPS)
                {
                    ks[i].emplace_back(kilometer3, time3, speed2);
                }
            }
        }
    }
    
    long double totalTime = (d - get<0>(ks[0].back())) / get<2>(ks[0].back()) + get<1>(ks[0].back());
    long double answer = d / totalTime;
    
    return answer;
}

int main(int argc, const char * argv[]) {
    freopen("A-small-attempt1.in.txt", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    
    cout.precision(6);
    cout.setf(ios::fixed);
    
    int t;
    cin >> t;
    
    for (int testcase = 1; testcase <= t; ++testcase)
    {
        long long d;
        int n;
        
        cin >> d >> n;
        
        vector < list < tuple < long double, long double, long double > > > ks(n);
        
        for (int i = 0; i < n; ++i)
        {
            int k;
            int s;
            
            cin >> k >> s;
            ks[i].emplace_back(k, 0,  s);
        }
        
        long double answer = solveLarge(d, ks);
        
        cout << "Case #" << testcase << ": " << answer << endl;
    }
    
    return 0;
}
