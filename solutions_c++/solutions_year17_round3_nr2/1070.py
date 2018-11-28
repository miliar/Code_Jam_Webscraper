#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <time.h>
#include <assert.h>
#define MAXN 55
using namespace std;

typedef pair<int, int> ii;

int main(){
    freopen("/Users/Masoud/Desktop/B-small-attempt2.in", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    int t;
    int ca = 1;
    scanf("%d", &t);
    while(t--){
        int aj, ac;
        scanf("%d %d", &aj, &ac);
        vector<ii> ajs(aj);
        vector<ii>acs(ac);
        for (int i =0; i<aj; i++) {
            scanf("%d %d", &ajs[i].first, &ajs[i].second);
        }
        for(int i=0; i<ac; i++){
            scanf("%d %d", &acs[i].first, &acs[i].second);
        }
        if ((aj == 1 && ac == 0) || (aj == 0 && ac == 1) || (aj == 0 && ac == 0)) {
            printf("Case #%d: %d\n", ca++, 2);
            continue;
        }
        if(aj == 1 && ac == 1){
            vector<ii> nums;
            nums.push_back(acs[0]);
            nums.push_back(ajs[0]);
            sort(nums.begin(), nums.end());
            bool can_two = false;
            for(int i=0; i<=720; i++){
                if(nums[0].first>=i && nums[0].second<=i+720){
                    can_two = true;
                    break;
                }
            }
            if (can_two) {
                printf("Case #%d: %d\n", ca++, 2);
            }else{
                printf("Case #%d: %d\n", ca++, 4);
            }
            continue;
        }
        vector<ii> nums;
        for(int i=0; i<acs.size(); i++)
            nums.push_back(acs[i]);
        for(int i =0; i<ajs.size(); i++)
            nums.push_back(ajs[i]);
        sort(nums.begin(), nums.end());
        if (nums[0].first+720>=nums[1].second || nums[0].second + 720 <= nums[1].first) {
            printf("Case #%d: %d\n", ca++, 2);
        }else{
            printf("Case #%d: %d\n", ca++, 4);
        }
    }
    return 0;
}

