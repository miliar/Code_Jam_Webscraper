#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

typedef long long ll;
int T;
ll n,k;

ll arr[100];

void init()
{
    for (int i = 0 ; i <= 60 ; i ++)
        arr[i] = (1LL << i )-1 ;
}


int main()
{
    init();
    int ca = 1;
    freopen("C-large.in","r",stdin);
    freopen("C-large-out.txt","w",stdout);
    scanf("%d",&T);
    ll t,ls,rs,rem,div;
    while (T--){
    scanf("%I64d%I64d",&n,&k);

    for (int i = 0 ; i <= 59 ; i ++)
        if (k<=arr[i+1])
        {
         //   cout<<"arr[i] = "<<arr[i]<<endl;
            k = k - arr[i];
            rem = (n-arr[i])%(arr[i]+1);
            n = (n-arr[i])/(arr[i]+1);
           // cout<<"now n = "<<n<<endl;
            break;
        }
        if (k<=rem)
            div = n+1;
        else
            div = n;
        //cout<<div <<endl;
        if (div&1)
            ls = div/2,rs = div/2;
        else if (div<=1)
            ls = 0 , rs = 0;
        else
            ls = div/2-1,rs= div/2;


        printf("Case #%d: ",ca++);
        printf("%I64d %I64d\n",rs,ls);
    }

}

