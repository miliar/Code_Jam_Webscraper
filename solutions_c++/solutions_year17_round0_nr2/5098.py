# include <cstdlib>
# include <cstdio>
# include <iostream>
# include <cmath>
# include <vector>
# include <map>
# include <set>
# include <sstream>
# include <queue>

using namespace std;

#define __ ios_base::sync_with_stdio(0); cin.tie(0);

template <class T> int toInt(const T &x){
  stringstream s; s << x; int r; s >> r; return r;
}

template <class T> int toLL(const T &x){
  stringstream s; s << x; unsigned long long int r; s >> r; return r;
}

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }

template <class T> char toChar(const T &x)
{ stringstream s; s << x; char r; s >> r; return r; }


int main(){
  int T; cin >> T;
  for(int t = 1; t <= T; ++t){
    string mnum; cin >> mnum;
    if(mnum.size() == 1){
      cout << "Case #" << t << ": " << mnum << endl;
      continue;
    }
    int from = 0;
    for(int i = 0; i < mnum.size() - 1; ++i){
      int current = toInt(mnum[i]);
      int mnext = toInt(mnum[i + 1]);
      //cout << current << " " << mnext << endl;
      if(current > mnext){
        //cout << "que pasa" << endl;
        int new_first_digit = toInt(mnum[from]) - 1;
        mnum[from] = toChar(new_first_digit);
        for(int j = from + 1; j < mnum.size(); ++j)
          mnum[j] = '9';
        break;
      }
      else if(current < mnext){
        from = i + 1;
      }
    }

    cout << "Case #" << t << ": ";
    if(mnum[0] == '0'){
      int i = 0;
      while(mnum[i] == '0') i++;
      while(i < mnum.size()){
        cout << mnum[i];
        i++;
      }
      cout << endl;
    }
    else{
      cout << mnum << endl;
    }
  }
  return 0;
}
