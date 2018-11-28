#include <iostream>
#include <string> 
#include <vector>
#include <assert.h>

using namespace std;

vector<int> pc;
vector<int> combination;
vector<vector<int> > combination_vec;

void go(int offset, int k) {
  if (k == 0) {
    vector<int> c(combination);
    combination_vec.push_back(c);
    return;
  }
  for (int i=offset; i<=pc.size()-k; ++i) {
    combination.push_back(pc[i]);
    go(i+1, k-1);
    combination.pop_back();
  }
}

string swap(string input, int k, int p) {
    assert(input.size() >= p -1+ k);
    for (int i=p-1; i<p-1+k; i++) {
        if (input[i] == '-')
            input[i] = '+';
        else input[i] = '-';
    }
    return input;
}

string swap_vec(string input, int k, vector<int> moves) {
    for (int i=0; i<moves.size(); i++)
        input = swap(input, k, moves[i]);
    return input;
}

bool are_pancakes_done(string input){
    for (int i=0; i<input.size(); i++)
        if (input[i] == '-')
            return false;
    return true;
}

int main(){
    int T, K;
    string S, test_S;
    cin >> T; 
    for (int i=0; i<T; i++) {
        combination_vec.clear();
        pc.clear();
        cin >> S >> K;
        int thres = S.size() - K + 1;
        for (int j=0; j<thres; ++j)
            pc.push_back(j+1);
        for (int j=1; j<=thres; ++j) {
            // Here we can do only j moves    
            go(0, j);
        }
        bool ok = are_pancakes_done(S);
        if (ok) {
            cout << "Case #" << i+1 << ": 0" << endl;
            continue;
        }
        for (int l=0; l<combination_vec.size(); ++l) {
            if (ok)
                break;
            //cout << "[";
            for (int k=0; k<combination_vec[l].size(); ++k) {
                string s_new = swap_vec(S,K, combination_vec[l]);
                ok = are_pancakes_done(s_new);
                if (ok) {
                    cout << "Case #" << i+1 << ": " << combination_vec[l].size() << endl;
                    break;
                }
            //   cout << combination_vec[l][k] << " ";
            }
            //cout << "]" << endl;
        }
        if (!ok)
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
