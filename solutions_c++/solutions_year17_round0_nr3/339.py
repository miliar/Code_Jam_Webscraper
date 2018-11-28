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

   for (int i111=0 ; i111<t111; i111++) {
      map<long long, long long> x;
      vector <long long> y;
      long long n,k,m, amin, amax,ml,mr;
      cin >> n >> k;
      y.push_back(n);
      make_heap(y.begin(), y.end());
      x[n] = 1;
      while (k>0) {
         m = y.front();
         pop_heap(y.begin(),y.end());
	      y.pop_back();
         ml= (m-1) >> 1;
         mr= m >> 1;
         //cout << k << ' ' << m << ' ' << x[m] << ' ' << ml << ' ' << mr << endl;
         if (k<=x[m]){
            amin = ml;
            amax = mr;
         }
         k-=x[m];
         if (ml >0 && x.count(ml)==0) {
            x[ml]=x[m];
            y.push_back(ml);
	         push_heap(y.begin(),y.end());
            }
         else
            x[ml]+=x[m];
         if (mr> 0 && x.count(mr)==0) {
            x[mr]=x[m];
            y.push_back(mr);
	         push_heap(y.begin(),y.end());
            }
         else
            x[mr]+=x[m];
      }
	
	   cout << "Case #"<< i111 +1 << ": " <<amax << ' ' << amin << endl;
	}
   return 0;
}
