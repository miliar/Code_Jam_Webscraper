#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

struct horse{
    int pos;
    int speed;
};

bool operator<(struct horse a, struct horse b){
  return a.pos > b.pos;
}

vector<struct horse> horses;

int main(){
    int T;
    scanf("%d ", &T);
    int i;
    for(i = 1; i <= T; i++){
        int D, N;
        horses.clear();
        scanf("%d %d ", &D, &N);
        for(int i1 = 0; i1 < N; i1++){
            int a,b;
            scanf("%d %d ", &a, &b);
            struct horse h;
            h.pos = a;
            h.speed = b;
            horses.push_back(h);
        }
        double time = 0.;
        sort(horses.begin(), horses.end());
        for(auto it = horses.begin(); it != horses.end(); ++it){
            double curr_time = (D - it->pos)/(double)it->speed;
            if(curr_time > time)
                time = curr_time;
        }
        printf("Case #%d: %lf\n", i, D / time);
    }

    return 0;
}
