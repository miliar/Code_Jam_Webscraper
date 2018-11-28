/* Bismillahir Rahmanir Rahim */

#include <bits/stdc++.h>

#define rep(i, n)	for(int i=0;i<n;i++)
#define repn(i, n)	for(int i=1;i<=n;i++)
#define set(i, n)	memset(i, n, sizeof(i))

#define pb	push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

bool ok(long long val){
    vector<int>dig;
    while(val){
        dig.pb(val % 10);
        val /= 10;
    }
    reverse(dig.begin(), dig.end());
    for(int i=1;i<dig.size();i++){
        if(dig[i] < dig[i-1]) return false;
    }
    return true;
}

long long brute(long long n){
    int ret = 1;
    repn(i, n){
        if(ok(i)) ret = i;
    }
    return ret;
}

int main(){
    int tc, k, cas=1;
    string str;
    scanf("%d", &tc);
    while(tc--){
        long long n;
        scanf("%lld", &n);
        vector<int>digits;
        while(n){
            digits.pb(n % 10LL);
            n /= 10LL;
        }
        reverse(digits.begin(), digits.end());
        long long ret = 0;
        for(int i=0;i<digits.size();i++){
            int flag = 0;
            for(int j=i+1;j<digits.size();j++){
                if(digits[j] > digits[i]) break;
                if(digits[j] < digits[i]){
                    flag = 1;
                }
            }
            if(flag){
                ret *= 10LL;
                ret += digits[i] - 1;
                for(int j=i+1;j<digits.size();j++){
                    ret *= 10LL;
                    ret += 9;
                }
                break;
            }
            else{
                ret *= 10LL;
                ret += digits[i];
            }
        }
        printf("Case #%d: %lld\n", cas++, ret);
    }
	return 0;
}

