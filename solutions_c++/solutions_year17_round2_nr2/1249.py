#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <bitset>
#include <cstdio>
#include <sstream>
#include <string>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <cctype>
#include <iomanip>
#include <list>
#include <cstring>

#define INF 2000000000
#define ull unsigned long long int
#define vi vector<int>
#define vii vector<ii>
#define int long long int

#define UNVISITED 0
#define OPENED 1
#define CLOSED 2

#define PI 3.14159265359

#define D(x) cout<<#x<<" : "<<x<<endl
#define P(x) cout << x << endl;

#define RED 1
#define YELLOW 2
#define BLUE 4
#define ORANGE 3
#define VIOLET 5
#define GREEN 7

using namespace std;

int n;

int color[10];
int sol[1010];
int compt;
bool cp(int deep, int firstColor, int lastColor) {
	if(deep == n) {
		compt++;
		if(lastColor == firstColor) return false;
		else {

			for(int i= 0; i < n; i++) {
				if(sol[i] == RED) cout << 'R';
				if(sol[i] == YELLOW) cout << 'Y';
				if(sol[i] == BLUE) cout << 'B';
				if(sol[i] == GREEN) cout << 'G';
				if(sol[i] == VIOLET) cout << 'V';
				if(sol[i] == ORANGE) cout << 'O';
			}
			cout << endl;
			return true;
		}
	}
	else {
		vector <pair<int, int> > v;
		for(int i= 1; i <= 7; i++) {
			v.push_back(make_pair(-color[i], i));
		}
		sort(v.begin(), v.end());
		
		for(int j= 1; j <= 7; j++) {
			if(compt > 100) return false;
			int i = v[j-1].second;
			if((i & lastColor)==0 && color[i] > 0) {
				sol[deep] = i;
				
				bool flag = false;
				color[i]--;
				if(deep == 0) flag = cp(deep+1, i, i);
				else flag = cp(deep+1, firstColor, i);
				color[i]++;
				if(flag) return true;
			}
		}
		
		return false;
	}
}


signed main () {
	int nTest; cin >> nTest;
	for(int iTest = 0; iTest < nTest; iTest++) {
		compt = 0; 
		cin >> n;
		int R, O, Y, G, B, V;
		cin >> R >> O >> Y >> G >> B >> V;
		
		color[RED] = R;
		
		color[RED] = R; color[YELLOW] = Y; color[BLUE] = B;
		color[ORANGE] = O; color[VIOLET] = V; color[GREEN] = G;
		printf("Case #%lld: ", iTest+1);	
		if(R > n/2 || B > n/2 || Y > n/2 || !cp(0,-1,8)) {
			printf("IMPOSSIBLE\n");
		}
		
		/*
		int last = -1;
		vector <int> t;
	
		for(int i= 0; i <n; i++) {
			int first = 1, second = 1;
			if(color[RED] >= color[YELLOW] && color[RED] >= color[BLUE]) first = RED;
			if(color[YELLOW] >= color[RED] && color[YELLOW] >= color[BLUE]) first = YELLOW;
			if(color[BLUE] >= color[YELLOW] && color[BLUE] >= color[RED]) first = BLUE;
		
			if((color[RED] >= color[YELLOW] || color[RED] >= color[BLUE]) && RED != first) second = RED;
			if((color[YELLOW] >= color[RED] || color[YELLOW] >= color[BLUE]) && YELLOW != first) second = YELLOW;
			if((color[BLUE] >= color[YELLOW] || color[BLUE] >= color[RED]) && BLUE != first) second = BLUE;
		
			if(first == last) {
				if(second == last) return 0;
				t.push_back(second); last = second; 
			}
			else{
				t.push_back(first); last = first;
			}
			if(i > 1 && t[i] == t[i-1]) return 0;
			color[last]--;
		}
		
		
		
		if(t[n-1] == t[0]) {printf("Case #%lld: IMPOSSIBLE\n", iTest+1);
			cout << R << " " << B << " " << Y << " " <<n << endl;
			for(int i= 0; i <n ;i++) {
				if(t[i] == RED) cout << 'R';
				if(t[i] == YELLOW) cout << 'Y';
				if(t[i] == BLUE) cout << 'B';
			}
		}
		else {
			printf("Case #%lld: ", iTest+1);
			for(int i= 0; i <n ;i++) {
				if(t[i] == RED) cout << 'R';
				if(t[i] == YELLOW) cout << 'Y';
				if(t[i] == BLUE) cout << 'B';
			}
			cout << endl;
		}*/
	}
	
	
	
	
	
	return 0;
}
