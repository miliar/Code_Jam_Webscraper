#include<stdio.h>
#include<string.h>
#include<math.h>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N;
int R, O, Y, G, B, V;
class unicorn{
public:
    char incompatible[3];
    char letter;
    int count;
    unicorn(char l, int c){
        letter = l;
        count = c;
        switch(letter) {
        case 'R':
            incompatible[0] = 'R';
            incompatible[1] = 'V';
            incompatible[2] = 'V';
            break;
        case 'O':
            incompatible[0] = 'O';
            incompatible[1] = 'R';
            incompatible[2] = 'Y';
            break;
        case 'Y':
            incompatible[0] = 'Y';
            incompatible[1] = 'Y';
            incompatible[2] = 'O';
            break;
        case 'G':
            incompatible[0] = 'G';
            incompatible[1] = 'Y';
            incompatible[2] = 'B';
            break;
        case 'B':
            incompatible[0] = 'B';
            incompatible[1] = 'B';
            incompatible[2] = 'G';
            break;
        case 'V':
            incompatible[0] = 'V';
            incompatible[1] = 'R';
            incompatible[2] = 'B';
            break;
        }
    }
    unicorn(const unicorn &o){
        letter = o.letter;
        count = o.count;
        memcpy(incompatible, o.incompatible, sizeof(incompatible));
    }
    bool operator<(unicorn &o){
        return count < o.count;
    }
};
vector<unicorn> list;
char ssolve[1010];
bool solve(char last, int C, bool last_max, int alg) {
    if(C == N) return true;
    switch(alg){
    case 0:
        if (last_max) {
            for(int i = 0; i < 6; ++i) {
                if (list[i].count <= 0 ||
                        list[i].incompatible[0] == last ||
                        list[i].incompatible[1] == last ||
                        list[i].incompatible[2] == last)
                    continue;
                if(C == N - 1 && (
                    list[i].incompatible[0] == ssolve[0] ||
                    list[i].incompatible[1] == ssolve[0] ||
                    list[i].incompatible[2] == ssolve[0]))
                    return false;
                ssolve[C] = list[i].letter;
                list[i].count--;
                sort(list.begin(), list.end());
                return solve(ssolve[C], C + 1, !last_max, alg);
            }
        } else {
            for(int i = 5; i >= 0; --i) {
                if (list[i].count <= 0 ||
                        list[i].incompatible[0] == last ||
                        list[i].incompatible[1] == last ||
                        list[i].incompatible[2] == last)
                    continue;
                if(C == N - 1 && (
                    list[i].incompatible[0] == ssolve[0] ||
                    list[i].incompatible[1] == ssolve[0] ||
                    list[i].incompatible[2] == ssolve[0]))
                    return false;
                ssolve[C] = list[i].letter;
                list[i].count--;
                sort(list.begin(), list.end());
                return solve(ssolve[C], C + 1, !last_max, alg);
            }
        }
        break;
    case 1:
        if (!last_max) {
            for(int i = 0; i < 6; ++i) {
                if (list[i].count <= 0 ||
                        list[i].incompatible[0] == last ||
                        list[i].incompatible[1] == last ||
                        list[i].incompatible[2] == last)
                    continue;
                if(C == N - 1 && (
                    list[i].incompatible[0] == ssolve[0] ||
                    list[i].incompatible[1] == ssolve[0] ||
                    list[i].incompatible[2] == ssolve[0]))
                    return false;
                ssolve[C] = list[i].letter;
                list[i].count--;
                sort(list.begin(), list.end());
                return solve(ssolve[C], C + 1, !last_max, alg);
            }
        } else {
            for(int i = 5; i >= 0; --i) {
                if (list[i].count <= 0 ||
                        list[i].incompatible[0] == last ||
                        list[i].incompatible[1] == last ||
                        list[i].incompatible[2] == last)
                    continue;
                if(C == N - 1 && (
                    list[i].incompatible[0] == ssolve[0] ||
                    list[i].incompatible[1] == ssolve[0] ||
                    list[i].incompatible[2] == ssolve[0]))
                    return false;
                ssolve[C] = list[i].letter;
                list[i].count--;
                sort(list.begin(), list.end());
                return solve(ssolve[C], C + 1, !last_max, alg);
            }
        }
        break;
    case 2:
        for(int i = 5; i >= 0; --i) {
            if (list[i].count <= 0 ||
                    list[i].incompatible[0] == last ||
                    list[i].incompatible[1] == last ||
                    list[i].incompatible[2] == last)
                continue;
            if(C == N - 1 && (
                list[i].incompatible[0] == ssolve[0] ||
                list[i].incompatible[1] == ssolve[0] ||
                list[i].incompatible[2] == ssolve[0]))
                return false;
            ssolve[C] = list[i].letter;
            list[i].count--;
            sort(list.begin(), list.end());
            return solve(ssolve[C], C + 1, !last_max, alg);
        }
        break;
    case 3:
        for(int i = 0; i < 6; ++i) {
            if (list[i].count <= 0 ||
                    list[i].incompatible[0] == last ||
                    list[i].incompatible[1] == last ||
                    list[i].incompatible[2] == last)
                continue;
            if(C == N - 1 && (
                list[i].incompatible[0] == ssolve[0] ||
                list[i].incompatible[1] == ssolve[0] ||
                list[i].incompatible[2] == ssolve[0]))
                return false;
            ssolve[C] = list[i].letter;
            list[i].count--;
            sort(list.begin(), list.end());
            return solve(ssolve[C], C + 1, !last_max, alg);
        }
        break;
    }
    return false;
}

int main() {
    int T;
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for(int i = 0; i < T;++i) {
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
        bool resolved = false;
        for(int alg = 0; alg <4 && !resolved; ++alg) {
            list.clear();
            list.push_back(unicorn('R', R));
            list.push_back(unicorn('O', O));
            list.push_back(unicorn('Y', Y));
            list.push_back(unicorn('G', G));
            list.push_back(unicorn('B', B));
            list.push_back(unicorn('V', V));
            memset(ssolve, 0x00, sizeof(ssolve));
            sort(list.begin(), list.end());
            if (solve('X', 0, true, alg)) {
                printf("Case #%d: %s\n", i+1, ssolve);
                resolved = true;
            }
        }
        if(!resolved)
            printf("Case #%d: IMPOSSIBLE\n", i+1);
    }

    return 0;
}
