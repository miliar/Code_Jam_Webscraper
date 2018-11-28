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

//        int N;
//        cin >> N;
//        int level = log10 (N);
//        cout << "level: " << level << "\n";
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

            Node* node = isTheLowestToTheRest(N.substr(i), N[i], i);
//            cout << "N[i]: " << N[i] << "\n";
            if (node->isTheLowestToTheRest){
                // 就單純繼續往下跑。每次可確認最左邊的數字
//                cout << "is the lowest" << "\n";
            }else{
                // 先來看看是否還能補救(end-當第一位數被迫要-1時)
//                cout << "is not the lowest" << "\n";
//                cout << "node->currLowestNumber_index: " << node->currLowestNumber_index << "\n";
//                cout << "i: " << i << "\n";
                for (int j = node->currLowestNumber_index; j-1 >= i; j--){
//                    cout << "j: " << j << "\n";
                    if (N[j] < N[i]){
//                        N[j] = N[i]; // 將目前最小數調整為當下最高位數
                        N[j] = '9'; // 將目前最小數調整為9
                        N[j - 1] -= 1; // 雖然為char,仍然可這樣直接減
//                        cout << "N: " << N << "\n";
                        makeRest9 = true;
//                        i = node->currLowestNumber_index; // node->currLowestNumber_index是第一個找到最小的數,代表之前的數字都已經挑到最大的了,而現在因為借位,後面的數字就都直接填9
//                        if ( (j-1) == '0' ){
//                            // 代表不妙,最高位數被減到了
////                            makeRest9 = true;
////                            N[i] = node->currLowestNumber;
////                            N[i];
//                            isZeroTheFisrt = 1;
////                            if (N[i] == '0') isZeroTheFisrt = 1;
//                        }
                    }else{
                        i = node->currLowestNumber_index;
                        break;
                    }// end of if
                }// end of for


                // 若剩餘數列中,有人比目前最高位數還要小,則將最高位數調整為此最小數
//                N[i] = node->currLowestNumber;
//                makeRest9 = true;

//                cout << "N[" << i << "]: " << " is minus 1" << "\n";
            }
//            cout << "N: " << N << "\n";
        }

//        cout << "N: " << N.substr(isZeroTheFisrt) << "\n";
        if (N[0] == '0'){
            isZeroTheFisrt = 1;
        }
        cout << "Case #" << caseIndex << ": " << N.substr(isZeroTheFisrt) << "\n";
        caseIndex++;

    }


    return 0;
}
