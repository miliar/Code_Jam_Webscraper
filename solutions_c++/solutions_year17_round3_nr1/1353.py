#include <bits/stdc++.h>
using namespace std;

#define sz(v)        ((int)v.size())
#define ll           long long
#define all(v)       (v.begin()) , (v.end())
#define rall(v)      (v.rbegin()) , (v.rend())
#define SetTo(v, a)  memset(v,a,sizeof(v))

const double Pi = acos(-1);
pair <int,int> arr[1005];

int n, k;

int main ()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int tc, a, b;
    scanf("%d", &tc);
    for(int test = 1;test <= tc;test++)
    {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &k);
        for(int i=0;i<n;i++){
            scanf("%d%d", &a, &b);
            arr[i] = make_pair(a, b);
        }
        sort(arr, arr + n);
        reverse(arr, arr + n);

        long double ans = 0;

        for(int i=0;i<=n-k;i++){
            long double tmp = Pi*arr[i].first * arr[i].first + 2*Pi*arr[i].first*arr[i].second;
            vector <long double> V;
            for(int j=i+1;j<n;j++){
                V.push_back(2*Pi*arr[j].first*arr[j].second);
            }
            sort(rall(V));
            for(int j=0;j<k-1;j++){
                tmp += V[j];
            }
            ans = max(ans, tmp);
        }
        cout << fixed << setprecision(10) << ans << endl;
    }
    return 0;
}
