#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

struct yee{
    int s, e;
    char p;
    bool operator<(const yee& y) const { return s < y.s; }
};

int main (){
    freopen ("pB.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t=1;t<=T;t++){
        vector<yee> v;
        int ac, aj;
        scanf("%d%d", &ac, &aj);
        if (ac==0 && aj==0){
            printf("Case #%d: 2\n", t);
            continue;
        }
        for (int i=0;i<ac;i++){
            int tmp1, tmp2;
            scanf("%d%d", &tmp1,&tmp2);
            v.push_back({tmp1,tmp2,'c'});
        }
        for (int i=0;i<aj;i++){
            int tmp1, tmp2;
            scanf("%d%d", &tmp1,&tmp2);
            v.push_back({tmp1,tmp2,'j'});
        }
        sort(v.begin(),v.end());

        vector<int> sc, sj;
        int cxw = 0;
        int usedc = (v[0].p == 'c'? v[0].e - v[0].s : 0);
        int usedj = (v[0].p == 'j'? v[0].e - v[0].s : 0);
        for (size_t i = 1;i<v.size();i++){
            if (v[i].p == 'c') usedc += v[i].e - v[i].s;
            else usedj += v[i].e - v[i].s;
            if (v[i].p != v[i-1].p){
                cxw ++;
            }
            else {
                if (v[i].p == 'c') sc.push_back(v[i].s - v[i-1].e);
                else sj.push_back(v[i].s - v[i-1].e);
            }
        }
        if (v[0].p != v.back().p){
            cxw ++;
        }
        else {
            if (v[0].p == 'c') sc.push_back(v[0].s + 1440 - v.back().e);
            else sj.push_back(v[0].s + 1440 - v.back().e);
        }
        sort(sc.begin(),sc.end());
        sort(sj.begin(),sj.end());

        int leftc = 720 - usedc;
        int leftj = 720 - usedj;
        size_t pos;
        bool is_fill = true;
        for (pos = 0; pos < sc.size() ; pos++){
            if (sc[pos] > leftc){
                is_fill = false;
                cxw += (sc.size() - pos) * 2;
                break;
            }
            else leftc -= sc[pos];
        }
        if (is_fill){
            for (pos = 0; pos < sj.size() ; pos++){
                if (sj[pos] > leftj){
                    cxw += (sj.size() - pos) * 2;
                    break;
                }
                else leftj -= sj[pos];
            }
        }
        printf("Case #%d: %d\n", t, cxw);
    }
}
