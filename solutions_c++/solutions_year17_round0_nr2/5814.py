#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int t, n;
    string s, temp;
    ifstream in("B-large.in");
    ofstream out("output.txt");
    in >> t;
    for(int i = 0; i < t; i++){
        in >> s; temp = s;
        n = temp.length();
        vector<int> a;
        for(int j = 0; j < n - 1; j++){
            if(temp[j] > temp[j+1]){
                int current = j;
                for(; current >= 1; ){
                    if(temp[current] < temp[current-1] + 1) current--;
                    else break;
                }
                if(current == 0 && temp[0] == '1'){
                    temp = string(n-1, '9');
                }
                else{
                    temp[current]--;
                    for(int k = current+1; k < n; k++) temp[k] = '9';
                }
                break;
            }
        }
        out << "Case #" << i+1 << ": " << temp << endl;
    }
    return 0;
}
