//bismillahir rahmanir raheem

#include <string>
#include <vector>
#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<math.h>
#include<string.h>
#include <stdlib.h>
#include<map>
#include<queue>
#include<stack>
#include<utility>
#include<stdlib.h>
#include<string>
#include<set>
#include<iomanip>
#define lld long long int
#define CLR(a) memset(a,0,sizeof(a))
#define RESET(a) memset(a,-1,sizeof(a))
#define act(a) memset(a,1,sizeof(a))
#define setinf(a) memset(a,0b01111111,sizeof(a));
#define FRO freopen("/Users/sheikahm/Contests/General/General/A-large.in","r",stdin);
#define FROF(a) freopen(a,"r",stdin);
#define FROut freopen("/Users/sheikahm/Contests/General/General/big-output.txt","w",stdout);
#define ui unsigned int
#define came "came"
#define pii pair<int,int>
#define plii pair<long long int, int>
#define pll pair<long long,long long>
#define pic pair<int,char>
#define ninf (-1e9)-2
#define inf (1e9)+2
#include<fstream>
#include <assert.h>
#include <bitset>
#include <unordered_map>
#define foreach(x) for(__typeof(x.begin()) it=x.begin(); it!=x.end();it++)

using namespace std;
#define pid pair<int,double>
#define pdi pair<double,int>

#define PB push_back
#define MP make_pair
#define pri(x) printf("%d\n",x)
#define F first
#define S second
#define vit vector<int>::iterator

int vis[2<<10];

char arr[15];

int strToNum(char *arr, int len) {
    int i;
    int num = 0;
    for(i = 0; i<len ; i++) {
        int bit = arr[i] == '+'? 1:0;
        num |= (bit<<i);
    }
    return num;
}

int flipBits(int startRange, int endingRange, int num) {
    
    int alter = ~(num & (((1<<(endingRange - startRange + 1)) - 1) <<startRange));
    int cut = num | (((1<<(endingRange - startRange + 1)) - 1) <<startRange);
    return cut & alter;
}

int bfs(int start, int k, int len) {
    int target = (1<<len) - 1;
    int i,j;
    queue<int> q;
    q.push(start);
    
    for(i = 0; i <=target; i++) {
        vis[i] = 1e9;
    }
    vis[start] = 0;
    
    if(start == target) {
        return 0;
    }
    
    while(!q.empty()) {
        int num = q.front();
        q.pop();
        for(i=0; i<= (len - k); i++) {
            int val = flipBits(i, i + k - 1, num);
            if(vis[val] > vis[num] + 1) {
                vis[val] = vis[num] + 1;
                if(val == target) {
                    return vis[val];
                }
                q.push(val);
            }
        }
    }
    return -1;
}

int calc(char *arr, int k) {
    int len = (int) strlen(arr);
    int num = strToNum(arr, len);
    int value = bfs(num, k, len);
    return value;
}

int bigCalc(char * arr, int k) {
    int len = (int) strlen(arr);
    int i,j;
    int count = 0;
    for(i = len - 1; i >= k - 1; i--) {
        if(arr[i] == '+') {
            continue;
        } else {
            count++;
            for(j = i; j>= i-k+1; j--) {
                arr[j] = arr[j] == '+'? '-': '+';
            }
        }
    }
    for(i = 0; i < k-1; i++) {
        if(arr[i] == '-') {
            return -1;
        }
    }
    return count;
}

int main() {
    FRO
    FROut
    int t, ca;
    scanf("%d",&t);
    for(ca = 1; ca <= t; ca++) {
        int k;
        scanf("%s %d", arr, &k);
        printf("Case #%d: ", ca);
        int value = bigCalc(arr, k);
        if (value == -1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", value);
        }
    }
    return 0;
}
