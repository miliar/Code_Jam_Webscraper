#include <iostream>
#include <string>
#include <fstream>

using namespace std;

bool valid (const string& S)
{
    const size_t size = S.size();
    for (size_t i = 0; i < size - 1; ++i) {
        if (S[i] > S[i+1])
            return false;
    }
    return true;
}

string make (char ch, int N) {
    string result;
    for (int i = 0; i < N; ++i){
        result.push_back(ch);
    }
    return result;
}


int nextNotEqual(const string& S, char ch, int idx)
{
    for (int i = idx; i < S.size(); ++i) {
        if (S[i] != ch)
            return idx;
    }
    return S.size()-1;
}

string solve(string N)
{
    if (N.size() == 1) {
        return N;
    }

    string result;
    for (int i = 0; i < N.size() - 1; ++i) {
        if (N[i] < N[i+1]) {
            result += N[i];
            if (i == N.size()-2){
                result += N[i+1];
            }
        } else if (N[i] == N[i+1]) {
            int idx = nextNotEqual(N, N[i+1], i+2);
            if (N[idx] == N[i]) {
                return result + make(N[i], N.size() - i);
            } else if (N[idx] > N[i]) {
                result += N[i];
            } else {
                if (N[i] == '1') {
                    return result + make('9', N.size() - i - 1);
                } else {
                    result += N[i] - 1;
                }
            }
        } else {
            if (N[i] == '1') {
                return result + make('9', N.size() - i - 1);
            } else {
                result += N[i] - 1;
                return result + make('9', N.size() - i - 1);
            }
        }
    }


    return result;
}

int main()
{
    int T;
    string N;

    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> T;
    for (int i = 0; i < T; ++i) {
        fin >> N;
        fout << "Case #" << i+1 <<": ";
        string result = solve(N);
        if (!valid(result)) {
            cout <<"ERROR in: "<<N<<" out: "<<result << endl;
        }
        fout << solve(N) << endl;
    }



    return 0;
}

