#include <iostream>


using namespace std;


void flipper(string& s, int pos ,int k){

  for(int i = pos; i < pos+k; i++){
    if(s[i] == '-')s[i] = '+';
    else s[i] = '-';
  }
}

int main(){

  int tc,k,ans;
  string s;
  bool done;



  cin >> tc;
  for(int caseno = 1; caseno <= tc; caseno++){
    cin >> s;
    cin >> k; // ---+-++-
    ans = 0;
    done = false;
    int len = s.length();
    for (int i = 0; i <= len - k; i++){

      if(s[i] == '-'){
        ans++;
        flipper(s,i,k);
      }
    }

    for(int i = len - k; i < len; i++){

      if(s[i] == '-'){
        cout << "Case #" << caseno <<  ": " <<  "IMPOSSIBLE" << endl;
        done = true;
        break;
      }

  }

  if(!done){
    cout << "Case #" << caseno <<  ": " << ans << endl;
  }

    }


}
