#include <iostream>
#include <string>

using namespace std;

string pancakes;
int K;

void flip( int i ){
  for( int k=0; k < K; ++k ){
    pancakes[i+k] = (pancakes[i+k] == '+') ? '-' : '+';
  }
}

bool is_solved(){
  for( char c: pancakes ){
    if( c != '+'){
      return false;
    }
  }
  return true;
}

int main(){
  int T;
  cin >> T;
  for( int t= 1; t<=T; ++t ){
    cin >> pancakes >> K;

    int flips = 0;
    for( int i=0; i < pancakes.length() - (K-1); ++i ){
      if( pancakes[i] == '-' ){
        flip( i );
        ++flips;
      }
    }

    if( is_solved() ){
      cout << "Case #" << t << ": " << flips << endl;
    } else {
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
  }
}
