#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <utility>
#include <math.h>

#define FOR(i,x,y) for(int i=x;i<=y;i++)
#define ROF(i,x,y) for(int i=x;i>=y;i--)
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define sz(X) ((int)(X).size()) 
#define MAX_int (1<<31)-1
#define MIN_int -(1<<31)+1

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI; 

int main(){

	int t,n,check;
	int R,O,Y,G,B,V;
	cin >> t;
	for(int lap=1;lap<=t;lap++){
		cin >> n;
		cin >> R >> O >> Y >> G >> B >> V;
		int nB = B;
		vector<char> V;
		check = 0;
		while(R){
			if(Y > 0){
				V.push_back('R');
				R--;
				V.push_back('Y');
				Y--;
			}
			else if(B > 0){
				V.push_back('R');
				R--;
				V.push_back('B');
				B--;
			}
			else {
				check = 1;
				break;
			}
		}
		if(check == 1){
			cout << "Case" << " #" << lap << ": IMPOSSIBLE\n";
			continue;
		}
		while(Y){
			if(B > 0){
				V.push_back('B');
				Y--;
				V.push_back('Y');
				B--;
			}
			else if(sz(V) == 0){
				V.push_back('Y');
				Y--;
			}
			else {
				check = 1;
				break;
			}
		}
		if(check == 1){
			cout << "Case" << " #" << lap << ": IMPOSSIBLE\n";
			continue;
		}
		if(B == nB){
			V.push_back('B');
			B--;
		}
		int AAA = 0;
		while(B){
			int si = sz(V);
			check = 0;
			for(int i=1;i<si;i++){
				if(V[i-1] != 'B' && V[i] != 'B'){
					V.insert(V.begin()+i, 'B');
					B--;
					check = 1;
					break;
				}
			}
			if(check == 0 && V[0] != 'B' && V[si-1] != 'B'){
				V.insert(V.end(), 'B');
				B--;
				check = 1;
			}
			if(check == 0){
				AAA = 1;
				break;
			}
		}
		if(AAA == 1){
			cout << "Case" << " #" << lap << ": IMPOSSIBLE\n";
			continue;
		}
		else {
			cout << "Case" << " #" << lap << ": ";
			int si = sz(V);
			for(int i=0;i<si;i++)cout << V[i];
			cout << "\n";
		}

	}
	
	return 0;
}