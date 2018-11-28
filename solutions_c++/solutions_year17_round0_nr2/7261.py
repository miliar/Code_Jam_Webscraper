#include <bits/stdc++.h>
#define endl '\n'

using namespace std;


int tests,current_case;
unsigned long long n,len,pw[128],pw10[128];

void message(int current_case) {
    //cerr<<"Case "<<current_case<<" solved!"<<endl;
    fprintf(stderr, "Case %d solved!\n", current_case);
}

unsigned long long count_digits(long long a) {
    unsigned long long ans=0;
    while(a) a/=10,++ans;
    return ans;
}

void solve(unsigned long long pos, unsigned long long last, unsigned long long curr) {
    if(pos>len) {
        printf("%llu\n", curr);
        return;
    }
    unsigned long long i;
    for(i=9;i>=last;i--) {
        if(curr*pw10[len-pos+1]+pw[len-pos+1]*i<=n) {
            solve(pos+1,i,curr*10+i);
            break;
        }
    }
}

int main() {
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    int i;

    pw[1]=1;
    for(i=2;i<=19;i++) pw[i]=pw[i-1]*10+1;
    pw10[0]=1;
    for(i=1;i<=19;i++) pw10[i]=pw10[i-1]*10;

    tests=1;
    scanf("%d", &tests);
    //cin>>tests;
    for(current_case=1;current_case<=tests;current_case++) {
        scanf("%llu", &n);
        len=count_digits(n);
        printf("Case #%d: ", current_case);
        if(pw[len]>n) {
            printf("%llu\n", pw[len-1]*9);
            goto MESSAGE;
        }
        solve(1,1,0);

        MESSAGE:
        message(current_case);
    }

    return 0;
}
