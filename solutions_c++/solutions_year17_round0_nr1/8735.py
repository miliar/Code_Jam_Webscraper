#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void getPans(string row, vector<string>& pans, int panSize);

int main() {
    unsigned int t;
    string row;
    int panSize;

    cin >> t;
    for (unsigned int k =1 ; k<=t; ++k){
        int flipCount = 0;
        cin>> row;
        cin>> panSize;
        for(unsigned int i = 0; i<=(row.size()-panSize);++i){
            if (row[i]=='-'){
                for (int j = 0; j < panSize; j++){
                    if (row[i+j] == '-') {
                        row[i+j] = '+';
                    }
                    else{
                        row[i+j] = '-';
                    }
                }
                flipCount++;
            }
        }
        bool allup = true;
        for( unsigned int j = 0; j<=row.size(); j++){
        if (row[j] == '-'){

            allup = false;
            break;
        }
        }

        cout <<"Case #"<<k<<": ";
        if (allup) cout << flipCount;
        else cout << "IMPOSSIBLE";
        cout << endl;
    }

	return 0;
}


