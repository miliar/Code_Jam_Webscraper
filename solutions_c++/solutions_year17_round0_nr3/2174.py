// Bismillahirrahmanirrahim
// AgriCoder IPB
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <sstream>
#include <clocale>
#include <ctime>
#include <climits>
#include <cassert>
//#include <unordered_map>
using namespace std;

#define FOR(i, agri, coder) for (int i = (int)agri; i <= (int)coder; i++)
#define REP(agri,coder) for (int agri = 0; agri < (int)coder; agri++)
#define FOREACH(i,agricoder) for (typeof((agricoder).end()) i = (agricoder).begin(); i != (agricoder).end(); ++i)
//for (auto& it: agricoder)
#define RESET(agri,coder) memset(agri, coder, sizeof(agri))
#define pb push_back
#define mp make_pair
#define NL printf("==========================\n")
#define getchar_unlocked getchar // for codeforces

int arahbar[8] = {0,1,0,-1,1,1,-1,-1};
int arahkol[8] = {1,0,-1,0,1,-1,-1,1};
int kudabar[8] = {-2,-1,1,2, 2,1 , -1 ,-2};
int kudakol[8] = {1 ,2 ,2,1,-1,-2 , -2,-1};

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef unsigned int UNi;

template<typename T>
T getNum() {
   T res=0;
   char c;
   while(1)
   {
      c=getchar_unlocked();
      if(c==' ' || c=='\n') continue;
      else break;
   }
   bool negatif;
   if (c=='-') {
       negatif = true;
       res = 0;
   }
   else {
       res=c-'0';
       negatif = false;
   }
   while(1)
   {
      c=getchar_unlocked();
      if('0'<=c && c<='9') res=res*10 + c-'0';
      else break;
   }
   if (negatif) res*=-1;
   return res;
}

inline void boost() { //dont use with cstdio, dont use in interactives
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
}
//freopen("badmilk.in", "r", stdin);
//freopen("badmilk.out", "w", stdout);
//fclose(stdin);
//fclose(stdout);
#define INF 1000000000
#define EPS 1e-9
#define MAX_N 100005
// ================================  TEMPLATE ENDS HERE ================================================== /

LL jumbit(LL x) {
	LL ret = 0;
	do {
		ret++;
		x>>=1;
	} while (x);
	return ret;
}

int main() {
	LL n,k;
	int tests;
	scanf("%d",&tests);
	FOR(zz,1,tests) {
		scanf("%lld %lld",&n,&k);
		LL jum = (LL)1;
		jum <<= jumbit(k);
		LL kanan = (n-k)/jum;
		LL kiri = ( (n-k ) + (jum>>1) ) / jum;
		printf("Case #%d: %lld %lld\n",zz,kiri,kanan);
	}
	
	return 0;
}

//int main() { //BruteForce the pattern
	//list<int> daftar;
	//FOR(n,1,300) {
		////printf("%3d=>",n);
		//daftar.clear();
		//daftar.pb(0); daftar.pb(n+1);
		//REP(k,n) {
			//list<int>::iterator it = daftar.begin();
			//int kiri,kanan = *it;
			//int ind = n+n,indMaks = 0,indMini = 0;
			//list<int>::iterator pos;
			//REP(i,k+1) {
				//kiri = kanan;
				//it++;
				//kanan = *it;
				//int jum = (kanan-kiri-1);
				//if (jum==0) continue;
				
				//int temp = kiri + (jum>>1) + (jum&1);
				//int tempL = temp - kiri - 1;
				//int tempR = kanan - temp - 1; 
				//int tempMaks = max(tempL,tempR);
				//int tempMini = min(tempL,tempR);
				
				//if (tempMini > indMini) {
					//ind = temp;
					//indMini = tempMini;
					//indMaks = tempMaks;
					//pos = it;
				//}
				//else if (tempMini==indMini and tempMaks>indMaks) {
					//ind = temp;
					//indMini = tempMini;
					//indMaks = tempMaks;
					//pos = it;
				//}
				//else if (tempMini==indMini and tempMaks==indMaks and temp<ind) {
					//ind = temp;
					//indMini = tempMini;
					//indMaks = tempMaks;
					//pos = it;
				//}
				////printf("Cek %d %d %d\n",kiri,ind,kanan);
			//}
			//printf("(%d,%d)",indMaks,indMini);
			//daftar.insert(pos,ind);
		//}
		//printf("\n");
	//}
	//return 0;
//}



//Alhamdulillahirabbilalamin 
