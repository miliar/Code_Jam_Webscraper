#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	std::cin.tie();
	std::ios::sync_with_stdio(false);
	int cases;
	cin >> cases; int t = 1;
	while (cases--){
		string in; int x;
		int res = 0; bool ch = 0;
		cin >> in >> x;
		for (int i = 0; i < in.size(); i++){
			if (in[i] == '-'){
				res++;
				if (i + x - 1 >= in.size()){
					ch = 1;
					break;
				}
				for (int f = i; f < i + x; f++){
					if (in[f] == '-'){
						in[f] = '+';
					}
					else{
						in[f] = '-';
					}
				}
			}
		}
		cout << "Case #" << t++ << ": ";
		if (!ch)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}