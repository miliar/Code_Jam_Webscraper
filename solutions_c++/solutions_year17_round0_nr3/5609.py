#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<unordered_map>
#include<map>
#include<set>
#include<list>
#include<string>
#include<cctype>
#include<regex>
#include<unordered_set>
#include<cmath>
#include<utility>

using namespace std;

#define INT_MAX 

#define mod 1000000007
#define mod9 1000000009
#define inf 1000000011
#define infll 2000000000000000005LL 
double pi = 3.1415926535897;

typedef long long int ll;
typedef long int l;
typedef long double ld;

int dx[] = {0, 0, -1, 1};
int dy[] = {1, -1, 0, 0};

template<class T>
inline T gcd(T a, T b){ 
    while (b > 0){
        a %= b; 
        swap(a, b); 
    }
    return a; 
}

template<class T>
inline T lcm(T a, T b){
    return a*b / gcd(a, b); 
}

inline bool ispalin(string& str){ 
    int n = str.length(); 
    for (int i = 0; i < n / 2; i++){ 
        if (str[i] != str[n - i - 1]) 
            return false; 
    }
    return true;
}

struct point{
    int x, y;
    point(){}
    point(int x, int y){
        this->x = x;
        this->y = y;
    }
};

// ---------------------------------------------------------------------------------//

int main(){
    int T;
    scanf("%d", &T);
    for(int t=0;t<T;t++){
        ll N, K;
        scanf("%lld %lld", &N, &K);
        multiset<ll> table;
        table.insert(N);
        ll count = K;
        while(count > 1){
            auto temp = --table.end();
            if(*temp & 1){
                table.insert(*temp/2);
                table.insert(*temp/2);
            }
            else{
                table.insert(*temp/2);
                table.insert(*temp/2 - 1);
            }
            table.erase(temp);
            count--;
        }
        auto top = --table.end();
        ll y, z;
        if(*top & 1){
            y = *top/2;
            z = *top/2;
        }
        else{
            y = *top/2;
            z = *top/2 - 1;
            if(z < 0) z = 0;
        }
        printf("Case #%d: %lld %lld\n", t+1, y, z); 
    }
    return 0;
}