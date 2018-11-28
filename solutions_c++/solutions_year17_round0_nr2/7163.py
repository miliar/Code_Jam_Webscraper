

#include <iostream>
#include <vector>


using namespace std;


void solve(int testnumber){
    string input;
    cin >> input;
    vector<int> v;
    int startpos = 0;
    string out;

    for(char c : input){
        v.push_back(static_cast<int>(c) - static_cast<int>('0'));
    }

    bool found = false;

    for (int i = 1; i < v.size(); i++){
        if (v[i] == v[i-1]){

        } else if (v[i] > v[i-1]){
            out.append(input.begin() + startpos, input.begin() + i);
            startpos = i;
        } else {
            if (startpos != 0 or (v[startpos] - 1 != 0))
                out.append(to_string(v[startpos] - 1));
            for (int k = startpos + 1; k < v.size(); k++)
                out.push_back('9');
            found = true;
            break;
        }
    }

    if (!found)
        out = input;

    cout << "Case #" << testnumber << ": " << out << std::endl;;

}


int main(){
    int testcases;
    cin >> testcases;
    for (int i = 0; i < testcases; i++){
        solve(i+1);
    }
}

