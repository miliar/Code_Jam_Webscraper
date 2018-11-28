#define _USE_MATH_DEFINES

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <string.h>
#include <stack>
#include <list>
#include <math.h>

using namespace std;


int main(int argc, const char * argv[])
{
    int test_case;
    cin >> test_case;
    
    for(int z = 1; z <= test_case; z++) {
        int n, k;
        vector<pair<long long, int> > v;
        vector<pair<int, pair<long long, long long> > > v2;
        cin >> n >> k;
        for(int i = 0; i < n; i++) {
            int t1, t2;
            scanf("%d %d", &t1, &t2);
            v2.push_back(make_pair(t1, make_pair(t2, i)));
        }
        sort(v2.begin(), v2.end());
        
        for(int i = 0; i < n; i++) {
            v2[i].second.second = i;
            v.push_back(make_pair((long long)2 * (long long)v2[i].first * (long long)v2[i].second.first, i));
        }
        
        sort(v.begin(), v.end());
        
        long long m = 0;
        
        
        for(int i = 0; i <= n - k; i++) {
            int pick  = n - 1 - i;
            long long result = (long long)v2[pick].first * (long long)v2[pick].first;
            result += (long long)v2[pick].first * (long long)v2[pick].second.first * (long long)2;
            
            int count = 0;
            int index = 0;
            while(n - 1 - index >= 0 && count != k - 1) {
                if(v[n - 1 - index].second < pick) {
                    count++;
                    result += v[n - 1 - index].first;
                }
                index++;
            }
            m = max(m, result);
        }
        
        
        printf("Case #%d: ", z);
        printf("%.7lf", (double)m * (double)M_PI);
        printf("\n");
    }
    
    return 0;
}
