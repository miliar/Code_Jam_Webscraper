#include<iostream>
#include<string>
#include<map>
#include<queue>

using namespace std;

typedef struct Problem Problem;

struct Problem {
    string faces;
    int size;
};

int isGoal(string& faces) {
    for (int i = 0; i < faces.length(); ++i)
        if (faces[i] == '-')
            return 0;
    return 1;
}

int main() {
    
    int T;
    cin >> T;
    string faces;
    int size;
    
    for (int i = 0; i < T; ++i) {
        Problem currProblem;
        cin >> currProblem.faces;
        cin >> currProblem.size;
        
        map<string, string> parent;
        parent[currProblem.faces] = "";
        
        queue<string> frontier;
        frontier.push(currProblem.faces);
        
        int found = 0;
        
        while (!frontier.empty()) {
            
            string curr = frontier.front();
            string next;
            frontier.pop();
            
            if (isGoal(curr)) {
                int steps = 0;
                while (parent[curr] != "") {
                    steps += 1;
                    curr = parent[curr];
                }
                cout << "Case #" << i + 1 << ": " << steps << endl;
                found = 1;
                break;
            }
            
            for (int k = 0; k <= curr.length() - currProblem.size; ++k) {
                next = curr;
                for (int p = k; p < k + currProblem.size; ++p) {
                    if (next[p] == '+')
                        next[p] = '-';
                    else
                        next[p] = '+';
                }
                if (parent.find(next) == parent.end()) {
                    frontier.push(next);
                    parent[next] = curr;
                }
                    
            } 
        }
        
        if (!found)
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        
        // cout << currProblem.faces << " " << currProblem.size << endl;
    }
    return 0;
}