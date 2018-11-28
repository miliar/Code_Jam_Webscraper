#include <iostream>
#include<bits/stdc++.h>
using namespace std;
// ya rab

double arr[55],temp[55];
int n,m;
double u;
int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    cin>>t;
    for(int k =  1 ; k<=t ; k++)
    {
        cin>>n>>m>>u;
        for(int i = 0 ; i<n ; i++) cin>>arr[i];
        sort(arr, arr+n);
        reverse(arr, arr+n);
        double sum = 0;
        for(int i = 0 ; i<m ; i++) temp[i] = arr[i] , sum+=1-arr[i];
        if(m==1) temp[0] = min(1.0 , temp[0] + u);
        else if(u>=sum)
        {
            for(int i = 0 ; i<m ; i++) temp[i] = 1;
        }
        else
        {
            while(1)
            {
                sort(temp , temp + m);
                if(temp[0]==1) break;
                double sum = temp[1] - temp[0]+0.0001;
                if(sum>=u) {temp[0]+=u; break;}
                temp[0]+=sum;
                u-=sum;
            }
        }
        double ans = 1;
        for(int i = 0 ; i<m ; i++) ans*=temp[i];
        printf("Case #%d: %.9f\n" , k , ans);
    }
    return 0;
}
