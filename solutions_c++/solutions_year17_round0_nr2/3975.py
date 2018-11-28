#include <iostream>
#include <vector>

using namespace std;

int main() {
    int casos;
    cin >> casos;
    for ( int i = 0 ; i < casos ; i++){
        string num;
        cin >> num;
        string A = "", res = "";
        A.push_back( num[0] );
        int flag = 0;
        for (int j = 1 ; j < num.size() ; j++){
            if(A[j-1] > num[j]) {
                A[flag]--;
                if(A[0] != '0') {
                    res.append(A.begin(),A.begin()+flag+1);
                }else{
                    res.append(A.begin()+1, A.begin()+1+flag);
                }
                res.append(num.size()-flag-1, '9');
            } else {
                A.push_back(num[j]);
                if (A[j] > A[flag]) flag = j;
            }

        }
        if (res == "") res.append(A);
        cout << "Case #" << i+1 << ": " << res << endl;
    }
    return 0;
}