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
	TC
	int t = T; 
	string N ;
	while(T--){
		cin >> N ;
		int sz = N.size() ;
		int i= 0;
		while(i < sz && N[i] == '0')
			i++;
		int flag = 0;	
		fi(j , i+1 , sz){
			if(N[j] < N[j-1]){
				N[j] = '9' ;
				if(flag == 0){
					N[j-1] -= 1 ;
					flag = 1 ;
				}
				int temp = j-1 ;
				while(temp > i){
					if(N[temp] < N[temp-1]){
						N[temp-1] -= 1 ;
					    N[temp] = N[temp+1] ;
					}
					temp-- ;	
				}
			}
		}
	    i= 0;
		while(i < sz && N[i] == '0')
			i++;
			
		cout << "Case #" << t-T << ": " ;
		fi(j, i, sz)
			cout << N[j]  ;
		cout << endl ; 	
	}
	return 0;
}
