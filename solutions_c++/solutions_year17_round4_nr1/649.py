#include <bits/stdc++.h>

#define mt make_tuple
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

void test(){
  int n, p;
  cin >> n >> p;
  vi mod(p,0);
  for(int i = 0 ; i < n ; i++){
    int a; cin >> a; mod[a%p]++;
  }
  if(p==2){
    cout << mod[0] + (mod[1]+1)/2 << endl;
    return;
  }
  else if(p == 3){
    if(mod[1] < mod[2])
      swap(mod[1],mod[2]);
    cout << mod[0] + mod[2] + (mod[1]-mod[2]+2)/3 << endl;
    return;
  }
  assert(p == 4);
  if(mod[1] > mod[3])
      swap(mod[1],mod[3]);
  if(mod[2]%2 == 0){
    cout << mod[0] + mod[1] + mod[2]/2 + (mod[3]-mod[1]+3)/4 << endl;
    return;
  }
  else{
    if(mod[3]-mod[1]>=2){
      cout << mod[0] + mod[1] + mod[2]/2 + 1 + (mod[3]-mod[1]+1)/4 << endl;
    } 
    else{
      cout << mod[0] + mod[1] + mod[2]/2 + 1 << endl;
    }
  }
}

int main(){
    int t;
    cin >> t;
    for( int i = 1;i<= t;i++){
        cout << "Case #" << i << ": ";
        test();
    }
	return 0;
}
