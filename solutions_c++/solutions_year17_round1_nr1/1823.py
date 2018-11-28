#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class test_case{
 public:
  test_case( unsigned t ): t_num( t ){}
  void read_data();
  void solve();
  void print_solution();
 private:
  unsigned t_num;
  stringstream solution;
 private:
  unsigned R,C;
  vector<vector<char>> cake;
};

void test_case::read_data(){
  cin >> R >> C;
  for(unsigned r=0; r<R; ++r){
    string line;
    cin >> line;
    vector<char> vc( line.begin(), line.end() );
    cake.push_back( vc );
  }
}

void test_case::solve(){
  //first row
  for( unsigned c=0; c<C; ++c){
    if( cake[0][c] == '?' ){
      for( unsigned r=1; r < R; ++r ){
        if( cake[r][c] != '?' ){
          cake[0][c] = cake[r][c];
          break;
        }
      }
    }
  }
  // next rows
  for( unsigned rr=1; rr<R; ++rr){
    for( unsigned c=0; c<C; ++c){
      if( cake[rr][c] == '?' ){
        for( int r=rr-1; r >= 0; --r ){
          if( cake[r][c] != '?' ){
            cake[rr][c] = cake[r][c];
            break;
          }
        }
      }
    }
  }
  //empty columns left
  for( unsigned c=0; c<C; ++c ){
    if( cake[0][c] == '?' ){
      for( unsigned r=0; r < R; ++r){
        for( unsigned cc=c+1; cc<C; ++cc){
          if( cake[r][cc] != '?' ){
            cake[r][c] = cake[r][cc];
            break;
          }
        }
      }
    }
  }
  //empty columns right
  for( unsigned c=0; c<C; ++c ){
    if( cake[0][c] == '?' ){
      for( unsigned r=0; r < R; ++r){
        for( int cc=c-1; cc>=0; --cc){
          if( cake[r][cc] != '?' ){
            cake[r][c] = cake[r][cc];
            break;
          }
        }
      }
    }
  }
  for( auto& vc: cake ){
    for( auto c: vc ){
      solution << c;
    }
    solution << "\n";
  }
}

void test_case::print_solution(){
  cout << "Case #" << t_num << ": \n" << solution.str();
}

int main(){
  unsigned T;
  cin >> T;
  for( unsigned t = 1; t <= T; ++t ){
    test_case tc( t );
    tc.read_data();
    tc.solve();
    tc.print_solution();
  }
}
