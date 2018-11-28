#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

struct Solver {
    int Hd, Ad, Hk, Ak, B, D;

    Solver() {
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
    }

    int solveAttack(int hp, int my_attack, int enemy_attack) {
        // My current hp is hp.
        // My strategy is:
        // if (hp > enemy_attack) attack
        // else cure
        // This is the minimum.
        int ret = (Hk + my_attack - 1) / my_attack;
        if (enemy_attack * (ret - 1) < hp) return ret;  // I can survive without curing.
        // He can indeed kill me if I don't cure.

        if (Hd <= 2 * enemy_attack) {
            // I can only keep curing.
            return -1;
        }

        // Let's sim....
        int enemy_hp = Hk;
        int ans = 1;
        for (int enemy_hp = Hk; enemy_hp > my_attack; ++ans) {
            if (hp <= enemy_attack) {
                hp = Hd;
            } else {
                enemy_hp -= my_attack;
            }
            hp -= enemy_attack;
        }
        return ans;

        int remainder = ret;
        int cure_turn = (hp / enemy_attack);
        ++ret;
        // Execute cure after cure_turn.
        int full_cure_turn = ((Hd - enemy_attack) / enemy_attack);
        // Then execute cure after each full_cure_turn.
        // Let's say I need to attack 7 times.
        // I need cure after my first attack.
        // Then I need cure after every 3 attacks.
        return ret + ((remainder - cure_turn - 1) / full_cure_turn);
    }

    int solveBuff(int hp, int enemy_attack) {
        if (B == 0) return solveAttack(hp, Ad, enemy_attack);
        // I will only buff at most 100 times.
        int turns = 0;
        int my_attack = Ad;
        // 0 buff.
        int ans = solveAttack(hp, my_attack, enemy_attack);
        for (int i = 0; i < 100; ++i) {
            if (hp <= enemy_attack) {
                ++turns;
                hp = Hd - enemy_attack;
                if (hp <= enemy_attack) {
                    // I can never buff myself.
                    break;
                }
            }
            // Buff myself.
            ++turns;
            my_attack += B;
            hp -= enemy_attack;
            int tmp = solveAttack(hp, my_attack, enemy_attack);
            if (tmp > -1 && (turns + tmp < ans || ans == -1)) ans = turns + tmp;
        }
        return ans;
    }

    int solve() {
        // As a dragon, I always performs some number of debuff,
        // followed by some number of buff,
        // follow by simple attacks.
        // Cure happens as needed.

        int hp = Hd;
        int enemy_attack = Ak;

        if (D == 0) return solveBuff(hp, enemy_attack);
        int ans = solveBuff(hp, enemy_attack);
        int turns = 0;
        for (int i = 0; i < 100; ++i) {
            // If I must cure before debuffing...
            if (hp <= (enemy_attack - D)) {
                ++turns;
                hp = Hd - enemy_attack;
                if (hp <= (enemy_attack - D)) {
                    // I can never debuff him.
                    break;
                }
            }
            // Debuff him.
            ++turns;
            enemy_attack -= D;
            if (enemy_attack < 0) enemy_attack = 0;
            hp -= enemy_attack;
            int tmp = solveBuff(hp, enemy_attack);
            if (tmp > -1 && (turns + tmp < ans || ans == -1)) ans = turns + tmp;
        }
        return ans;
    }
};

int main() {
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        Solver solver;
        int ans = solver.solve();
        cout << "Case #" << case_index << ": ";
        if (ans == -1) cout << "IMPOSSIBLE";
        else cout << ans;
        cout << endl;
    }
    return 0;
}
