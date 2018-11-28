#include <bits/stdc++.h>
using namespace std;

typedef long long int lli;

pair <lli,lli> arr[1000 + 10];

int main(){
    lli test,n,k,temp_l,temp_r,maxi,maxi2,idx,temp_val,temp_val2,cnt;
    scanf("%lld",&test);

    for(lli i_t = 0; i_t < test; i_t++){
        scanf("%lld %lld",&n,&k);
        temp_l = 0;
        temp_r = n-1;
        arr[0].first = arr[0].second = arr[n+1].first = arr[n+1].second = -1;
        for(lli i_n = 1; i_n <= n; i_n++){
            arr[i_n].first = temp_l;
            arr[i_n].second = temp_r;
            temp_l++;
            temp_r--;
        }

        for(lli i_k = 0; i_k < k; i_k++){
            maxi2 = 0;maxi = 0;idx = -1;

            for(lli i_n = 1; i_n <= n; i_n++){
                if(arr[i_n].first != -1 && arr[i_n].second != -1){
                    temp_val = min(arr[i_n].first,arr[i_n].second);
                    temp_val2 = max(arr[i_n].first,arr[i_n].second);
                    if(temp_val > maxi){
                        maxi = temp_val;
                        idx = i_n;
                        maxi2 = temp_val2;
                    }
                    else if(temp_val == maxi){
                        if(maxi2 < temp_val2){
                            maxi2 = temp_val2;
                            idx = i_n;
                        }
                    }
                }
            }


            if(i_k == k - 1){
                printf("Case #%lld: %lld %lld\n",i_t + 1,maxi2,maxi);
            }
            cnt = 0;
            for(lli i_n = idx-1; i_n >= 0; i_n--)
                if(arr[i_n].first != -1 && arr[i_n].second != -1){
                    arr[i_n].second = cnt;
                    cnt++;
                }
                else
                    break;
            cnt = 0;
            for(lli i_n = idx + 1; i_n <= n; i_n++)
                if(arr[i_n].first != -1 && arr[i_n].second != -1){
                    arr[i_n].first = cnt;
                    cnt++;
                }
                else
                    break;

            arr[idx].first = arr[idx].second = -1;
        }
    }
}
