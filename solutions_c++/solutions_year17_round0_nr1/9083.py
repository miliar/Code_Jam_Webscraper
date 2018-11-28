#include<iostream>

using namespace std;

void flipl(string &s, int i, int k){
    for(int j = i; j < i+k; j++){
        s[j] = (s[j] == '+' ? '-' : '+');
    }
}

int getMoves(string s, int k){
    int count = 0;
    for(int i =0; i < s.size() - k; i++){
        if (s[i] == '-'){
            flipl(s, i, k);
            count++;
        }
    }
    int countplus = 0;
    for (int i = s.size()-k; i < s.size(); i++){
        if(s[i] == '+'){
            countplus++;
        }
    }
    //cout << s;
    if (countplus == 0)
        return count+1;
    else if(countplus == k)
        return count;
    else
        return -1;
}

int main(){
    int t;
    cin >> t;
    int i =1;
    while(i <= t){
        string s;
        int k;
        cin >> s >>k;
        int resp = getMoves(s, k);
        if(resp < 0)
            cout << "Case #" << i++ << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i++ << ": " << resp << endl;
    }
    return 0;
}