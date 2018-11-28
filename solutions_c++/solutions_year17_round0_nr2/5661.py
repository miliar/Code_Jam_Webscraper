#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> ii;

void run(const int testcase) {
    string x;
    cin>>x;
    int n = x.size();
    string answer;
    for (int i = 0; i < n; ++i) {
        char best = 0;
        for (char d = '0'; d <= '9'; ++d) {
            string y = answer;
            for (int j = i; j < n; ++j)
                y.push_back(d);
            if (y <= x)
                best = d;
            else
                break;
        }
        answer.push_back(best);
    }
    printf("Case #%d: ", testcase);
    reverse(answer.begin(), answer.end());
    while (!answer.empty() && answer.back() == '0') answer.pop_back();
    reverse(answer.begin(), answer.end());
    if (answer.empty())
        answer = "0";
    cout<<answer<<endl;
}

int32_t main() {
    int testcases;
    cin>>testcases;
    for (int testcase = 1; testcase <= testcases; ++testcase) {
        run(testcase);
    }
}
