// Small only since it seems to not actually obey increasing then decreasing...?

#include <algorithm>
#include <iostream>

using namespace std;

typedef long long ll;

ll round_up(ll num, ll den) {
	return (num + den - 1) / den;
}

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		ll dragon_hp, dragon_atk, knight_hp, knight_atk, buff, debuff;
		cin >> dragon_hp >> dragon_atk >> knight_hp >> knight_atk >> buff >> debuff;

		ll offensive_moves = round_up(knight_hp, dragon_atk);
		if (buff > 0) { // try buffing to speed things up...
			int buff_times = 1;
			while (dragon_atk + (buff_times - 1) * buff < knight_hp) { // at most O(sqrt(10^9)) iters
				ll possible = buff_times + round_up(knight_hp, dragon_atk + buff * buff_times);
				if (possible <= offensive_moves) offensive_moves = possible;
				// else break;
				buff_times++;
			}
		}

		ll total = 3000000000ll;

		// debuffing is useful only if double-debuffing is good enough to tank two hits
		if (debuff > 0 && max(knight_atk - debuff, 0ll) + max(knight_atk - 2*debuff, 0ll) < dragon_hp) {
			ll curr_hp = dragon_hp;
			ll true_hp = round_up(dragon_hp, knight_atk);
			
			if (offensive_moves <= true_hp)
				total = offensive_moves;
			else if (true_hp > 2)
				total = offensive_moves + round_up(offensive_moves - true_hp, true_hp - 2); // no debuffs
			
			ll moves_so_far = 0;
			// try one more debuff
			while (true) {
				if (knight_atk - debuff >= curr_hp) { // got to heal
					moves_so_far++;
					curr_hp = dragon_hp - knight_atk;
				}
				moves_so_far++;
				knight_atk = max(knight_atk - debuff, 0ll);
				curr_hp -= knight_atk;

				if (knight_atk == 0) {
					ll poss = moves_so_far + offensive_moves;
					if (poss < total) total = poss;
					break;
				}

				// what happens if, no more debuff?
				if (round_up(dragon_hp, knight_atk) > 2) {
					ll poss = moves_so_far + offensive_moves + round_up(offensive_moves - round_up(curr_hp, knight_atk), round_up(dragon_hp, knight_atk) - 2);
					if (poss <= total) total = poss;
					// else break;
				}
			}
		} else {
			ll true_hp = round_up(dragon_hp, knight_atk);
			if (true_hp <= 2) { // have to win in one/two attacks, since healing is useless
				if (offensive_moves <= true_hp) {
					total = offensive_moves;
				} else {
					total = -1;
				}
			} else {
				total = offensive_moves + round_up(offensive_moves - true_hp, true_hp - 2);
			}
		}

		cout << "Case #" << test << ": ";
		if (total > 0) {
			cout << total;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}