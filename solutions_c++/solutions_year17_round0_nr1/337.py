// Created by alex_mat21. And it works!

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include <bitset>
#include <string> 
#include <iomanip>
#include <cmath>
#include <utility>
 
#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define vi vector<int>
#define fs first
#define sd second
#define pii pair<int,int>

using namespace std;

int main () {
   int t111;
   cin >> t111;

   int k,m;
   string s;
   int a[1010];
   for (int i111=0 ; i111<t111; i111++) {
	   cin >> s;
	   cin >> k;
	   m=0;
	   FOR(i,s.size()) {
	      if (s[i] == '+')
	         a[i] = 1;
	      else   
	         a[i] = 0;
	   }
	   FOR(i, s.size()) {
	      if (!a[i]) {
	         if (i <= s.size() - k) {
	            m++;
	            for (int j=i; j<i+k; j++)
	               a[j] = 1-a[j];
	         } else {
	            m=-1;
	            break;
	         }
	      }
	   }
	   if (m>=0)
	      cout << "Case #"<< i111 +1 << ": " << m << endl;
	   else
	      cout << "Case #"<< i111 +1 << ": IMPOSSIBLE" << endl;
	}
   return 0;
}
