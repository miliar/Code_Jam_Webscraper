#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cctype>
#include <cstring>
#include <bitset>
#include <algorithm>
#include <iomanip>
#include <string>

#define ld long double
#define ll long long
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define y0 _y0
#define y1 _y1

using namespace std;



int main(){
	freopen("A-large.in","r",stdin);
	freopen("outputA.txt","w",stdout);
	
	int t;
	cin >> t;
	for (int ii = 1; ii <= t; ii++){
		string s;
		int k, flips = 0;
		cin >> s >> k;
		for (int i = 0; i < s.length(); i++){
			if (s[i] == '-'){
				if (s.length() - i < k){
					flips = -1;
					break;
				}
				else{
					for (int j = i; j < i+k; j++){
						s[j] = (s[j] == '-' ? '+' : '-');
					}
					flips++;
				}
			}
		}
		cout << "Case #" << ii << ": ";
		if (flips < 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << flips << endl;
		
	}

 	return 0;
}
