#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <utility>
using namespace std;

typedef char c;
typedef vector<c> vc;
typedef vector<vc> vvc;

bool canPutChild(const vvc &board, const map<c, pair<int, int> > &childLocations, c child, int row, int col) {
    //cerr << "canPutChild" << child << "\n";
    if (board[row][col] != '?' && board[row][col] != child) return false;
    pair<int, int> origLoc = childLocations.at(child);
    for (int i = min(origLoc.first, row); i <= max(origLoc.first, row); i++)
        for (int j = min(origLoc.second, col); j <= max(origLoc.second, col); j++)
            if (board[i][j] != '?' && board[i][j] != child)
                return false;
    return true;
}

void putChild(vvc &board, const map<c, pair<int, int> > &childLocations, c child, int row, int col) {
    //cerr << "putChild\n";
    pair<int, int> origLoc = childLocations.at(child);
    for (int i = min(origLoc.first, row); i <= max(origLoc.first, row); i++)
        for (int j = min(origLoc.second, col); j <= max(origLoc.second, col); j++)
            board[i][j] = child;
}

void unputChild(vvc &board, const map<c, pair<int, int> > &childLocations, c child, int row, int col) {
    //cerr << "unputChild began\n";
    pair<int, int> origLoc = childLocations.at(child);
    for (int i = min(origLoc.first, row); i <= max(origLoc.first, row); i++)
        for (int j = min(origLoc.second, col); j <= max(origLoc.second, col); j++)
            board[i][j] = '?';
    board[origLoc.first][origLoc.second] = child;
    //cerr << "unputChild ended\n";
}

bool isDone(const vvc &board) {
    for (auto a : board)
        for (auto b : a)
            if (b == '?')
                return false;
    return true;
}

void print(const vvc &board) {
    for (auto a : board) {
        for (auto b : a) 
            cout << b;
        cout << endl;
    }
}

bool begin(vvc board, list<c> children, const map<c, pair<int, int> > &childLocations) {
    if (isDone(board)) {
        print(board);
        return true;
    }
    if (children.empty()) {
        return false;
    }

    c newChild = children.front();
    children.pop_front();
    pair<int, int> origLoc = childLocations.at(newChild);

    //cerr << "putting child " << newChild << endl;

    for (int i = 0; i <= origLoc.first; i++) {
        for (int j = 0; j <= origLoc.second; j++) {
            if (canPutChild(board, childLocations, newChild, i,j)) {

                for (int k = origLoc.first; k < board.size(); k++) {
                    for (int l = origLoc.second; l < board[k].size(); l++) {
                        //cerr << "size=" << board[k].size();
                        //cerr << "l=" << l << endl;

                        if (canPutChild(board, childLocations, newChild, k,l) && 
                            canPutChild(board, childLocations, newChild, i,l) &&
                            canPutChild(board, childLocations, newChild, k,j)) {

                            putChild(board, childLocations, newChild, i,j);
                            putChild(board, childLocations, newChild, i,l);
                            putChild(board, childLocations, newChild, k,j);
                            putChild(board, childLocations, newChild, k,l);


                            //cerr << i << j << k << l << endl;

                            //print(board);

                            if (begin(board, children, childLocations))
                                return true;

                            unputChild(board, childLocations, newChild, k,l);
                            unputChild(board, childLocations, newChild, k,j);
                            unputChild(board, childLocations, newChild, i,l);
                            unputChild(board, childLocations, newChild, i,j);
                        }
                    }
                }

            }
        }
    }
    return false;
}

void solve() {
    int R,C;
    cin >> R >> C;

    vvc board(R,vc(C));
    set<c> childrenSet;
    map<c, pair<int, int> > childLocations;

    for (int i = 0; i < R; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < C; j++) {
            board[i][j] = s[j];
            childrenSet.insert(s[j]);
            childLocations[s[j]] = make_pair(i,j);
        }
    }
    childrenSet.erase('?');
    childLocations.erase('?');
    list<c> children(childrenSet.begin(), childrenSet.end());

    begin(board, children, childLocations);
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ":\n";
        solve();
    }
}
