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
#define MAXN 10000000
using namespace std;

typedef pair<double, double> dd;
int main(){
    freopen("/Users/Masoud/Desktop/A-small-attempt0.in", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    int t;
    int ca = 1;
    scanf("%d", &t);
    while(t--){
        double d;
        int n;
        scanf("%lf %d", &d, &n);
        vector<dd> nums;
        for(int i=0; i<n; i++){
            double pos, speed;
            scanf("%lf %lf", &pos, &speed);
            nums.push_back({pos,speed});
        }
        sort(nums.begin(), nums.end());
        double t = 0;
        bool got_dest = false;
        while(!got_dest){
            double min_time = 100000000000.0;
            int idx = -1;
            for(int i=0; i<nums.size()-1; i++){
                if(nums[i].second > nums[i+1].second){
                    double collision_time = (nums[i+1].first - nums[i].first)/(nums[i].second-nums[i+1].second);
                    double collision_pos = nums[i].first + collision_time*nums[i].second;
                    if(collision_time<min_time && collision_pos < d){
                        min_time = collision_time;
                        idx = i;
                    }
                }else{
                    break;
                }
            }
            if(idx == -1){
                got_dest = true;
                t += (d-nums[0].first)/nums[0].second;
            }else{
                t+= min_time;
                vector<dd> new_nums;
                for(int i=0; i<=idx; i++){
                    double walk = min_time*nums[i].second;
                    if(nums[i].first + walk > d){
                        got_dest = true;
                        t += (d-nums[i].first)/nums[i].second;
                        break;
                    }else{
                        new_nums.push_back({nums[i].first+walk, nums[i].second});
                    }
                }
                if (got_dest) {
                    continue;
                }
                new_nums[idx].second = nums[idx+1].second;
                for(int i = idx+2; i<nums.size(); i++){
                    double walk = min_time*nums[i].second;
                    new_nums.push_back({nums[i].first+walk, nums[i].second});
                }
                nums = new_nums;
            }
        }
        double speed = d/t;
        printf("Case #%d: %lf\n", ca++, speed);
    }
    return 0;
}

