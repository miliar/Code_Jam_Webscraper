#include<bits/stdc++.h>
using namespace std;
void solve(){
    int d,n;
    scanf("%d %d",&d,&n);
    pair<int,int> arr[n];
    for(int i=0;i<n;i++){
        scanf("%d %d",&arr[i].first,&arr[i].second);
    }
    sort(arr,arr+n);
    reverse(arr,arr+n);
    double t=0;
    for(int i=0;i<n;i++){
        int sp=arr[i].second;
        double dd=d-arr[i].first;
        double tnow=dd/sp;
        t=max(t,tnow);
    }
    printf("%lf\n",d/t);
}
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        printf("Case #%d: ",i+1);
        solve();
    }
}
