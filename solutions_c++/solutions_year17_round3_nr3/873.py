#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

struct core{
    double base, add;
    bool operator<(const core &r)const{
        return base > r.base;
    }
};

int main(){
    int T, N, K;
    scanf("%d\n", &T);

    int t = 1;
    while(t < T+1){
        double unit;
        std::vector<core> arr;
        std::vector<std::pair<double, int> > diffvalues;
        scanf("%d %d %lf", &N, &K, &unit);
        arr.resize(N);
        for(int i = 0; i < N; i++)
            scanf("%lf ", &arr[i].base);
        std::sort(arr.begin(), arr.end());
        double maxv = arr[0].base;
        double pre = -1;
        for(int i =K-1; i >=0 ;i--){//add max k units
            if(pre == arr[i].base)
                diffvalues[diffvalues.size()-1].second+=1;
            else
                diffvalues.push_back(std::pair<double, int> (arr[i].base, 1));
        }
        if(arr[0].base != 1.0)
            diffvalues.push_back(std::pair<double, int>(1, 0));

        for(int i = 0; i < diffvalues.size()-1; i++){
            double& value = diffvalues[i].first;
            int& count = diffvalues[i].second;
            double nextvalue = diffvalues[i+1].first;
            if((nextvalue-value)*count > unit){//unit end
                value+=unit/count;
                unit = 0;
            } else {
                unit -= (nextvalue-value)*count;
                diffvalues[i+1].second += count;
                count = 0;
            }
        }
        /*if(unit > 0){//still avail
            if(diffvalues[diffvalues.size()-1].first != 1.0)

            }*/
        double prob = 1;
        for(int i = 0; i < diffvalues.size()-1; i++){
            for(int j = 0; j < diffvalues[i].second; j++)
                prob *= diffvalues[i].first;
        }
        printf("Case #%d: %lf\n", t, prob);
        t++;
    }
}
