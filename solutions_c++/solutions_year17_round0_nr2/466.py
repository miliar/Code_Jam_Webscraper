
#include <iostream>
#include <vector>
using namespace std;

void main() {
  int T;
  cin >> T;
  for( int iT = 1; iT <= T; ++iT ) {
    long long N;
    cin >> N;
    //cout << "\norig: " << N << ", ";
    vector<int> arr;
    while( N / 10 > 0 ) {
      arr.insert( arr.begin(), N % 10 );
      N /= 10;
    }
    arr.insert( arr.begin(), N % 10 );

    for( int i = 1; i < arr.size(); ++i ) {
      if( arr[i - 1] > arr[i] ) {
        int badPos = i - 1;
        while( badPos >= 0 && arr[badPos] == arr[i - 1] ) badPos--;
        badPos++;
        arr[badPos]--;
        for( int j = badPos + 1; j < arr.size(); ++j ) {
          arr[j] = 9;
        }
        break;
      }
    }

    long long last = 0;
    for( int elem : arr ) last = last * 10 + elem;
    
    cout << "Case #" << iT << ": " << last << endl;
  }

}

