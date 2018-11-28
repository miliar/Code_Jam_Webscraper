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

int main() {
	int tests;
	string s;
	int k,len;
	scanf("%d",&tests);
	FOR(zz,1,tests) {
		cin >> s;
		scanf("%d",&k);
		len = s.length();
		int ans = 0;
		FOR(i,0,len-k) {
			if (s[i]=='-') {
				REP(j,k) {
					if (s[i+j]=='+') s[i+j] = '-';
					else s[i+j] = '+';
				}
				ans++;
			}
		}
		
		bool cek = true;
		REP(i,len) if (s[i]=='-') cek = false;
		if (cek) printf("Case #%d: %d\n",zz,ans);
		else printf("Case #%d: IMPOSSIBLE\n",zz);
	}
	
	return 0;
}

//Alhamdulillahirabbilalamin                   
