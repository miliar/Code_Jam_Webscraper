#include <bits/stdc++.h>
// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
#define dibs reserve
#define OVER9000 1234567890123456789LL
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-8
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
#define dbl long double
#define pi 3.14159265358979323846
using namespace std;
// mylittledoge

#ifdef DONLINE_JUDGE
	// palindromic tree is better than splay tree!
	#define lld I64d
#endif

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
//	int hd[110][110], turns[110][110];
	for(int t =0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		int Hd,Ad,Hk,Ak,B,D;
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		if(Ad >= Hk) {
			cout << "1\n";
			continue;}
		if(Hd <= Ak-D) {
			cout << "IMPOSSIBLE\n";
			continue;}
/*		hd[0][0] =Hd;
		turns[0][0] =0;
		for(int i =0; i <= 101; i++) turns[i][0] =-1;
		for(int i =0; i <= 100; i++) {
			int ak =Ak-(i+1)*D;
			if(hd[i][0] > ak) hd[i+1][0] =hd[i][0]-ak, turns[i+1][0] =turns[i][0]+1;
			}
*/		int ans =-1;
		for(int d =0; d <= ((D == 0)?0:Ak); d++) 
			for(int b =0; b <= ((B == 0)?0:Hk); b++) {
				int hd =Hd, ak =Ak, turns =0;
				for(int i =0; i < d; i++) {
					if(ak-D >= hd) {
						hd =Hd;
						hd -=ak;
						turns++;}
					if(ak-D >= hd) {
						turns =-1;
						break;}
					ak -=D;
					hd -=ak;
					turns++;}
				if(turns == -1) continue;
				for(int i =0; i < b; i++) {
					if(ak >= hd) {
						hd =Hd;
						hd -=ak;
						turns++;}
					if(ak >= hd) {
						turns =-1;
						break;}
					hd -=ak;
					turns++;}
				if(turns == -1) continue;
				int hk =Hk;
				while(hk > 0) {
					if(hk <= Ad+b*B) {
						turns++;
						break;}
					if(ak >= hd) {
						hd =Hd;
						hd -=ak;
						turns++;}
					if(ak >= hd) {
						turns =-1;
						break;}
					hk -=Ad+b*B;
					hd -=ak;
					turns++;}
				ans =(ans == -1)?turns:min(ans,turns);}
		if(ans == -1) cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";}
	return 0;}

// look at my code
// my code is amazing
