#include <bits/stdc++.h>

using namespace std;

int T;
long long x;
map<long long, int> m;

string toString(long long x) {
    if(x == 0)
        return "0";
    string r = "";
    while(x != 0){
        r = char('0' + x%10) + r;
        x /= 10;
    }
    return r;
}

long long solve(long long k) {

    if(m.count(k))
        return m[k];

    string s, s1;

    for(long long j=k;j>=0;j--){
        //printf("%lld\n", j);
        //getchar();

        if(m.count(j)) {
            m[k]=m[j];
            return m[j];
        }

        s = toString(j);
        s1 = s;
        sort(s1.begin(), s1.end());
        //printf("j= %d     s=%s    s1=%s\n", j, s.c_str(), s1.c_str());
        if(s==s1) {
            m[k]=j;
            return j;
        }
    }
    return 0;
}

int main()
{
    freopen("small_input.txt", "r", stdin);
    freopen("small_output.txt", "w+", stdout);

    scanf("%d", &T);
    for(int i=0;i<T;i++) {
        scanf("%lld", &x);
        if(i)
            printf("\n");

        printf("Case #%d: %lld", i+1, solve(x));
    }

    return 0;
}
