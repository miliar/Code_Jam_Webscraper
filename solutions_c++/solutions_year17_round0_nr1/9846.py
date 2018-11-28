#include <iostream>
#include <fstream>

using namespace std;

void flip(string &s, int pos) {
    if (s[pos] == '+')
        s[pos] = '-';
    else s[pos] = '+';
}
int main() {
    std::ifstream in("../input.txt");
    std::cin.rdbuf(in.rdbuf());

    std::ofstream out("../output_small.txt");
    std::cout.rdbuf(out.rdbuf());
    int T, K;
    string s;
    cin>>T;
    for (int t = 1;t <= T;++t) {
        cin>>s;
        cin>>K;
        int l = s.length();
        int times = 0;
        bool possible = true;
        for (int i = 0;i < l;++i) {
            if (s[i] == '+')
                continue;
            if (i+K > l) {
                cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
                possible = false;
                break;
            }
            for (int k = 0;k < K && i+k < l;++k) {
                flip(s, i+k);
            }
            times++;
        }
        if (possible)
            cout<<"Case #"<<t<<": "<<times<<endl;
    }

    return 0;
}