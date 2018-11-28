#include<bits/stdc++.h>
using namespace std;

long long N;
vector<int> d, a;

void main2(int tc) {
    scanf("%lld", &N);
    d.clear();
    a.clear();
    while(N) {
        d.push_back(N % 10);
        N /= 10;
    }
    reverse(d.begin(), d.end());

    for(int i = 0; i < d.size(); i++) {
        bool o = true;
        for(int j = i; j < d.size(); j++) {
            if(d[i] < d[j]) break;
            if(d[i] > d[j]) {
                o = false;
                break;
            }
        }
        if(!o) {
            a.push_back(d[i] - 1);
            for(int j = i + 1; j < d.size(); j++) a.push_back(9);
            break;
        }
        a.push_back(d[i]);
    }
    printf("Case #%d: ", tc);
    bool l = true;
    for(int i = 0; i < a.size(); i++) {
        if(a[i] != 0) l = false;
        if(a[i] == 0 && l) continue;
        printf("%d", a[i]);
    }
    printf("\n");
}

int TC;
int main() {
    freopen("inputB.txt", "r", stdin);
    freopen("outputB.txt", "w", stdout);
    scanf("%d", &TC);
    for(int i = 1; i <= TC; i++) main2(i);
}
