#include<cstdio>
#include<set>
#include<algorithm>
using namespace std;
typedef long long int lli;
typedef long double ld;
struct pancake{
    lli R, H;
};
ld PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823L;
multiset<lli> sidearea;
pancake pancakes[1000];
bool pancakecmp(pancake a, pancake b){
    return a.R < b.R;
}
int main(){
    int numcases; scanf("%d", &numcases);
    for(int ccase = 0; ccase < numcases; ccase++){
        sidearea = multiset<lli>();
        int N, K; scanf("%d%d", &N, &K);
        for(int i = 0; i < N; i++){
            scanf("%lld%lld", &pancakes[i].R, &pancakes[i].H);
        }
        sort(pancakes, pancakes + N, pancakecmp);
        lli sideareasum = 0;
        lli cmax = 0;
        for(int i = 0; i < N; i++){
            lli csidearea = pancakes[i].R * pancakes[i].H;
            sideareasum += csidearea;
            lli carea = 2 * sideareasum + pancakes[i].R * pancakes[i].R;
            if(carea > cmax) cmax = carea;
            sidearea.insert(csidearea);
            if(sidearea.size() > K - 1){
                sideareasum -= *sidearea.begin();
                sidearea.erase(sidearea.begin());
            }
        }
        printf("Case #%d: %.9Lf\n", ccase + 1, ((ld)cmax) * PI);
    }
    return 0;
}
