#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
const double PI = acos(-1.0);
const double e = exp(1.0);
#define ll __int64
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
#define inf 0x7fffffff
using namespace std;
/*
24*60分钟


每个人负责720
n m:
n、m行 忙碌时间段




 */

struct node  {
    int st, ed;
    bool operator <(node x){
    	return st<x.st;
    }
} a[10], b[10];

int main() {
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int n, m;
    for (int cas = 1; cas <= t; cas++) {
        printf("Case #%d: ", cas);
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &a[i].st, &a[i].ed);
        }
        for (int i = 0; i < m; i++) {
            scanf("%d%d", &b[i].st, &b[i].ed);
        }
        sort(a, a + n);
        sort(b, b + m);
        if (n == 0 && m == 0) {
            printf("2\n");
        } else if (n == 0 && m == 1) {
            printf("2\n");
        } else if (n == 0 && m == 2) {
            if ((b[1].ed - b[0].st <= 720)
                    || (1440 - b[1].st + b[0].ed <= 720)) {
                printf("2\n");
            } else
                printf("4\n");
        } else if (n == 1 && m == 0) {
            printf("2\n");
        } else if (n == 1 && m == 1) {
            printf("2\n");
        } else if (n == 1 && m == 2) {
            if (a[0].ed <= b[0].st) {
                if (b[1].ed - b[0].st <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            } else if (a[0].ed <= b[1].st) {
                if (1440 - b[1].st + b[0].st <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            } else {
                if (b[1].ed - b[0].st <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            }
        } else if (n == 2 && m == 0) {
            if ((a[1].ed - a[0].st <= 720)
                    || (1440 - a[1].st + a[0].ed <= 720)) {
                printf("2\n");
            } else
                printf("4\n");
        } else if (n == 2 && m == 1) {
            if (b[0].ed <= a[0].st) {
                if (a[1].ed - a[0].st <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            } else if (b[0].ed <= a[1].st) {
                if (1440 - a[1].st + a[0].st <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            } else {
                if (a[1].ed - a[0].st <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            }
        } else if (n == 2 && m == 2) {
            if (b[1].ed <= a[0].st || a[1].ed <= b[0].st) {
                if (a[1].ed - a[0].st <= 720 && b[1].ed - b[0].st <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            } else if (a[0].ed <= b[0].st && b[0].ed <= a[1].st
                    && a[1].ed <= b[1].st) {
                printf("4\n");
            } else if (b[0].ed <= a[0].st && a[0].ed <= b[1].st
                    && b[1].ed <= a[1].st) {
                printf("4\n");
            } else if (a[1].st >= b[1].ed) {
                if (b[1].ed - b[0].st <= 720 && 1440 - a[1].st + a[0].ed <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            } else {
                if (a[1].ed - a[0].st <= 720 && 1440 - b[1].st + b[0].ed <= 720)
                    printf("2\n");
                else
                    printf("4\n");
            }
        }
    }
    return 0;
}

