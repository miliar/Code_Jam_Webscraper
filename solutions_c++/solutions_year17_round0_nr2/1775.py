#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

bool check(string num){
    for(int i = 1; i < num.size(); i++){
        if(num[i] < num[i-1]) return false;
    }

    return true;
}

string get(long long n){
    string res;
    while(n != 0){
        res += ((n % 10) + '0');
        n /= 10;
    }

    reverse(res.begin(), res.end());
    return res;
}

long long getNum(string num){
    long long res = 0;
    long long mul = 1;
    for(int i = num.size()-1; i >= 0; i--){
        res += (num[i]-'0') * mul;
        mul *= 10;
    }
    return res;
}

int main(){

    freopen("B-large.in", "r", stdin);
    freopen("output2.txt", "w", stdout);
    int tt;
    cin>>tt;

    for(int ttt = 1; ttt <= tt; ttt++){
        long long n;
        cin>>n;

        string num = get(n);

        string res;
        if(check(num)) res = num;
        else{
            res = "1";
            for(int i = 0; i < num.size(); i++){
                string x = num;
                x[i]--;
                for(int j = i+1; j < num.size(); j++){
                    x[j] = '9';
                }

                if(x[0] == '0') x.erase(0, 1);

                if(check(x)){
                    if(getNum(x) > getNum(res)){
                        res = x;
                    }
                }
            }
        }

        cout<<"Case #"<<ttt<<": "<<res<<endl;

    }

    return 0;
}
