#include <bits/stdc++.h>
using namespace std;

const int maxN = 105;
pair<int,int> arr[maxN];

bool comp(pair<int,int> a, pair<int,int> b){
    return a.first<b.first;
}

int main(){
//    freopen("data.txt", "r", stdin);
    freopen("A-small-attempt4.in", "r", stdin);
    freopen("A-small-attempt4.out", "w", stdout);
    int t;
    cin >> t;
    cout << setprecision(10) << fixed;
    for(int i=1; i<=t; i++){
        int d, n;
        cin >> d >> n;
        for(int j=0; j<n; j++){
            int a, b;
            cin >> a >> b;
            arr[j] = {a, b};
        }
        sort(arr, arr+n, comp);
        for(int j=0; j<n-1; j++){
            if(arr[j+1].second>=arr[j].second){
                n = j+1;
                break;
            }
        }
//        double tim = 0;
//        double speed = arr[n-1].second;
//        double pos = arr[n-1].first;
//        for(int j=n-2; j>=0; j--){
//            double x1 = tim*arr[j].second+arr[j].first;
//            if(x1>=pos) continue;
//            double ti = x1-pos;
//            ti /= speed-arr[j].second;
//            if(ti<=tim) continue;
//            tim += ti;
//        }
//        double pos = arr[0].first;
//        double speed = arr[0].second;
//        double tim = 0;
//        for(int j=1; j<n; j++){
//            double x = tim*arr[j].second + arr[j].first;
//            if(pos > x){
//                tim = 0;
//                pos = arr[j].first;
//                speed = arr[j].second;
//            }
//            double ti = pos-x;
//            ti /= arr[j].second-speed;
//            pos = ti*speed + pos;
//            speed = arr[j].second;
//            cout << speed << endl;
//            tim += ti;
//        }
//        cout << pos << " " << speed << endl;
        long double lower = 0;
        long double upper = 1e18;
        long double eps = 0.0000000000000000001l;
        long double ans = 0;
        while(upper-lower>eps){
            long double mid = (lower+upper)/2.0l;
            if(abs(mid-ans)<=eps) break;
            bool f = true;
            for(int j=0; j<n; j++){
                if((long double)(arr[j].second)-mid>eps) continue;
                long double x = arr[j].first;
                x /= mid-arr[j].second;
                if((long double)(d)-x*mid > eps){
                    f = false;
                    break;
                }
            }
            ans = mid;
            if(f){
                lower = mid;
            }else{
                upper = mid;
            }
        }
        cout << "Case #" << i << ": " << lower << endl;
    }
    return 0;
}
