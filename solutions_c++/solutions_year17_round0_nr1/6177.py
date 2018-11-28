

#include <iostream>
#include <cstdio>

using namespace std;
int arr[1004];
int helper[1004];
int len;
int solve(string s,int k)
{
    if (s.size() < k){
        if (s.find('-') == -1)
            return 0;
        else
            return -1;
    }
    if (s.size() == k){
        int counter = 0;
        for (int i = 0; i < s.size(); ++i){
            if (s[i] == '-')
                counter++;
        }
        if (counter == 0)
            return 0;
        else if (counter == s.size())
            return 1;
        else
            return -1;
        }
    int swapper = 0;
    int ans = 0;
    for (int i = 0; i <= len - k; ++i){
        if (helper[i] == 1){
            swapper--;
        }
        if (swapper % 2 == 1)
            arr[i] = 1 - arr[i];
        
        if (arr[i] == 0){
            swapper++;
            ans++;
            helper[i + k] = 1;
            arr[i] = 1;
        }
    }
//    for (int i = 0; i < len; ++i)
//        cout << arr[i] << ' ';
//    cout << endl;
    for (int i = len - k + 1; i < len; ++i){
        if (helper[i] == 1)
            swapper--;
        if (swapper % 2 == 1)
            arr[i] = 1 - arr[i];
    }
   
    for (int i = 0; i < len; ++i)
        if (arr[i] == 0)
            return -1;
    return ans;
}
int main(int argc, const char * argv[]) {
    freopen("/Users/Andrew/Desktop/GCJ2017/GCJ2017/A.txt", "r", stdin);
    freopen("/Users/Andrew/Desktop/GCJ2017/GCJ2017/Aans.txt", "w", stdout);
    int tests;
    cin >> tests;
    int testCounter = 1;
    string s;
    int k;
    while (testCounter <= tests) {
        cin >> s;
        len = s.size();
        for (int i = 0; i < len; ++i){
            arr[i] = (s[i] == '+')? 1  : 0;
            helper[i] = 0;
        }
        cin >> k;
        int ans = solve(s,k);
        string out;
        if (ans == -1)
            out = "IMPOSSIBLE";
        else
            out = to_string(ans);
        cout << "Case #" << testCounter << ": " << out << endl;
        testCounter++;
    }
    return 0;
}
