#include <cstdio>
#include <string>
#include <vector>
int main(){
    int T;
    scanf("%d",&T);
    for(int tc = 1; tc <= T ; tc++){
        int n;
        char s[100];
        scanf("%s", s);
        printf("Case #%d: ",tc);
        std::vector<std::string> data;
        for(int i = 0; s[i]!=0; i++){
            data.push_back(s);
            if(s[i]== 0) break;
            data[i][i]--;
            for(int j = i+1; j < data[i].size(); j++) data[i][j]='9';
        }
        data.push_back(s);
        long long ans = 0;
        for(auto ss : data){
            long long pv = 0;
            for(int i = 0; i < ss.size(); i++){
                pv = pv * 10 + ss[i]-'0';
                if(i != 0 && ss[i] < ss[i-1]) {
                    pv = -1;
                    break;
                }
            }
            if(pv != -1) ans = std::max(ans,pv);
        }
        printf("%lld\n",ans);
    }
}
