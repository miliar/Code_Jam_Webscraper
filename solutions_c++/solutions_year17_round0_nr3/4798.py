#include<bits/stdc++.h>
#include<fstream>
using namespace std;

typedef long long int ll;

ll maximum(ll a , ll b){
    if(a>b){
        return a;
    }
    return b;
}

int main(){
    ll t;
    ifstream f ;
    f.open("C-small-2-attempt0.in");
    ofstream out ;
    out.open("out.txt");
    f >> t;
    ll a=1;
    while(a<=t){
        ll n;
        f >> n;
        ll k;
        f >> k;
        ll i = 0;
        queue<ll> q;
        ll val;
        q.push(n);
        while(i<k){
            val = q.front();
            q.pop();
            ll ct=1;
            ll flag=0;
            while(!q.empty() && flag==0 && i<k){
                if(val == q.front() && val%2==0){
                    ct++;
                    i++;
                    q.pop();
                }
                else{
                    flag=1;
                }
            }
            if(val%2==0){
                ll c=0;
                while(c<ct){
                    q.push(val/2);
                    c++;
                }
                c=0;
                while(c<ct){
                    q.push(maximum(0, val/2 - 1));
                    c++;
                }
            }
            else{
                q.push(val/2);
                q.push(val/2);
            }
            i++;
        }
        ll mx, mn;
        if(val%2==0){
            mx = val/2;
            mn = maximum(0, val/2 - 1);
        }
        else{
            mx = val/2;
            mn = val/2;
        }
        out << "Case #" << a << ": ";
        out << mx << " " << mn << endl;
        a++;
    }
    f.close();
    out.close();
}

