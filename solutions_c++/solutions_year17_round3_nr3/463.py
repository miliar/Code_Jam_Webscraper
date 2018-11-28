#include <bits/stdc++.h>
#define ff first
#define ss second
#define pi 3.14159265359
#define EPS 1e-6
using namespace std;
typedef long long ll;

double arr[101];
int main()
{
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("c-small-out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int I = 1 ; I <= t ; I ++){
        int n,k;
        cin >> n >> k;
        double u;
        cin >> u;
        int cnt = 0;
        multiset<double> s;
        for(int i = 0 ; i < n ; i++){
            cin >> arr[i];
            s.insert(arr[i]);
        }
        while(u > EPS){
            vector<double> v;
            double small = *s.begin();
            s.erase(s.begin());
            while(s.size() && fabs(*s.begin() - small) < EPS){
                v.push_back(small);
                s.erase(s.begin());
            }
            double second = -1;
            if(s.size()){
                second = * s.begin();
            }
            if(second < 0 || (second - small) * (1+v.size()) > u ){
                double inc = u / (1+v.size());
                for(int i = 0 ; i < 1 + v.size() ; i++){
                    s.insert(min(small + inc,1.0));
                    u -= inc;
                }
            }else{
                s.insert(second);
                u -= (second - small);
                for(int i = 0 ; i < v.size() ; i ++){
                    s.insert(second);
                    u -= (second - small);
                }
            }
        }
        double ans = 1.0;
        for(auto it : s){
            ans *= it;
        }
        printf("Case #%d: %.9lf\n",I,ans);
    }
    return 0;
}
