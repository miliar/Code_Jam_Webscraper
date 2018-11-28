//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<int(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


int extra() {
    vi den = vi(24*60, 0);
    vi useky[3];
    vi P = {0,0,0};
    int dvojpoc = 0, dvojsuc = 0;
    int A,B,a,b;

    scanf("%d%d", &A, &B);
    For(i, A) {
        scanf("%d%d", &a, &b);
        for(int j = a; j < b; ++j) den[j] = 1;
    }
    For(i, B) {
        scanf("%d%d", &a, &b);
        for(int j = a; j < b; ++j) den[j] = 2;
    }
    int pred = 0;
    int dlzka = 0;
    For(i, 24*60) {
        if (den[i]) {
            pred = den[i];
            dlzka = 0;
        } else dlzka++;
    }
    For(i, 24*60) {
        P[den[i]]++;
        if (den[i]) {
            if (pred == den[i] && dlzka) {
                useky[den[i]].push_back(dlzka);
            }
            if (pred != den[i]) {
                dvojpoc++;
                dvojsuc+=dlzka;
            }
            pred = den[i];
            dlzka = 0;
        } else dlzka++; 
    }
    if (P[1] > P[2]) {
        swap(P[1],P[2]);
        swap(useky[1],useky[2]);
    }
    sort(useky[2].begin(), useky[2].end());
    reverse(useky[2].begin(), useky[2].end());
    int pos = 0;
    while(P[1] + dvojsuc < 12*60) {
        P[1]+=useky[2][pos];
        pos++;
        dvojpoc+=2;
    }
    printf("%d\n", dvojpoc);
}

int main() {
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
