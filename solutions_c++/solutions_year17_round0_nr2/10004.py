//#include<bits/stdc++.h>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define pb push_back

# define inOut(a,b) freopen(a,"r",stdin);freopen(b,"w",stdout);
# define RESET(a) memset(a,0,sizeof(a))
# define MEMO(a) memset(a,-1,sizeof(a))
# define DEBUG puts("Debug-Has-Come-Until-Here")


typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main(){
	ios_base::sync_with_stdio(false);
	
	int T, loopT, i,j, panjang;
	string arr;
	cin >> T;
	getline(cin, arr);
	while(loopT < T){
		getline(cin, arr);
		panjang = arr.length();
		
		cout << "Case #" << ++loopT << ": " ;
		if (panjang == 1)
			cout << arr << endl;
		else{
			int activate = 0;
			i = 1;
			while(i < panjang){
//				cout << i << endl;
				if (activate)
					arr[i] = '9';
				else{
					if (arr[i] < arr[i-1]){
//						cout << (arr[i] < arr[i-1]) << endl;
						activate = 1;
						arr[i] = '9';
						j = i-1;
						if (arr[j] > '0')arr[j]--;
						while(true){
							if (arr[j] >= arr[j-1] && arr[j] != '0')break;
							if (j < 1 )break;
							//if (arr[j] < arr[j-1] || arr[j]==0){
								arr[j] = '9';
								if (arr[j-1] > '0')arr[j-1]--;
							//}
							j--;
						}
					}
				}
				i++;
			}
			
			for (i=0; i<panjang; i++)
				if (arr[i] >'0')cout << arr[i];
			cout << endl;
		}
	}
	return 0;
}




