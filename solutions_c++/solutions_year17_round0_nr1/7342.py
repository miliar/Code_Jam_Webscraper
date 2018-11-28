#include <iostream>
#include <stdio.h>
#include <cmath>
#include <stdlib.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <ctime>
#include <iomanip>
#define  fi(i,a,b)  for(int i=a;i<b;i++)
#define  fd(i,a,b)  for(int i=a;i>b;i--)
#define  si(n)      scanf("%d",&n);
#define  sc(n)      scanf("%c",&n);
#define  sll(n)     scanf("%lld",&n);
#define  TC         int T; si(T);

using namespace std;

int main(){
	//ios_base::sync_with_stdio(false);
	TC
	string s ; 
	int K ;
	int t = T ;
	while(T--){
		cin >> s >> K ;
		int sz = s.size() ;
		int ans = 0 ;
		fi(i,0,sz-K+1){
			if(s[i] == '-'){
				fi(j,0,K){
					if(s[i+j] == '-') s[i+j] = '+' ;
					else s[i+j] = '-' ; 
				}
				ans++ ;
			}
		}
		int flag = 1 ;
		fi(i,sz-K,sz){
			if(s[i] == '-'){
				flag = 0 ;
				break ;
			}
		}
		cout << "Case #" << t-T << ": " ;
		if(flag) cout << ans << endl ;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
