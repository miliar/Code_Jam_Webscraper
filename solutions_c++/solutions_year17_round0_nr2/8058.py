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
	freopen("B-large.in","r",stdin);
	freopen("outputB.txt","w",stdout);
	
	int t;
	cin >> t;
	for (int ii = 1; ii <= t; ii++){
		ll n;
		int a[20], c = 0;
		cin >> n;
		while(n > 0){
			a[c] = n % 10;
			n /= 10;
			c++;
		}
		
		for (int i = 0; i < c-1; i++){
			if (a[i] < a[i+1]){
				for (int j = i; j >= 0; j--){
					a[j] = 9;
				}
				a[i+1]--;
			}
		}
		
		for (int i = c - 1; i >= 0; i--){
			n *= 10;
			n += a[i];
		}
		
		cout << "Case #" << ii << ": ";
		cout << n << endl;
		
	}

 	return 0;
}
