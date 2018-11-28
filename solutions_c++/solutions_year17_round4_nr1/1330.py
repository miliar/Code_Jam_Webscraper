#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;



int main() {
    freopen("Documents/Informatics/GoogleCodeJam/in.txt", "r", stdin);
    freopen("Documents/Informatics/GoogleCodeJam/freshchocolate.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int cas = 1; cas <= tc; cas++) {
        int n, p;
        int arr[4] = {0};
        scanf("%d %d", &n, &p);
        int in;
        for (int i = 0; i < n; i++) {
            scanf("%d", &in);
            arr[in%p]++;
        }
        int ans = arr[0];
        arr[0] = 0;
        if (p == 3) {
            int temp = min(arr[1], arr[2]);
            ans += temp;
            arr[1] -= temp;
            arr[2] -= temp;
            while (arr[1] > p-1) {
                arr[1] -= p;
                ans++;
            }
            while (arr[2] > p-1) {
                arr[2] -= p;
                ans++;
            }
        }
        else if (p == 2) {
            ans += arr[1]/2;
            arr[1] -= 2*(arr[1]/2);
        }
        else if (p == 4) {
            int temp = min(arr[1], arr[3]);
            ans += temp;
            arr[1] -= temp;
            arr[3] -= temp;
            ans += arr[2]/2;
            arr[2] -= 2*(arr[2]/2);
            while (arr[1] >= p) {
                if (arr[2] > 0) {
                    arr[2]--;
                    arr[1]-=2;
                    ans++;
                }
                else {
                    arr[1] -= p;
                    ans++;
                }
            }
            while (arr[3] >= p) {
                if (arr[2] > 0) {
                    arr[2]--;
                    arr[3]-=2;
                    ans++;
                }
                else {
                    arr[3] -= p;
                    ans++;
                }
            }
        }
        for (int i = 0; i < p; i++) {
            if (arr[i] > 0) {
                ans++;
                break;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
