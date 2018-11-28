#include<bits/stdc++.h>
#define inf 0x3f3f3f3f
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define len(x) (int)(x).size()
using namespace std;

long long T, N; 

vector<unsigned long long>tidy_nums;

void generate(unsigned long long start){
    #define MAXN (unsigned long long)1e18
    for(int i = 1;i < 10;i++){
        long long last_st = start %10;
        if(i >= last_st && start*10+i < MAXN){
            tidy_nums.pb(start*10+i);
            generate(start*10 + i);
        }
    }
    #undef MAXN
}

int main(){
    cin >> T;
    generate(0);
    sort(all(tidy_nums));
    for(int t = 1; t <= T;t++){
        cin >> N;
        vector<unsigned long long>::iterator pos = lower_bound(all(tidy_nums), N);
        int ans1 = pos - tidy_nums.begin();
        int ans2 = --pos - tidy_nums.begin();
        if(tidy_nums[ans1] == N) {
            cout << "Case #" << t << ": " << tidy_nums[ans1] << endl;
        }else{
            cout << "Case #" << t << ": " << tidy_nums[ans2] << endl;
        }
    }
    return 0;
}
