#include<bits/stdc++.h>
using namespace std;
#define x first
#define y second
typedef long long int LL;
double dp[10005];
int main(){
    int t, C=0;
    scanf("%d",&t);
    while(t--){
        double D;
        int n;
        scanf("%lf%d",&D,&n);
        vector<pair<double,double>> arr;
        for(int i=0;i<n;i++){
            double k,s;
            scanf("%lf%lf",&k,&s);
            arr.push_back({k,s});
        }
        sort(arr.begin(),arr.end());
        double pre=D, time=0;
        for(int i=n-1;i>=0;i--){
            if(i==n-1){
                time = (D - arr[i].x) / arr[i].y;
                continue;
            }
            int flag=0;
            for(int j=i+1;j<n;j++){
                if(arr[i].y > arr[j].y){
                    double t=(arr[j].x-arr[i].x)/(arr[i].y-arr[j].y);
                    if(arr[i].x+arr[i].y*t<=D) flag=1;
                }
            }
            if(flag==0){
                time = (D - arr[i].x) / arr[i].y;
            }
        }
        printf("Case #%d: %.6f\n",++C, D / time);
    }
}
