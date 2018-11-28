#include <iostream>  
#include <string>
#include <vector>

using namespace std;  

void solve_rec( vector<int>& vNum, size_t beg, size_t end ) {
    if ( beg == end )
        return;
    size_t i;
    for ( i = beg; i < end; ++i ) {
        if ( vNum[i] > vNum[i+1] ) {
            vNum[i] -= 1;
            for ( size_t j = i+1; j <= end; ++j )
                vNum[j] = 9;
            break;
        }
    }

    if ( i == end )
        return;

    solve_rec( vNum, beg, i );
}

string solve( const string& num ) {
    vector<int> vNum (num.size(), 0);
    for ( size_t i = 0; i < num.size(); ++i ) {
        vNum[i] = (num[i] - '0');
    }

    solve_rec( vNum, 0, vNum.size()-1 );

    string ret;
    size_t beg = vNum[0] == 0 ? 1 : 0;
    for ( size_t i = beg; i < vNum.size(); ++i )
        ret += (vNum[i]+'0');
    
    return ret;
}

int main() {
  int t;
  string num;
  
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> num; 
    cout << "Case #" << i << ": " << solve(num) << endl;
  }

  return 0;
}
