#include <bits/stdc++.h>
#define forn(i,n) for(lli i = 0; i < n; i++)
#define f first
#define s second

using namespace std;

typedef unsigned long long int lli;
typedef pair<lli,lli> plli;

string toBitStr(lli n) {
    string str = "";
    while(n > 0){
        str += n%2 + '0';
        n /= 2;
    }
    reverse(str.begin(), str.end());
    return str;
}

plli solve(lli stalls, lli ppl)
{
    plli ans, buff;

    vector< vector<plli> > v (toBitStr(stalls).size(), vector<plli>());

    buff.f = (stalls-1)/2;
    buff.s = stalls/2;
    v[0].push_back(buff);
    // printf("(%lld, %lld)\n", buff.f, buff.s);

    for(uint i = 1; i < v.size(); i++) {
        for(uint j = 0; j < v[i-1].size(); j++){

            if(v[i-1][j].f > 0) buff.f = (v[i-1][j].f-1)/2;
            else buff.f = 0;
            buff.s = v[i-1][j].f/2;
            v[i].push_back(buff);

            // printf("(%lld, %lld)", buff.f, buff.s);

            if(v[i-1][j].s > 0) buff.f = (v[i-1][j].s-1)/2;
            else buff.f = 0;
            buff.s = v[i-1][j].s/2;
            v[i].push_back(buff);

            // printf("(%lld, %lld) ", buff.f, buff.s);
        }
        sort(v[i].rbegin(), v[i].rend());
        // printf("\n");
    }
    lli b2 = 0;
    int p = 0;
    for(lli i = 1; i <= ppl; i*=2) {
        p++;
        b2 = i;
    }
    // ?\cout << "b2: " << b2 << " p: " << p << endl;

    // for(uint i = 0; i < v[p-1].size(); i++) {
    //     printf("(%lld, %lld) ", v[p-1][i].f, v[p-1][i].s);
    // }

    ans = v[p-1][ppl-b2];


    return ans;
}

int main()
{

    lli t, stalls, ppl;
    plli maxmin;
    cin >> t;
    forn(tt, t) {
        cin >> stalls >> ppl;
        maxmin = solve(stalls, ppl);
        printf("Case #%lld: %lld %lld\n", tt+1, maxmin.s, maxmin.f);
    }
    return 0;
}
