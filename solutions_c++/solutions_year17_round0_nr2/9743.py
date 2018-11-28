#include <iostream>
#include <math.h>
using namespace std;

class Node{
public:

    bool isTheLowestToTheRest;
    char currLowestNumber;
    int currLowestNumber_index;

};

Node* isTheLowestToTheRest(const string& str, char c, int startIndex){
    Node* node = new Node();
    node->isTheLowestToTheRest = true;
    for (int i = 0; i < str.length(); i++){
        if (str[i] < c){
            node->currLowestNumber = str[i];
            node->currLowestNumber_index = i + startIndex; // 注意,要記錄的是原本完整str的index,所以需要加回startIndex
            node->isTheLowestToTheRest = false;// 若其中有一個數字小於c(目前最大位數),則回傳false
            return node;
        }
    }
    return node;
}

// greedy
int main(){

    int T;
    cin >> T;
    int caseIndex = 1;
    while(T){
        T--;

        string N;
        cin >> N;
//        cout << "N: " << N << "\n";

        // 檢查是否數字小於最高位數
        bool makeRest9 = false;
        int isZeroTheFisrt = 0;
        for (int i = 0; i < N.length(); i++){
            if (makeRest9){
                N[i] = '9';
//                cout << "N: " << N << "\n";
                continue;
            }

            Node* node = isTheLowestToTheRest(N.substr(i), N[i], i); // O(log10(n))
//            cout << "N[i]: " << N[i] << "\n";
            if (node->isTheLowestToTheRest){
                // 就單純繼續往下跑。每次可確認最左邊的數字
//                cout << "is the lowest" << "\n";
            }else{
                // 先來看看是否還能補救,向前一位數借位使用
                for (int j = node->currLowestNumber_index; j-1 >= i; j--){ // O(n)
//                    cout << "j: " << j << "\n";
                    if (N[j] < N[i]){
                        N[j] = '9'; // 將目前最小數調整為9
                        N[j - 1] -= 1; // 雖然為char,仍然可這樣直接減
//                        cout << "N: " << N << "\n";
                        makeRest9 = true; // 代表有借過位了,則剩下的數字都填9即可
                    }else{
                        i = node->currLowestNumber_index; // 若比對過程,數字沒有在比當下最高位數還小,則直接跳到後面去處理即可
                        break;
                    }// end of if
                }// end of for
            }
//            cout << "N: " << N << "\n";
        }

        if (N[0] == '0'){
            isZeroTheFisrt = 1;
        }
        cout << "Case #" << caseIndex << ": " << N.substr(isZeroTheFisrt) << "\n";
        caseIndex++;

    }


    return 0;
}
