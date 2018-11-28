#include <iostream>
#include <iomanip>
#include <sstream>
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
  int D, N;
  vector<int> start_position;
  vector<int> max_speed;
};

void test_case::read_data(){
  cin >> D >> N;
  for( int n=0; n<N; ++n){
    int sp, ms;
    cin >> sp >> ms;
    start_position.push_back(sp);
    max_speed.push_back(ms);
  }
}

void test_case::solve(){
  long double travel_time = 0;
  for(int n=0; n<N; ++n){
    long double tt = ((long double)( D - start_position[n] )) / max_speed[n];
    if( tt > travel_time ){
      travel_time = tt;
    }
  }
  solution << setprecision(9);
  solution << ( (long double)D/travel_time );
}

void test_case::print_solution(){
  cout << "Case #" << t_num << ": " << solution.str() << endl;
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
