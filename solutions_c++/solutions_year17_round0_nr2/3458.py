#include <iostream>
#include <vector>
using namespace std;

string helper(vector<int> &input){
    int len = input.size();
    for(int i = len - 1; i >= 1; i --){
        if(input[i] < 0)    input[i] = 9;
        if(input[i] < input[i-1]){
            for(int j = i; j < len; j ++)
                input[j] = 9;
            input[i-1] --;
        }
    }

    string res;
    for(int i = 0; i < input.size(); i ++){
        if(res.length() == 0 && input[i] == 0)  continue;
        res += (input[i] + '0');
    }
    return res;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int count = 1, n;
    cin >> n;
    while(n--){
        string k;
        cin >> k;
        vector<int> input(k.length());
        for(int i = 0; i < k.length(); i ++){
            input[i] = int(k[i] - '0');
        }
        string res = helper(input);
        cout << "Case #" << count << ": " << res << endl;
        count ++;
    }
    return 0;
}