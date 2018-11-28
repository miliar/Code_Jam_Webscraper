#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    std::ios::sync_with_stdio(false);
    cin.tie(0);
    pair<long long,long long> nums[10];
    int cnt = 1;

    int t;
    cin>>t;
    long long n, k;
    for(int cc = 1; cc <= t; ++cc){
        cin>>n>>k;
        cnt = 1;

        nums[1] = make_pair(n, 1);
        pair<long long,long long> temp[10];
        bool found = false;
        long long res1 = 0, res2 = 0, res;
        while(1){
            long long ttt = cnt * 2;
            long long say = 0;
            for(int i = cnt; i > 0; --i){
                long long l, r;
                //cout<<"->> "<<nums[i].first<<" "<<nums[i].second<<endl;
                if(k <= nums[i].second){
                    found = true;
                    res = nums[i].first;
                    if(res % 2 == 0){
                        res1 = res / 2;
                        res2 = res / 2 - 1;
                    } else{
                        res1 = res2 = res / 2;
                    }
                    break;
                }
                if(found == true)
                    break;
                k -= nums[i].second;
                if(nums[i].first % 2 == 0){
                    temp[++say].first = nums[i].first / 2 - 1;
                    temp[say].second = nums[i].second;
                    temp[++say].first = nums[i].first / 2;
                    temp[say].second = nums[i].second;
                } else{
                    temp[++say].first = nums[i].first / 2;
                    temp[say].second = nums[i].second;
                    temp[++say].first = nums[i].first / 2;
                    temp[say].second = nums[i].second;
                }
            }
            //for(int i = 1; i <= ttt; ++i){
            //    cout<<"->> "<<temp[i].first<<" "<<temp[i].second<<" <<-"<<endl;
           // }
            if(found == true)
                break;
            int cur = 1;
            sort(temp + 1, temp + 1 + ttt);
            for(int i = 2; i <= ttt; ++i){
                if(temp[i].first == temp[cur].first)
                    temp[cur].second += temp[i].second;
                else{
                    cur++;
                    temp[cur] = temp[i];
                }
            }
            for(int i = 1; i <= cur; ++i)
                nums[i] = temp[i];

            cnt = cur;
        }
        cout<<"Case #"<<cc<<": "<<res1<<" "<<res2<<endl;


    }

    return 0;
}
