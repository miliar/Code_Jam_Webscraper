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
   string s;
   int n,k;
   int a[20];
   for (int i111=0 ; i111<t111; i111++) {
	   cin >> s;
	   n = s.size();
	   k=0;
	   a[0]=s[s.size()-1]-48;
	   for (int i=s.size()-2; i>=0; i--){
	      if (s[i]-48 > a[n-i-2]) {
	         a[n-i-1] = s[i]-49;
	         k=n-i-1;   
	      } else
	         a[n-i-1] = s[i]-48;
	   }
	   cout << "Case #"<< i111 +1 << ": ";
	   int j = n-1;
	   while (a[j]==0 && j>=k)
	      j--;
	   while (j>=k) {
	      cout << a[j];
	      j--;
	   }
	   while (j>=0) {
	      cout << '9';
	      j--;
	   } 
	   cout << endl;
	}
   return 0;
}
