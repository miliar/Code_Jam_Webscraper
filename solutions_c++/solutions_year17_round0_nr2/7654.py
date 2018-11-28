#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cctype>
#include <cassert>
#include <numeric>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <list>
#include <set>          
#include <map>
#include <unordered_set>
#include <cstdio>
#include <string>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <climits>
#include <iomanip>

using namespace std;

int t, testnum = 1;
long long n;

long long mujhe_pata_hai_ye_function_me_likha_hua_tumhe_ghanta_samajh_nahi_aega() {
	vector<int> kehna_kya_chahte_ho;
	long long naya_hai_n = n;
	while (naya_hai_n > 0) {
		kehna_kya_chahte_ho.push_back(naya_hai_n % 10);
		naya_hai_n /= 10;
	}
	reverse(kehna_kya_chahte_ho.begin(), kehna_kya_chahte_ho.end());
	int tatti_hui_ya_nahi = (int)kehna_kya_chahte_ho.size();
	while (true) {
		bool found_hua_ki_nahi = true;
		for (int i = 0; i + 1 < tatti_hui_ya_nahi; i++) {
			if (kehna_kya_chahte_ho[i] > kehna_kya_chahte_ho[i + 1]) {
				found_hua_ki_nahi = false;
				kehna_kya_chahte_ho[i]--;
				for (int j = i + 1; j < tatti_hui_ya_nahi; j++)
					kehna_kya_chahte_ho[j] = 9;

			}
		}
		if (found_hua_ki_nahi)	break;
	}
	int mera_index = 0;
	for (int i = 0; i < tatti_hui_ya_nahi; i++) if (kehna_kya_chahte_ho[i] != 0) {
		mera_index = i;
		break;
	} 
	long long de_do_koi_achcha_Answer_mujhe = 0;
	for (int i = mera_index; i < tatti_hui_ya_nahi; i++) {
		de_do_koi_achcha_Answer_mujhe = 10 * de_do_koi_achcha_Answer_mujhe + kehna_kya_chahte_ho[i];
	}
	return de_do_koi_achcha_Answer_mujhe;
}

int main(){

    
    scanf("%d", &t);
    while (testnum <= t) {
        scanf("%lld", &n);
        cout << "Case #" << testnum << ": " << mujhe_pata_hai_ye_function_me_likha_hua_tumhe_ghanta_samajh_nahi_aega() << "\n";
        testnum++;
    }


    return 0;
}