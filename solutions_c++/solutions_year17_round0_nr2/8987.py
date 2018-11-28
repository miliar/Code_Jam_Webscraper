#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool tidy(long long int x) {
    string num = to_string(x);
    for(int i = 0; i < num.length()-1; i++)
        if(num[i+1] < num[i])
            return false;
    return true;
}

int main() {
    ifstream fin("/Users/uelnily/Downloads/B-small-attempt0.in");
    ofstream cout("/Users/uelnily/Desktop/Practice/Practice/B-small-attempt0.out");
    long long int T, N, C;
    fin >> T;
    C = T;
    while(T--) {
        long long int ans = 0;
        fin >> N;
        for(long long int i = N; i > 0; i--) {
            if(tidy(i)) {
                ans = i;
                break;
            }
        }
        cout << "Case #" << C-T << ": " << ans << endl;
    }
    
    return 0;
}


//#include <iostream>
//#include <fstream>
//#include <algorithm>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//    ifstream fin("/Users/uelnily/Downloads/A-large.in");
//    ofstream fout("/Users/uelnily/Downloads/A-large.out");
//    
//    int T, K, C;
//    string S;
//    
//    fin >> T;
//    C = T;
//    while(T--) {
//        int ans = 0, np = 0;
//        fin >> S >> K;
//        
//        for(int i = 0; i <= (S.length() - K); i++) {
//            if(S[i] == '-') {
//                S[i] = '+';
//                for(int j = 1; j < K; j++) {
//                    if(S[i+j] == '+')
//                        S[i+j] = '-';
//                    else if (S[i+j] == '-')
//                        S[i+j] = '+';
//                }
//                ans++;
//            }
//        }
//        for(long int i = (S.length() - K); i < S.length(); i++) {
//            if(S[i] == '-') {
//                np = 1;
//            }
//        }
//        
//        if(np) {
//            fout << "Case #" << C-T << ": IMPOSSIBLE" << endl;
//            continue;
//        }
//        
//        fout << "Case #" << C-T << ": " << ans << endl;
//    }
//    
//    return 0;
//}
