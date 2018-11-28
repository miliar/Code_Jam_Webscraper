#include <iostream>
#include <string>
#include <deque>
#include <set>
#include <utility>

using namespace std;

int main() {
    int T;

    cin >> T;
    for(int cs=1;cs<=T;cs++) {
        string s;
        int K;
        cin >> s >> K;

        set<string> ss;
        deque<pair<string, int>> q;
        q.push_back(make_pair(s,0));
        ss.insert(s);

        int l = s.size();
        string happy(l, '+');
        pair<string,int> t;
        while(!q.empty()) {
            t = q.front();
            if(t.first == happy) {
                break;
            }
            q.pop_front();

            for(int i=0;i<l;i++) {
                if(i+K>l) break;

                string s = t.first;
                for(int j=0;j<K;j++) {
                    if(s[i+j] == '+') s[i+j] = '-';
                    else s[i+j] = '+';
                }

                if(ss.find(s) == ss.end()) {
                    q.push_back(make_pair(s, t.second+1));
                    ss.insert(s);
                }
            }
        }

        if(q.empty()) {
            printf("Case #%d: IMPOSSIBLE\n", cs);
        } else {
            printf("Case #%d: %d\n", cs, t.second);
        }
    }

    return 0;
}
