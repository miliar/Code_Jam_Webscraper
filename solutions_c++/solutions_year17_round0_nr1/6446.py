#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

int main(){
    int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		char s[1005];
		int K;
		cin >> s >> K;
		int ans = 0, l = strlen(s);
		for(int j = 0; j <= l-K; j++){
			if(s[j] == '+')
				continue;
			ans++;
			for(int k = j; k < j+K; k++){
				if(s[k] == '-')
					s[k] = '+';
				else
					s[k] = '-';
			}
		}
		bool f = false;
		for(int j = l-K; j < l; j++){
			if(s[j] == '-'){
				f = true;
				break;
			}
		}
		if(!f)
			cout << "Case #" << i << ": " << ans << endl;
		else
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}
