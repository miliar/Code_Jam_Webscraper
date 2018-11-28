#include <bits/stdtr1c++.h>

#define time lol
#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("out.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl
#define ran(a, b) ((((rand() << 15) ^ rand()) % ((b) - (a) + 1)) + (a))

using namespace std;

int n;
long double time[1010];
long long d, dis[1010], speed[1010];

bool check(long double v){
    long double t = (long double)d / v;

//    for (int i = 0; i < n; i++){
//        if (v > speed[i]){
//            long double x = (long double)(dis[i]) / (long double)abs(v - speed[i]);
//            long double y = (long double)(d - dis[i]) / (long double)speed[i];
//
//            if (x < t && x < y){
//                long double p1 = x * v;
//                long double p2 = dis[i] + x * speed[i];
//                if (p1 > p2) return false;
//            }
//        }
//    }
//    return true;


    for (int i = 0; i <= 10000; i++){
        long double x = t / i;
        long double p1 = x * v;
        for (int j = 0; j < n; j++){
            long double p2 = dis[j] + x * speed[j];
            if (p1 > p2) return false;
        }
    }
    return true;
}

int main(){
    read();
    write();
    int T = 0, t, i, j, k;
    unsigned long long h = 0;

    scanf("%d", &t);
    while (t--){
        scanf("%lld %d", &d, &n);
        for (i = 0; i < n; i++) scanf("%lld %lld", &dis[i], &speed[i]);

//        n = 1000, d = ran(2, 10);
//        for (i = 0; i < n; i++) dis[i] = ran(1, d - 1);
//        for (i = 0; i < n; i++) speed[i] = ran(1, 10000);


        vector <pair<long long, long long>> v;
        for (i = 0; i < n; i++) v.push_back(make_pair(dis[i], speed[i]));
        sort(v.begin(), v.end());
        for (i = 0; i < n; i++) dis[i] = v[i].first, speed[i] = v[i].second;

//        for (i = 0; i < n; i++){
//            time[i] = 1e100;
//            if ((i > 0 && dis[i] == dis[i - 1] && speed[i] > speed[i - 1])){
//                time[i] = 0.0;
//                continue;
//            }
//            if (((i + 1) < n && dis[i] == dis[i + 1] && speed[i] > speed[i + 1])){
//                time[i] = 0.0;
//                continue;
//            }
//
//            for (j = i + 1; j < n; j++){
//                if (speed[i] > speed[j] && dis[i] != dis[j]){
//                    time[i] = (long double)abs(dis[i] - dis[j]) / (long double)abs(speed[i] - speed[j]);
//                }
//            }
//        }

        long double low = 0.0, high = 1e18;
        for (i = 0; i < 500; i++){
            long double mid = (low + high) / 2.0;
            if (check(mid)) low = mid;
            else high = mid;
        }

        fprintf(stderr, "Case #%d: %0.12f\n", T + 1, (double)low + 1e-15);
        printf("Case #%d: %0.12f\n", ++T, (double)low + 1e-15);
        h = h * 666666667 + floor(low + 0.5);
    }

    fprintf(stderr, "hash = %llu\n", h);
    return 0;
}

/***

4
1000000000 1
999999999 10000
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10

***/
