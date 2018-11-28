#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>

using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

#define cin fin
#define cout fout

const int MAXN = 1e3 + 10;
int t , n , D;
int K[MAXN];
int S[MAXN];

void input(int x){
  cin >> D >> n;
  double hours = 0;
  for(int i = 0 ; i < n ; i++){
    cin >> K[i] >> S[i];
    hours = max(hours , (double)(D - K[i]) / S[i]);
  }
  cout << "Case #" << x << ": " << setprecision(15) << D/hours << endl;
}

int main(){
  cin >> t;
  for(int i = 0 ; i < t ; i++)
    input(i+1);
  return 0;
}
