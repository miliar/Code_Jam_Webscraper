#include <iostream>
#include <vector>
#include <queue>


typedef long long ll;
using namespace std;
ll adjust(ll num){
    ll tmp = 0;
    ll ten = 1;
    ll last = 9;
    while(num / 10){


        if(num%10 > last)
            break;
        last = num%10;
        tmp = tmp*10 + 9;
        num/=10;
        ten *= 10;
    }
    if(num != 1){
        return (num - 1)*ten + tmp;
    } else{
        return tmp;
    }
}
bool istidy(ll num){
    ll last = 9;
    while(num / 10){
        if(num%10 > last)
            return false;
        last = num%10;
        num/=10;
    }
    return num <= last;
}

int main() {
//    small input
//    freopen("test1.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("Bbig.out","w",stdout);
    int tt;

    cin >> tt;
    int order = 1;
    while(tt-- > 0){
        ll num;
        cin >> num;
        while(!istidy(num)){
            num = adjust(num);
        };
//        if(hasanswer){
            cout<<"Case #"<<(order++)<<": "<<num<<endl;
//        }else{
//            cout<<"Case #"<<(order++)<<": "<<"IMPOSSIBLE"<<endl;
//        }
    }
}