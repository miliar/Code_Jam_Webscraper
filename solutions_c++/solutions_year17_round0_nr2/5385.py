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

vector<int> conv(ll num){
    vector<int> temp;
    while(num){
        temp.push_back(num%10);
        num /= 10;
    }
    reverse(temp.begin(), temp.end());
    return temp;
}

int chk(vector<int> &arr){
    if(arr.size() == 1) return -1;
    for(int i=1;i<arr.size();i++){
        if(arr[i] < arr[i - 1]) return (i - 1);
    }
    return -1;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=0;t<T;t++){
        ll num;
        scanf("%lld", &num);
        vector<int> arr = conv(num);
        while(1){
            int pos = chk(arr);
            if(pos < 0) break;
            arr[pos]--;
            while(pos < arr.size()) arr[++pos] = 9;
        }
        printf("Case #%d: ", t + 1);
        bool start = false;
        for(int i=0;i<arr.size();i++){
            if(arr[i] == 0 && !start) continue;
            printf("%d", arr[i]);
            start = true;
        }
        printf("\n");
    }
    return 0;
}