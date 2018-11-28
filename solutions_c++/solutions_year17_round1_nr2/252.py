#include <cstdio>
#include <vector>
#include <algorithm>

typedef std::pair<int,int> ii;

int serv_size[55], N, P;
std::vector<ii> package[55];
int select[55];
bool taken[55][55];

// Returns minimum servings
int calc_max(int size, int quantity){ // Ingredient and quantity of a package
    return 10*quantity / (9*size);
}

// Returns maximum servings
int calc_min(int size, int quantity){ // Ingredient and quantity of a package
    return 10*quantity / (11*size) + (10*quantity % (11*size) != 0);
}

bool recurse(int ing, ii bounds){
    if(ing >= N)
        return true;

    for(int i = 0; i < package[ing].size(); i++){
        if(taken[ing][i]) continue;

        ii next = package[ing][i];
        if(next.first > bounds.second || next.second < bounds.first) continue;

        select[ing] = i;
        ii new_bounds = ii(std::max(bounds.first, next.first), std::min(bounds.second, next.second));
        if(recurse(ing+1, new_bounds))
            return true;
    }

    return false;
}

int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++){
        for(int i = 0; i < 55; i++){
            package[i].clear();
            for(int j = 0; j < 55; j++)
                taken[i][j] = false;
        }

        scanf("%d%d", &N, &P);

        for(int i = 0; i < N; i++)
            scanf("%d", serv_size + i);

        for(int i = 0; i < N; i++)
        for(int p = 0, next; p < P; p++){
            scanf("%d", &next);

            int s_min = calc_min(serv_size[i], next);
            int s_max = calc_max(serv_size[i], next);

            //printf("Next = %d, bounds = (%d,%d)\n", next, s_min, s_max);

            if(s_max > 0 && s_min <= s_max)
                package[i].push_back(ii(s_min, s_max));
        }

        for(int i = 0; i < N; i++){
            sort(package[i].begin(), package[i].end());
            //for(int j = 0; j < package[i].size(); j++)
                //printf("(%d,%d) ", package[i][j].first, package[i][j].second);
            //printf("\n");
        }

        int ans = 0;
        for(int i = 0; i < package[0].size(); i++){
            select[0] = i;
            if(recurse(1, package[0][i])){
                ans++;
                for(int i = 0; i < N; i++)
                    taken[i][select[i]] = true;
            }
        }

        printf("Case #%d: %d\n", t, ans);
    }
}

