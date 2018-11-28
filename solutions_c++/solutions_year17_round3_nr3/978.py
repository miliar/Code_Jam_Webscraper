#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm>
#include <cstring>
#include <map>
#include <queue>
#include <cmath>
#define PI 3.14159265359
using namespace std;

vector<double> vt;

int main(void)
{

    freopen("C-small-1-attempt1.in", "r", stdin);
    freopen("CSoutput.txt", "w", stdout);


    int t;
    cin >> t;

    int n, k;
    double so;
    for(int i=1;i<=t;i++){
        cin >> n >> k;
        cin >> so;
        vt.clear();
        vt.push_back(0);
        double a;
        for(int j=0;j<n;j++){
            cin >> a;
            vt.push_back(a);
        }

        sort(vt.begin(),vt.end());
        vt.push_back(1.0);
        for(int j=1; j<=n;j++){
            double diff = vt[j+1] - vt[j];

            if(diff*j <= so){
                for(int k=1;k<=j;k++) vt[k] = vt[j+1];
                so -= diff*j;
            }else{
                for(int k=1;k<=j;k++) vt[k] += so/j;
                so = 0;
                break;
            }
        }
        double ans = 1;
        for(int j=1;j<=n;j++) {
                ans *= vt[j];
        }
        printf("Case #%d: %0.9f\n", i, ans);
    }

    return 0;
}
