#include <iostream>
#include <cassert>
#include <string>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <stdint.h>
#include <cstdio>
#include <map>
#include <queue>

using namespace std;
int main(int argc, char **argv) {
    int T;
    cin >> T;
    for(int cn=1;cn<=T;++cn) {
        int R,C;
        cin >> R >> C;
        vector<string> v;
        for(int i=0;i<R;++i) {
            string s;
            cin >> s;
            v.push_back(s);
        }
        vector<vector<int> > sums(R+1, vector<int>(C+1, 0));
        for(int r=0;r<R;++r) {
            for(int c=0;c<C;++c) {
                sums[r][c+1] = (v[r][c] != '?') + sums[r][c];
            }
        }
        vector<vector<int> > ok(C, vector<int>(C, 0));
        for(int a=0;a<C;++a) {
            for(int b=a;b<C;++b) {
                bool good = true;
                bool didit = false;
                for(int r=0;r<R;++r) {
                    if(sums[r][b+1] - sums[r][a] > 1) {
                        good = false;
                        break;
                    }
                    if(sums[r][b+1] - sums[r][a] > 0) {
                        didit = true;
                    }
                }
                ok[a][b] = (good && didit);
            }
        }
        pair<int,int> memo[50];
        memo[C] = make_pair(1, -1);
        for(int c=C-1;c>=0;--c) {
            for(int d=c;d<C;++d) {
                if(ok[c][d] && memo[d+1].first) {
                    memo[c] = make_pair(1,d+1);
                    goto gg;
                }
            }
            memo[c] = make_pair(0, 0);
            gg:;
        }
        assert(memo[0].first == 1);
        int cat = 0;
        while(cat < C) {
            char first_let = '*';
            char curr_let = '?';
            assert(memo[cat].first == 1);
            int next_thing = memo[cat].second;
            vector<char> labels;
            for(int r=0;r<R;++r) {
                for(int c=cat;c<next_thing;++c) 
                {
                    if(v[r][c] != '?') {
                        curr_let = v[r][c];
                        if(first_let == '*') {
                            first_let = curr_let;
                        }
                    }
                }
                labels.push_back(curr_let);
            }
            for(int r=0;r<R;++r) {
                char zz = labels[r];
                if(zz == '?'){zz = first_let;}
                for(int c=cat;c<next_thing;++c) 
                {
                    v[r][c] = zz;
                }
            }
            cat = next_thing;
        }
        printf("Case #%d:\n", cn);
        for(int i=0;i<R;++i) 
        {
            printf("%s\n", v[i].c_str());
        }
    }
    return 0;
}
