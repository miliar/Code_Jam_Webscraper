#include <bits/stdc++.h>
using namespace std;

void preprocess() {
}

void process_testcase(const int testcase, const int should_run) {
    int n, r, o, y, g, b, wtf;
    cin>>n>>r>>o>>y>>g>>b>>wtf;
    int orir = r, oriy = y, orib = b;

    // r, y, b
    int v[3];
    v[0] = r;
    v[1] = y;
    v[2] = b;
    char c[3];
    c[0] = 'R';
    c[1] = 'Y';
    c[2] = 'B';
    if (should_run) {
        string ans = "";
        int common = 0;
        if (v[1] >= v[0] && v[1] >= v[2])
            common = 1;
        if (v[2] >= v[0] && v[2] >= v[1])
            common = 2;
        int rarest = 0;
        if (v[1] <= v[0] && v[1] <= v[2] && common != 1)
            rarest = 1;
        if (v[2] <= v[0] && v[2] <= v[1] && common != 2)
            rarest = 2;
        int middle = 0;
        for (int i = 0; i < 3; ++i)
            if (i != common && i != rarest)
                middle = i;
        //printf("rarest = %d\n", rarest);
        string str;
        while (v[rarest] > 0) {
            str.push_back(c[common]);
            str.push_back(c[middle]);
            str.push_back(c[rarest]);
            --v[0];
            --v[1];
            --v[2];
        }
        int x = common;
        int y = middle;
        while (v[y] > 0) {
            str.push_back(c[x]);
            str.push_back(c[y]);
            --v[x];
            --v[y];
        }
        //cout<<str<<endl;
        //printf("v[%d] = %d\n", x, v[x]);
        while (v[x]) {
            const int n = str.size();
            for (int p = 0; p < n; ++p) {
                if (c[x] != str[p] && c[x] != str[(p+1)%n]) {
                    str.insert((p+1)%n, 1, c[x]);
                    --v[x];
                    //printf("inseri: v[%d] = %d\n", x, v[x]);
                    goto next_insertion;
                }
            }
            str = "";
            goto out;
next_insertion:;
        }

out:
        ans = str;
        printf("Case #%d: ", testcase);
        if (ans.empty()) {
            puts("IMPOSSIBLE");
        } else {
            int rr = 0, ry = 0, rb  = 0;
            for (char c : ans)
                if (c == 'R')
                    ++rr;
                else if (c == 'Y')
                    ++ry;
                else if (c == 'B')
                    ++rb;
                else
                    throw 42;
            const int n = ans.size();
            for (int i = 0; i < n; ++i)
                assert(ans[i] != ans[(i+n-1)%n] && ans[i] != ans[(i+1)%n]);
            assert(rr == orir);
            assert(ry == oriy);
            assert(rb == orib);
            cout<<ans<<'\n';
        }
    }
}
