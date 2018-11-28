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

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }

int main(){
  int T; cin >> T;
  for(int t = 1; t <= T; ++t){
    int R, C; cin >> R >> C;
    vector<string> mycake(R);
    vector< pair<int,int> > initials;
    for(int i = 0; i < R; ++i){
      cin >> mycake[i];
      for(int j = 0; j < C; ++j){
        if(mycake[i][j] != '?')
          initials.push_back(make_pair(i,j));
      }
    }

    for(int i = 0; i < initials.size(); ++i){
      int j = initials[i].first;
      int k = initials[i].second;
      char current = mycake[j][k];
      //cout << current << j << " " << k << endl;
      int mfrom = k, mto = k;
      while(k > 0){
        if(mycake[j][k - 1] == '?'){
          mycake[j][k - 1] = current;
          k--;
        }
        else
          break;
      }
      mfrom = k;

      k = initials[i].second;
      while(k < C - 1){
        if(mycake[j][k + 1] == '?'){
          mycake[j][k + 1] = current;
          k++;
          //cout << k << " ";
        }
        else
          break;
      }
      mto = k;
      //cout << "mfrom: " << mfrom << " mto: " << mto << endl;

      j -= 1;
      while(j >= 0){
        bool valid = true;
        for(int l = mfrom; l <= mto; ++l){
          if(mycake[j][l] != '?'){
            valid = false;
            break;
          }
        }
        if(valid){
          for(int l = mfrom; l <= mto; ++l)
            mycake[j][l] = current;
          j--;
        }
        else
          break;
      }

      j = initials[i].first;
      j += 1;
      //cout << "pass " << j << endl;
      while(j < R){
        bool valid = true;
        for(int l = mfrom; l <= mto; ++l){
          if(mycake[j][l] != '?'){
            valid = false;
            break;
          }
        }
        if(valid){
          for(int l = mfrom; l <= mto; ++l)
            mycake[j][l] = current;
          j++;
        }
        else
          break;
      }
      //cout << "pass2" << endl;
    }
    cout << "Case #" << t << ":" << endl;
    for(int i = 0; i < R; i++){
      for(int j = 0; j < C; ++j)
        cout << mycake[i][j];
      cout << endl;
    }

  }
  return 0;
}
