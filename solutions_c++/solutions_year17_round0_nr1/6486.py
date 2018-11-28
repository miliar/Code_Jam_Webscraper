#include<iostream>
#include<fstream>
using namespace std;

void inverse(string &s, int i , int k) {
    //cout << " inverse " ;
    for (int j = i; j < i + k; j++) {
        //cout << s[j];
        if (s[j] == '+') 
            s[j] = '-';
        else s[j] = '+';
    }
    //cout << endl;
}

int swappan(string &s, int k) {

    //cout << " string " << s << " flips " << k << endl;
    int len = s.length(), i =0, count =0;
    for(i =0; i < (len - k + 1) ; i++) {
        if (s[i] == '+') continue;
        inverse(s, i, k);
        ++count;
    }
    for (int j = i; j < len; j ++)  {
        if (s[j] == '-') return -1;
    }
            return count;

}

int main() {

    int input;
    string s;
    int flips;

    ifstream file("input.txt");
    file >> input;
    for (int i =0; i< input ; i++) {
        file >> s;
        file >> flips;
        int output = swappan(s, flips);
        if (output == -1)
            cout << "Case #" << i + 1 << ": "<< "IMPOSSIBLE" <<endl;
        else
            cout << "Case #" << i + 1 << ": " << output << endl;
    }
}
