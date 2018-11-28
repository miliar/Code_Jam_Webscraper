#include <cstdio>
#include <string>
#include <queue>
#include <map>
#include <utility>
#include <iostream>

using namespace std;

int main() {
    int t, k, ans, cases=0;
    queue< pair<string, int> > q;
    string s;
    map<string, int> visited;
    size_t found;

    scanf("%d", &t);

    while (t--) {
        cin >> s;
        scanf("%d", &k);

        //cout << "s = " << s << ", k = " << k << endl;

        q.push({s, 0});
        visited[s] = 1;
        ans = -1;
        while (!q.empty()) {
            pair<string, int> f = q.front(); q.pop();
            string atual = f.first; int dist = f.second;
            //cout << atual << ", dist=" << dist << endl;
            found = atual.find("-");
            if (found == string::npos) {
                ans = dist;
                break;
            }

            for (int i = 0 ; i <= atual.size()-k ; i++) {
                string nova = atual;
                for(int j = 0 ; j < k ; j++){
                    nova[j+i] = nova[j+i] == '+' ? '-' : '+';
                }
                if(!visited[nova]) {
                    visited[nova] = 1;
                    q.push({nova, dist+1});
                }
            }
        }

        if(ans != -1)
            printf("Case #%d: %d\n", ++cases, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", ++cases);

        while(!q.empty()) q.pop();
        visited.clear();
    }

    return 0;
}
