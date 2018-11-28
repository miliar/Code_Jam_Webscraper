// CodeJam 2017
// Problem D
// zintrepid

#include <cassert>
#include <iostream>
#include <string>
#include <tuple>
#include <map>
#include <vector>

using namespace std;

struct Space
{
    bool d;
    bool rc;
    int value;
};
typedef vector<Space> SpaceVector;

struct Piece
{
    int R;
    int C;
    char type;
};
typedef vector<Piece> Pieces;

void ExRC(int N, int x, int y, SpaceVector& v)
{
    assert(!v[y*N+x].rc);
    for (int i=0; i < N; ++i) {
        if (i != x) {
            v[y*N+i].rc = true;
        }
    }
    for (int i=0; i < N; ++i) {
        if (i != y) {
            v[i*N+x].rc = true;
        }
    }
}

void ExD(int N, int x, int y, SpaceVector& v)
{
    assert(!v[y*N+x].d);
    for (int i=x-1,j=y-1; i>=0 && j>=0; --i, --j) {
        v[j*N+i].d = true;
    }
    for (int i=x-1,j=y+1; i>=0 && j<N; --i, ++j) {
        v[j*N+i].d = true;
    }
    for (int i=x+1,j=y-1; i<N && j>=0; ++i, --j) {
        v[j*N+i].d = true;
    }
    for (int i=x+1,j=y+1; i<N && j<N; ++i, ++j) {
        v[j*N+i].d = true;
    }
}

bool DoRun()
{
    int N, M;
    cin >> N >> M;
    if (cin.fail()) return false;
    SpaceVector space(N * N, Space{false, false, 0});

    int score = 0;
    for (int i=0; i < M; ++i) {
        char type;
        int R, C;
        cin >> type >> R >> C;
        int x = C - 1, y = R - 1;
        if (type == '+' || type == 'o') ExD(N, x, y, space);
        if (type == 'x' || type == 'o') ExRC(N, x, y, space);
        if (type == 'o') space[y*N+x].value = 2;
        else space[y*N+x].value = 1;
        score += space[y*N+x].value;
    }
    if (cin.fail()) return false;
    Pieces placedPieces;
    for (int d=0; d < N; ++d) {
        for (int x=d, y=d; x<N; ++x) {
            int i = y*N+x;
            if (!space[i].d && space[i].value == 0) {
                space[i].value = 1;
                ++score;
                ExD(N, x, y, space);
                placedPieces.push_back({y+1, x+1, '+'});
            }
        }
        for (int x=d, y=d+1; y<N; ++y) {
            int i = y*N+x;
            if (!space[i].d && space[i].value == 0) {
                space[i].value = 1;
                ++score;
                ExD(N, x, y, space);
                placedPieces.push_back({y+1, x+1, '+'});
            }
        }
    }
    for (int i=0; i < N * N; ++i) {
        int x=i%N;
        int y=i/N;
        if (!space[i].rc && space[i].value == 0) {
            space[i].value = 1;
            ++score;
            ExRC(N, x, y, space);
            placedPieces.push_back({y+1, x+1, 'x'});
        }
    }
    for (int i=0; i < N * N; ++i) {
        int x=i%N;
        int y=i/N;
        if (!space[i].rc && !space[i].d && space[i].value != 2) {
            score += 2 - space[i].value;
            space[i].value = 2;
            ExD(N, x, y, space);
            ExRC(N, x, y, space);
            for (auto it = placedPieces.begin(); it != placedPieces.end(); ++it) {
                if (it->R == y+1 && it->C == x+1) {
                    placedPieces.erase(it);
                    break;
                }
            }
            placedPieces.push_back({y+1, x+1, 'o'});
        }
    }
    cout << score << ' ' << placedPieces.size();
    for (const Piece& piece : placedPieces)
        cout << '\n' << piece.type << ' ' << piece.R << ' ' << piece.C;
    return true;
}

int main()
{
    int runs;
    cin >> runs;
    for (int i=0; i < runs; ++i) {
        cout << "Case #" << i + 1 << ": ";
        if (!DoRun()) {
            cerr << "RUN FAILED\n";
            return 1;
        }
        cout << "\n";
    }
    cerr << "Success.\n";
    return 0;
}
