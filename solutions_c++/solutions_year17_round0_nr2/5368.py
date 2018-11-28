#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

typedef long long ll;

bool is_tidy(ll n) {
   char num[20];
   sprintf(num, "%lld", n);
   int s = strlen(num);
   int x = num[0]-'0';
   for(int i=1;i<s;i++) {
       int y=num[i]-'0';
       if(y<x) return false;
       x = y;
   }
   return true;
}


ll solve(ll n) {
    char num[20];
    char out[20];
    sprintf(num, "%lld", n);
    int len = strlen(num);
    strcpy(out, num);
    
    int i=len;
    //cerr << "len:" << i << endl;
    while(--i) {
        char cd = out[i];
        //cerr << "i:" << i << " cd:" << cd;
        if(i>0) {
            char nd = out[i-1];
            //cerr << " nd:" << nd;
            if(nd > cd) {
                for(int z=i;z<len;z++) 
                    out[z] = '9';
                if(out[i-1] != '0') 
                    out[i-1]--;
            }
        } 
        //cerr << " out:" << out << endl;
    }

    return strtoll(out, NULL, 10);
}


int main() {
    ll T;
    cin >> T;
    for(ll i=0;i<T;i++) {
        ll N;
        cin >> N;
        ll ans = solve(N);
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
}
