#include <iostream>
#include<bits/stdc++.h>
using namespace std;
// ya rab

pair<long long,long long>arr[1100];
int n,m;
double bi = 3.141592653589793;
 pair<double,int>  dp[1100][1100];
pair<double,int> solve(int idx, int rem)
{
    if(rem==0) return {0,1};
    pair<double,int>  & ret = dp[idx][rem];
    if(ret.second!= -1) return ret;
    ret = {0,0};
    for(int i = idx+1 ; i<n ; i++)
    {
       pair<double,int>  x = solve(i , rem-1);
       if(x.second)
        {
            ret.second = 1;
            double sum = x.first + 2*bi*arr[i].second * arr[i].first + bi*(arr[idx].first* arr[idx].first - arr[i].first*arr[i].first);
            if(rem - 1 == 0) sum+= bi * arr[i].first * arr[i].first;
            ret.first = max(ret.first ,sum);
        }
    }
    return ret;
}
int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    cin>>t;
    for(int k =  1 ; k<=t ; k++)
    {

        cin>>n>>m;
        for(int i = 0 ; i<n ; i++) scanf("%lld%lld" , &arr[i].first , &arr[i].second);
        sort(arr, arr+n);
        reverse(arr, arr+n);
        memset(dp , -1 ,sizeof dp);
        double maxi = 0;
        for(int i = 0 ; i<n ; i++)
        {
            double sum = 2*arr[i].second*arr[i].first*bi;
            if(m==1) sum+=arr[i].first*arr[i].first * bi;
            pair<double,int>  x = solve(i , m-1);
            if(x.second)
            {
                maxi = max(maxi , sum + x.first);
            }
        }
        printf("Case #%d: %.9f\n" , k , maxi);
    }
    return 0;
}
