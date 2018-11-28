#include<bits/stdc++.h>

#define INF 9223372036854775807
#define mod 1000000007
#define ll  long long int
#define ld double
#define endl '\n'
#define sz 202
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

using namespace std;

ll n,k,power,bada,num,inner_nodes;

ll get_pow(){
    ll cur = 1,sum = 0;
    ll temp = 0;
    while(true){
        sum += cur;
        if(sum >= k)
            break;
        temp++;
        cur*= 2;
    }
    num = cur;
    inner_nodes = cur/2 -1;
    return temp;
}

ll get_bada(){
    ll temp = n,div;
    for(ll i = 0; i < power; i++){
    //    cout<<"yeee "<<temp<<' ';
        temp--;
        div = temp/2;
        temp = temp - div;
        temp = max(div,temp);
    }
   // cout<<temp<<endl;
    return temp;
}

ll predicate(ll used, ll x){
    return x*used + (x-1)*(num-used);
}


ll bin(ll x,ll lo, ll hi){
    ll mid,temp;
    while(lo <= hi){
        mid = (lo + hi)/2;
        temp = predicate(mid,bada);
        if(temp == n-(num -1))
            return mid;
        else if(temp < n-(num -1))
            lo = mid+1;
        else
            hi = mid-1;
    }
}


int main(){
    ll i,j,t,seq,a,b;
    fast();
    cin>>t;
    for(ll times = 1; times <= t; times++){
        cin>>n>>k;
        power = get_pow();      //power is the height of last level
        bada = get_bada();      //bada holds bigger of those two integers in that level
                                //num holds elements in the current level
        seq = bin(bada,0,num);  //seq holds the number of larger numbers in the last level
        k = k - (num - 1);       //remaining slots to be filled

       // cout<<power<<' '<<bada<<' '<<seq<<' '<<k<<endl;

        if(k <= seq){
            bada--;
            a = bada/2;
            b = bada - a;
        }
        else{
            bada -= 2;
            a = bada/2;
            b = bada -a;
        }
        cout<<"Case #"<<times<<": "<<max(a,b)<<' '<<min(a,b)<<endl;
    }
    return 0;
}
