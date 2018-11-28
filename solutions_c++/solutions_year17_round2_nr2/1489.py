#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int col[6];
int main()
{
    int T;cin>>T;
    for(int TT = 1; TT <= T; ++TT) {
        printf("Case #%d: ", TT);
        int N; cin>>N;
        for (int i = 0; i < 6; ++i) {
            cin>>col[i];
        }
        pair<int, char> a[3] = {make_pair(col[0], 'R'), make_pair(col[2], 'Y'), make_pair(col[4], 'B')};
        sort(a, a + 3);
        int sum = a[0].first + a[1].first + a[2].first;
        if(a[2].first > sum / 2) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        vector<char> ans;
        ans.push_back(a[2].second);
        a[2].first --;
        bool flag = true;
        for(int i = 1; i < N; ++i) {
            int ptr = -1;
            char last = *ans.rbegin();

            for(int i = 0; i < 3; ++i) {
                if(a[i].second != last) {
                    if(ptr == -1) {
                        ptr = i;
                    } else if(a[i].first >= a[ptr].first) {
                        ptr = i;
                    }
                }
            }
            //cout<<ptr<<" "<<a[ptr].second<<" "<<a[ptr].first<<endl;
            if(a[ptr].first) {
                ans.push_back(a[ptr].second);
                a[ptr].first--;
            } else {
                flag = false;
            }
        }
        for(int i = 1; i < N; ++i) {
            if(ans[i] == ans[i - 1]) {
                flag = false;
            }
        }
        if(ans[0] == ans[N - 1]) flag = false;
        if(flag) {
            for(int i = 0; i < N; ++i) {
                printf("%c", ans[i]);
            }
            cout<<endl;
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}