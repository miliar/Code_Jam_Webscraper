#include<cstdio>
#include<cstring>
#include<queue>
#include<vector>

using namespace std;

#define N 110

int tasu[2*N], kakeru[N];
bool ut0[2*N], *ut=ut0+N, uk[N], iso[N];

struct model{
    char t;
    int i, j;
    model(const char &t=0, const int &i=0, const int &j=0): t(t), i(i), j(j){}
};

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        int n, m;
        scanf("%d%d", &n, &m);
        for(int i=0; i<=2*n-2; i++){
            tasu[i] = -N;
        }
        memset(kakeru, -1, sizeof(kakeru));
        memset(ut0, false, sizeof(ut0));
        memset(uk, false, sizeof(uk));
        memset(iso, false, sizeof(iso));
        int y = 0;
        while(m--){
            char t[2];
            int i, j;
            scanf("%s%d%d", t, &i, &j);
            i--; j--;
            if(t[0] == '+'){
                tasu[i+j] = i-j;
                ut[i-j] = true;
                y++;
            }else if(t[0] == 'x'){
                kakeru[i] = j;
                uk[j] = true;
                y++;
            }else{
                tasu[i+j] = i-j;
                ut[i-j] = true;
                kakeru[i] = j;
                uk[j] = true;
                y += 2;
            }
        }
        printf("Case #%d: ", kase);
        queue<int> loli;
        if(!ut[0]){
            tasu[0] = 0;
            y++;
        }
#define shota(jj) do{\
        for(int i=jj; i<=n-2; i+=2){\
            if(!ut[i]){\
                loli.push(i);\
            }\
            if(!ut[-i]){\
                loli.push(-i);\
            }\
            if(tasu[i] == -N && !loli.empty()){\
                tasu[i] = loli.front(); loli.pop();\
                y++;\
            }\
            if(tasu[2*n-2-i] == -N && !loli.empty()){\
                tasu[2*n-2-i] = loli.front(); loli.pop();\
                y++;\
            }\
        }\
    }while(0)
        shota(1);
        while(!loli.empty()){
            loli.pop();
        }
        shota(2);
        if(tasu[n-1] == -N){
            tasu[n-1] = n-1;
            y++;
        }
        for(int i=0, j=0; i<=n-1;){
            if(~kakeru[i]){
                i++; continue;
            }
            if(uk[j]){
                j++; continue;
            }
            kakeru[i] = j++;
            y++;
        }
        vector<model> ans;
        for(int i=0; i<=2*n-2; i++){
            if(tasu[i] > -N && !ut[tasu[i]]){
                int r = (i+tasu[i])/2, c = (i-tasu[i])/2;
                if(kakeru[r] == c){
                    iso[r] = true;
                }else{
                    ans.push_back(model('+', r+1, c+1));
                }
            }
        }
        for(int i=0; i<=n-1; i++){
            if(!uk[kakeru[i]]){
                if(tasu[i+kakeru[i]] == i-kakeru[i]){
                    ans.push_back(model('o', i+1, kakeru[i]+1));
                }else{
                    ans.push_back(model('x', i+1, kakeru[i]+1));
                }
            }else if(iso[i]){
                ans.push_back(model('o', i+1, kakeru[i]+1));
            }
        }
        printf("%d %d\n", y, (int)ans.size());
        for(int i=0; i<(int)ans.size(); i++){
            printf("%c %d %d\n", ans[i].t, ans[i].i, ans[i].j);
        }
    }
    return 0;
}
