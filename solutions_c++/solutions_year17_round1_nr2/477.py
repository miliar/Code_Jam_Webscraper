#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int T;
int n, p;
int req[55];
int ptr[55];
vector<int> in[55];

int main() {
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++){
        scanf("%d %d", &n, &p);
        for(int i = 0; i < n; i++){
            ptr[i] = 0;
            scanf("%d", &req[i]);
        }

        for(int i = 0; i < n; i++){
            in[i].clear();
            for(int j = 0; j < p; j++){
                int temp;
                scanf("%d", &temp);
                in[i].push_back(temp);
            }
            sort(in[i].begin(), in[i].end());
        }

        int ans = 0;

        int sv = 1;
        bool kit = true;
        while(kit){
            bool can = true;
            while(can && kit){
                for(int i = 0; i < n; i++){
                    double minn = (req[i] * sv) * 9;
                    double maxx = (req[i] * sv) * 11;

                    while(ptr[i] < p && in[i][ptr[i]] * 10 < minn){
                        ptr[i]++;
                    }

                    if(ptr[i] == p){
                        kit = false;
                        can = false;
                    }
                    else if(maxx < in[i][ptr[i]] * 10){
                        can = false;
                    }
                }

                if(can){
                    ans ++;
                    for(int i = 0; i < n; i++){
                        ptr[i]++;
                    }
                }
            }
            sv++;
        }

        printf("Case #%d: %d\n", tt, ans);
    }
}
