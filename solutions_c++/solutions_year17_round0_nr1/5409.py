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

void flip(string &str, int k, int pos){
    for(int i = pos; i < pos + k;i++){
        if(str[i] == '-') str[i] = '+';
        else str[i] = '-';
    }
}

int main(){
    int T;
    cin>>T;
    for(int t=0;t<T;t++){
        string str;
        int k;
        cin>>str>>k;
        int count = 0;
        for(int pos = 0; pos < str.length() - k + 1;){
            if(str[pos] == '-'){
                flip(str, k, pos);
                count++;
            }
            else pos++;
        }
        bool flag = 1;
        for(int i=0;i<str.length();i++){
            if(str[i] == '-'){
                flag = 0;
                break;
            }
        }
        if(flag) cout<<"Case #"<<t + 1<<": "<<count<<endl;
        else cout<<"Case #"<<t + 1<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}