#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <limits>
#include <queue>

using namespace std;

char flip_pancake(char c) { return c == '+' ? '-' : '+'; }

string flip(const string & s, int idx, int k) {
    string out(s);
    transform(s.begin() + idx, s.begin() + idx + k, out.begin() + idx, flip_pancake);
    return out;
}

int get_solution(const string & s, int K, const string & solution) {
    const unsigned long L = s.length() - K + 1;
    queue<pair<string,int>> q;
    map<size_t,int> memo;
    map<size_t,int>::iterator it;
    
    q.push(pair<string,int>(s, 0));
    memo.insert(pair<size_t,int>(hash<string>()(s), 0));
    
    while (q.size() > 0) {
        // Retrieve the current pancake stack and the number of flips it has taken us to get there
        pair<string,int> curr = q.front();
        q.pop();
        
        // Try every combination of K-flips on the pancake stack
        for (int i = 0; i < L; i++) {
            string f = flip(curr.first, i, K);
            
            // Have we seen this new flipped state before?
            it = memo.find(hash<string>()(f));
            if (it != memo.end()) {
                // Update state with current if it is a better solution than before
                if (curr.second >= it->second) {
                    break;
                }
                it->second = curr.second + 1;
            } else {
                memo.insert(pair<size_t,int>(hash<string>()(f), curr.second + 1));
            }
            q.push(pair<string,int>(f,curr.second + 1));
        }
    }
    
    it = memo.find(hash<string>()(solution));
    return it == memo.end() ? -1 : it->second;
}

int main(int argc, const char * argv[]) {
    int T;
    cin >> T; cin.ignore();
    
    for (int t = 0; t < T; t++) {
        string s;
        getline(cin, s);
        size_t space_pos = s.find(' ', 0);
        int K = stoi(s.substr(space_pos));
        s = s.substr(0, space_pos);
        
        string happy_stack;
        for (int i = 0; i < s.length(); i++) happy_stack += '+';
        
        int solution = get_solution(s, K, happy_stack);
        
        cout << "Case #" << (t + 1) << ": ";
        if (solution < 0) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << solution << endl;
        }
    }
    
    return 0;
}
