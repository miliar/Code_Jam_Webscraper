// In the name of Allah the Most Merciful.

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

bool is_it(ll a)
{
    int temp = 9;

    while(a!=0){

        if(a%10>temp)return false;

        temp = a%10;
        a/=10;
    }

    return true;
}

int main(void)
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int i=0;i<t;i++){

        ll a;
        cin >> a;

        while(is_it(a)!=true)a--;

        printf("Case #%d: %lld\n",i+1 , a);

    }
    return 0;
}
