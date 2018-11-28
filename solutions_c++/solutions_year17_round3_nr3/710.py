#include<bits/stdc++.h>

#define INF 9223372036854775807
#define mod 1000000007
#define ep 0.000000001
#define ll  long long int
#define ld double
#define endl '\n'
#define sz 2005
#define pi 3.141592653589
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

using namespace std;

ld arr[sz],u;
ll n,k;


bool predicate(ld mid){
    ll i,j;
    ld temp = 0;
    for(i = 0; i <n ;i++){
        temp += max(0.00,mid - arr[i]);
    }
    return u - temp >= ep;
}

ld bin(){
    ld low,high,mid;
    ll i,j;
    low = 0.0;
    high = 1.1;
    for(i = 0; i < 1000; i++){
        mid = low + (high - low)/2;
        if(predicate(mid))
            low = mid;
        else
            high = mid;
    }
    ld ans = 1.000;
    for(i = 0; i < n; i++){
        ans *= max(arr[i],mid);
    }
    return ans;
}

int main(){
    ll i,j,t;
    scanf("%lld",&t);
    for(j = 1; j <= t; j++){
        scanf("%lld%lld%lf",&n,&k,&u);
        for(i = 0; i < n ;i++){
            scanf("%lf",&arr[i]);
        }
        sort(arr,arr+n);
        //cout<<"Case #"<<j<<": ";
        //cout<<bin()<<endl;
        ld temp = bin();
        printf("Case #%lld: %.8lf\n",j,temp);

    }
    return 0;
}
