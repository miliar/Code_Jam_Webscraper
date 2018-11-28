#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define FOR(k,a,b) for(int k=(a); k<(b); k++)

void solve_case(int T){
  int N, R, O, Y, G, B, V;
  cin >> N >> R >> O >> Y >> G >> B >> V;

  if (R > N/2 || Y > N/2 || B > N/2){
  	cout << "Case #" << T << ": IMPOSSIBLE" << endl;
  	return;
  }

  vector<char> list;

  while(max(R, Y) > 0 && max(Y, B) > 0 && max(B, R) > 0){
  	if (R > 0){
  		list.push_back('R');
  		R--;
  	}
  	if (Y > 0){
  		list.push_back('Y');
  		Y--;
  	}
  	if (B > 0){
  		list.push_back('B');
  		B--;
  	}
  }

  int f = 0;
  bool found = false;
  while(max(max(R, Y), B) > 0){
  	found = false;
  	while (!found){
  		if (R > 0 && list[f] != 'R' && list[f+1] != 'R'){
  			list.insert(list.begin()+f+1,'R');
  			R--;
  			found = true;
  		}
  		if (Y > 0 && list[f] != 'Y' && list[f+1] != 'Y'){
  			list.insert(list.begin()+f+1,'Y');
  			Y--;
  			found = true;
  		}
  		if (B > 0 && list[f] != 'B' && list[f+1] != 'B'){
  			list.insert(list.begin()+f+1,'B');
  			B--;
  			found = true;
  		}
  		f++;
  	}
  }

  cout << "Case #" << T << ": ";
  FOR(i,0,list.size()){
  	cout << list[i];
  }
  cout << endl;
}

int main() {
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  	solve_case(i);
  	}
  	return 0;
}