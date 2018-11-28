#include <iostream>
#include <fstream>
#include <climits>
#include <array>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>

using namespace std;
unsigned long long arr[20];
unsigned long long num(int index) {
  if (arr[index] != 0) return arr[index];
  return arr[index]=(unsigned long long) pow( 10, index );
}
int main(){
  memset(arr, 0 , sizeof arr);
	ifstream infile;
	ofstream outfile;
	infile.open("input.txt");
	outfile.open("output.txt");
  int T;
  unsigned long long N, ans;
	infile >> T;
	for (int j = 0; j<T; j++) {
    infile >> N;
    ans = 0;
    cout << j+1 << " " << T << " " << N << endl;
    if ( N < 10) ans = N;
    for ( int i = 19; i > 0; i--) {
      if ( (N / num(i)) % 10> (N % num(i)) / num(i-1) ) {
        while (( N / num(i+1) % 10 == (N % num(i+1)) / num(i) )) {
          i++;
          cout << N / num(i+1) % 10 << " " << (N % num(i+1)) / num(i)  << endl;
        }
        ans = ( (N / num(i) - 1) * num(i) ) + (num(i)-1);
        break;
      }
    }
    if (ans == 0 ) ans = N;
		outfile << "Case #" << j+1 <<": "<<ans<<endl;
  }
	infile.close();
	outfile.close();
}
